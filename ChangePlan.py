# -*- coding: utf-8 -*-

import sys, os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QLabel, QPushButton
import warnings
from datetime import datetime
from PyQt5.QtCore import pyqtSignal

warnings.filterwarnings('ignore', category=DeprecationWarning)

def get_resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối đến resource (icon, image, etc.)"""
    if getattr(sys, 'frozen', False):  
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class ListItemWidget(QWidget):
    """Custom widget cho mỗi item trong list"""
    def __init__(self, ext_code, plan_code, parent=None):
        super().__init__(parent)
        self.ext_code = ext_code
        self.plan_code = plan_code
        self.parent_list = parent
        
        # Tạo layout
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Label hiển thị ext_code và plan_code
        self.label = QLabel(f"{ext_code} - {plan_code}")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        
        # Nút xóa với icon
        self.delete_btn = QPushButton()
        self.delete_btn.setFixedSize(40, 40)
        self.delete_btn.setToolTip("Xóa item này")
        self.delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)
        
        # Set icon cho nút xóa
        icon_path = get_resource_path("images/recycle-bin.png")
        if os.path.exists(icon_path):
            icon = QtGui.QIcon(icon_path)
            self.delete_btn.setIcon(icon)
            self.delete_btn.setIconSize(QtCore.QSize(24, 24))
        else:
            self.delete_btn.setText("X")
            self.delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16pt;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #c82333;
                }
            """)
        
        # Kết nối sự kiện xóa
        self.delete_btn.clicked.connect(self.delete_item)
        
        # Thêm vào layout
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.delete_btn)
        
        self.setLayout(layout)
    
    def delete_item(self):
        """Xóa item hiện tại"""
        reply = QtWidgets.QMessageBox.question(
            self.parent_list.parent(),
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa mã '{self.ext_code}' (Plan: {self.plan_code}) khỏi danh sách kế hoạch?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            # Xóa trong view
            for i in range(self.parent_list.count()):
                item = self.parent_list.item(i)
                widget = self.parent_list.itemWidget(item)
                if widget == self:
                    self.parent_list.takeItem(i)
                    print(f"Đã xóa item tại index {i}")
                    break
            
            # Gọi hàm cập nhật (sẽ xóa trong database và cập nhật lại sort_order)
            parent_window = self.parent_list.parent()
            if hasattr(parent_window, 'update_order_after_delete'):
                # Truyền thông tin item đã xóa
                parent_window.update_order_after_delete(self.ext_code, self.plan_code)
            else:
                print("Warning: update_order_after_delete not found")

class Ui_ChangePlan(object):
    def setupUi(self, ChangePlan):
        ChangePlan.setObjectName("ChangePlan")
        ChangePlan.resize(700, 550)  # Tăng kích thước để chứa nút xóa
        ChangePlan.setMinimumSize(QtCore.QSize(700, 550))
        ChangePlan.setMaximumSize(QtCore.QSize(700, 550))   
        self.listWidget = QtWidgets.QListWidget(ChangePlan)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 520, 481))
        self.listWidget.setObjectName("listWidget")
        
        # Style cho listWidget để item to hơn
        self.listWidget.setStyleSheet("""
            QListWidget {
                font-size: 14pt;
                font-weight: bold;
                font-family: Arial;
                outline: none;
            }
            QListWidget::item {
                padding: 0px;
                border-bottom: 1px solid #dee2e6;
                min-height: 55px;
            }
            QListWidget::item:selected {
                background-color: transparent;
            }
        """)
        
        self.SavePlan = QtWidgets.QPushButton(ChangePlan)
        self.SavePlan.setEnabled(False)
        self.SavePlan.setGeometry(QtCore.QRect(540, 60, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SavePlan.setFont(font)
        self.SavePlan.setStyleSheet("QPushButton {\n"
"    background-color: #198754;\n"
"    color: white;\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"\n"
"    padding: 6px 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #20a464;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #146c43;\n"
"}")
        icon = QtGui.QIcon()
        icon_path = get_resource_path("images/save.png")
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SavePlan.setIcon(icon)
        self.SavePlan.setIconSize(QtCore.QSize(32, 32))
        self.SavePlan.setObjectName("SavePlan")
        
        self.OperatorChangePlan = QtWidgets.QLineEdit(ChangePlan)
        self.OperatorChangePlan.setGeometry(QtCore.QRect(540, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OperatorChangePlan.setFont(font)
        self.OperatorChangePlan.setEchoMode(QtWidgets.QLineEdit.Password)
        self.OperatorChangePlan.setObjectName("OperatorChangePlan")

        self.retranslateUi(ChangePlan)
        QtCore.QMetaObject.connectSlotsByName(ChangePlan)

    def retranslateUi(self, ChangePlan):
        _translate = QtCore.QCoreApplication.translate
        ChangePlan.setWindowTitle(_translate("ChangePlan", "Change Plan"))
        self.SavePlan.setText(_translate("ChangePlan", "Lưu\n"
"Save"))
        self.OperatorChangePlan.setPlaceholderText(_translate("ChangePlan", "Operator Code"))


class ChangePlanWindow(QtWidgets.QWidget):
    # Khai báo signal ở đây
    plan_changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChangePlan()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện
        self.ui.OperatorChangePlan.returnPressed.connect(self.check_operator)
        self.ui.SavePlan.clicked.connect(self.save_plan_order)
        
        # Biến lưu operator_code đã xác thực
        self.validated_operator = None
        self.original_order = []  # Lưu thứ tự ban đầu để so sánh
        self.current_plan_code = None  # Lưu plan_code hiện tại để sử dụng khi lưu
    
    def check_operator(self):
        """Kiểm tra operator trong database"""
        operator_input = self.ui.OperatorChangePlan.text().strip()
        
        if not operator_input:
            QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập mã Operator!")
            return
        
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Kiểm tra operator tồn tại
            cursor.execute('SELECT operator_code, operator_name FROM operator WHERE operator_code = ?', (operator_input,))
            result = cursor.fetchone()
            
            if result:
                operator_code, operator_name = result
                self.validated_operator = operator_code
                
                # Disable ô nhập operator
                self.ui.OperatorChangePlan.setEnabled(False)
                
                # Load danh sách plan vào listWidget
                self.load_plan_list()
                
                # Enable listWidget và cho phép kéo thả
                self.ui.listWidget.setEnabled(True)
                self.ui.listWidget.setDragDropMode(QtWidgets.QListWidget.InternalMove)
                
            else:
                QtWidgets.QMessageBox.warning(self, "Lỗi", f"Operator '{operator_input}' không tồn tại trong database!")
                self.ui.OperatorChangePlan.clear()
                self.ui.OperatorChangePlan.setFocus()
                
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Không thể kết nối database: {str(e)}")
        finally:
            if conn:
                conn.close()
    
    def load_plan_list(self):
        """Load danh sách ext_code và plan_code từ bảng plan vào listWidget theo sort_order"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Lấy tất cả dữ liệu từ bảng plan, sắp xếp theo sort_order
            cursor.execute('''
                SELECT ext_code, plan_code, id, sort_order 
                FROM plan 
                ORDER BY sort_order, plan_code, id
            ''')
            
            plans_data = cursor.fetchall()
            
            if not plans_data:
                QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không có dữ liệu kế hoạch trong database!")
                return
            
            # Xóa dữ liệu cũ trong listWidget
            self.ui.listWidget.clear()
            
            # Lưu dữ liệu gốc
            self.original_order = []
            
            # Thêm các item vào listWidget
            for ext_code, plan_code, record_id, sort_order in plans_data:
                # Tạo item và custom widget
                item = QListWidgetItem()
                item.setSizeHint(QtCore.QSize(0, 60))
                
                # Tạo widget cho item
                widget = ListItemWidget(ext_code, plan_code, self.ui.listWidget)
                
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, widget)
                
                # Lưu thông tin vào widget để có thể truy xuất sau
                widget.record_id = record_id
                widget.original_sort_order = sort_order
                
                self.original_order.append({
                    'ext_code': ext_code,
                    'plan_code': plan_code,
                    'id': record_id,
                    'sort_order': sort_order
                })
            
            # Enable nút Save
            self.ui.SavePlan.setEnabled(True)
            
            # Hiển thị tổng số item lên title
            self.setWindowTitle(f"Change Plan - Tổng số: {len(plans_data)} mã")
            
            # Cho phép kéo thả
            self.ui.listWidget.setDragDropMode(QtWidgets.QListWidget.InternalMove)
            
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Không thể đọc dữ liệu: {str(e)}")
        finally:
            if conn:
                conn.close()

    def get_current_order(self):
        """Lấy thứ tự hiện tại từ listWidget"""
        current_order = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            widget = self.ui.listWidget.itemWidget(item)
            if widget:
                current_order.append({
                    'ext_code': widget.ext_code,
                    'plan_code': widget.plan_code
                })
        return current_order

    def update_sort_order_after_drag(self):
        """Cập nhật sort_order sau khi kéo thả"""
        # Lấy thứ tự hiện tại từ listWidget
        current_order = self.get_current_order()
        
        if not current_order:
            return
        
        # Kiểm tra xem có thay đổi thứ tự không
        current_ext_codes = [item['ext_code'] for item in current_order]
        original_ext_codes = [item['ext_code'] for item in self.original_order]
        
        if current_ext_codes == original_ext_codes:
            return
        
        # Cập nhật lại sort_order trong database tạm thời
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            cursor.execute('BEGIN TRANSACTION')
            
            # Cập nhật sort_order tạm thời để lưu vị trí mới
            for idx, item in enumerate(current_order):
                cursor.execute('''
                    UPDATE plan 
                    SET sort_order = ? 
                    WHERE ext_code = ? AND plan_code = ?
                ''', (idx, item['ext_code'], item['plan_code']))
            
            conn.commit()
            
            # Cập nhật original_order
            self.original_order = current_order.copy()
            
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            print(f"Lỗi khi cập nhật sort_order: {str(e)}")
        finally:
            if conn:
                conn.close()

    def update_order_after_delete(self, deleted_ext_code=None, deleted_plan_code=None):
        """Cập nhật sau khi xóa item"""
        
        # Nếu có thông tin item đã xóa, xóa khỏi database
        if deleted_ext_code and deleted_plan_code:
            conn = None
            try:
                conn = sqlite3.connect('extruder.sqlite')
                cursor = conn.cursor()
                
                # Xóa item khỏi database
                cursor.execute('''
                    DELETE FROM plan 
                    WHERE ext_code = ? AND plan_code = ?
                ''', (deleted_ext_code, deleted_plan_code))
                
                print(f"Đã xóa trong database: {deleted_ext_code} - {deleted_plan_code}")
                
                # Ghi vào history
                cursor.execute('''
                    INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (deleted_ext_code, self.validated_operator, 
                    'DELETE_FROM_PLAN', deleted_plan_code,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                
                conn.commit()
                
            except sqlite3.Error as e:
                if conn:
                    conn.rollback()
                QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Lỗi khi xóa trong database:\n{str(e)}")
                return
            finally:
                if conn:
                    conn.close()
        
        # Lấy thứ tự hiện tại từ listWidget
        current_order = self.get_current_order()
        
        if not current_order:
            # Nếu không còn item nào, hỏi có muốn đóng cửa sổ không
            reply = QtWidgets.QMessageBox.question(
                self,
                "Thông báo",
                "Danh sách kế hoạch đã trống.\nBạn có muốn đóng cửa sổ này không?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.Yes
            )
            if reply == QtWidgets.QMessageBox.Yes:
                self.close()
            else:
                # Nếu không đóng, cập nhật original_order rỗng
                self.original_order = []
                self.setWindowTitle(f"Change Plan - Tổng số: 0 mã")
            return
        
        # Cập nhật lại sort_order trong database cho các item còn lại
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            cursor.execute('BEGIN TRANSACTION')
            
            # Cập nhật sort_order mới cho các item còn lại
            for idx, item in enumerate(current_order):
                cursor.execute('''
                    UPDATE plan 
                    SET sort_order = ? 
                    WHERE ext_code = ? AND plan_code = ?
                ''', (idx, item['ext_code'], item['plan_code']))
                
                # Ghi vào history
                cursor.execute('''
                    INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (item['ext_code'], self.validated_operator, f'REORDER_AFTER_DELETE_TO_{idx}', 
                    item['plan_code'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            conn.commit()
            
            # Cập nhật original_order
            self.original_order = current_order.copy()
            
            # Cập nhật title
            self.setWindowTitle(f"Change Plan - Tổng số: {len(current_order)} mã")
            
            # Nhóm theo plan_code để hiển thị
            plan_groups = {}
            for item in current_order:
                plan_code = item['plan_code']
                if plan_code not in plan_groups:
                    plan_groups[plan_code] = 0
                plan_groups[plan_code] += 1
            
            plan_summary = "\n".join([f"  - {plan_code}: {count} mã" for plan_code, count in plan_groups.items()])
            
            # QtWidgets.QMessageBox.information(
            #     self,
            #     "Thành công",
            #     f"Đã xóa item khỏi danh sách và cập nhật lại thứ tự!\n\n"
            #     f"Số lượng còn lại: {len(current_order)} mã.\n"
            #     f"Chi tiết theo plan_code:\n{plan_summary}"
            # )
            
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Lỗi khi cập nhật thứ tự:\n{str(e)}")
        finally:
            if conn:
                conn.close()
                
    def save_plan_order(self):
        """Lưu thứ tự mới của plan vào database (chỉ update sort_order, giữ nguyên plan_code)"""
        
        # Lấy thứ tự hiện tại từ listWidget
        current_order = self.get_current_order()
        
        if not current_order:
            QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không có dữ liệu để lưu!")
            return
        
        # Xác nhận lưu thay đổi
        reply = QtWidgets.QMessageBox.question(
            self,
            "Xác nhận",
            f"Bạn có chắc chắn muốn thay đổi thứ tự kế hoạch?\n\n"
            f"Tổng số mã: {len(current_order)}\n"
            f"Số lượng plan_code: {len(set([item['plan_code'] for item in current_order]))}\n\n"
            f"Hành động này sẽ cập nhật thứ tự trong database.",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply != QtWidgets.QMessageBox.Yes:
            return
        
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Bắt đầu transaction
            cursor.execute('BEGIN TRANSACTION')
            
            # Cập nhật sort_order cho từng record dựa trên vị trí hiện tại
            updated_count = 0
            for idx, item in enumerate(current_order):
                ext_code = item['ext_code']
                plan_code = item['plan_code']
                
                # Update sort_order theo vị trí mới
                cursor.execute('''
                    UPDATE plan 
                    SET sort_order = ? 
                    WHERE ext_code = ? AND plan_code = ?
                ''', (idx, ext_code, plan_code))
                
                if cursor.rowcount > 0:
                    updated_count += 1
                    
                    # Ghi vào history
                    cursor.execute('''
                        INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (ext_code, self.validated_operator, f'UPDATE_SORT_ORDER_TO_{idx}', plan_code,
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # Commit transaction
            conn.commit()
            
            # Cập nhật original_order với thứ tự mới
            self.original_order = current_order.copy()
            
            # Nhóm theo plan_code để hiển thị chi tiết
            plan_groups = {}
            for item in current_order:
                plan_code = item['plan_code']
                if plan_code not in plan_groups:
                    plan_groups[plan_code] = 0
                plan_groups[plan_code] += 1
            
            plan_summary = "\n".join([f"  - {plan_code}: {count} mã" for plan_code, count in plan_groups.items()])
            
            # QtWidgets.QMessageBox.information(
            #     self,
            #     "Thành công",
            #     f"Đã lưu thứ tự kế hoạch mới!\n\n"
            #     f"Tổng số: {updated_count}/{len(current_order)} mã.\n"
            #     f"Chi tiết theo plan_code:\n{plan_summary}"
            # )
            
            # Phát signal thông báo đã thay đổi
            self.plan_changed.emit()
            
            # Đóng cửa sổ
            self.close()
                
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Lỗi khi lưu thứ tự:\n{str(e)}")
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ChangePlanWindow()
    window.show()
    sys.exit(app.exec_())