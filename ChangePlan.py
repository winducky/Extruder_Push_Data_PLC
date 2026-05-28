# -*- coding: utf-8 -*-

import sys, os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import warnings
from datetime import datetime
from PyQt5.QtCore import pyqtSignal

warnings.filterwarnings('ignore', category=DeprecationWarning)
def get_resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối đến resource (icon, image, etc.)"""
    if getattr(sys, 'frozen', False):  
        base_path = os.path.dirname(sys.executable)  # Lấy thư mục chứa file .exe
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

class Ui_ChangePlan(object):
    # Không khai báo signal ở đây
    def setupUi(self, ChangePlan):
        ChangePlan.setObjectName("ChangePlan")
        ChangePlan.resize(654, 495)
        self.listWidget = QtWidgets.QListWidget(ChangePlan)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 461, 481))
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
                padding: 12px;
                border-bottom: 1px solid #dee2e6;
                min-height: 55px;
            }
            QListWidget::item:selected {
                background-color: #0d6efd;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #e9ecef;
            }
        """)
        
        self.SavePlan = QtWidgets.QPushButton(ChangePlan)
        self.SavePlan.setEnabled(False)
        self.SavePlan.setGeometry(QtCore.QRect(480, 60, 161, 51))
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
        self.OperatorChangePlan.setGeometry(QtCore.QRect(480, 10, 161, 41))
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
        """Load danh sách ext_code từ bảng plan vào listWidget theo sort_order"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Kiểm tra xem cột sort_order có tồn tại không
            cursor.execute("PRAGMA table_info(plan)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if 'sort_order' in columns:
                # Lấy dữ liệu theo sort_order
                cursor.execute('SELECT ext_code FROM plan ORDER BY sort_order, id')
            else:
                # Nếu chưa có cột sort_order, lấy theo id
                cursor.execute('SELECT ext_code FROM plan ORDER BY id')
            
            plans = cursor.fetchall()
            
            if not plans:
                QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không có dữ liệu kế hoạch trong database!")
                return
            
            # Xóa dữ liệu cũ trong listWidget
            self.ui.listWidget.clear()
            
            # Thêm các item vào listWidget
            self.original_order = []
            for idx, plan in enumerate(plans):
                ext_code = plan[0]
                item = QListWidgetItem(ext_code)
                
                # Set font đậm và to hơn
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                item.setFont(font)
                
                # Set chiều cao item
                item.setSizeHint(QtCore.QSize(0, 50))
                
                self.ui.listWidget.addItem(item)
                self.original_order.append(ext_code)
            
            # Enable nút Save
            self.ui.SavePlan.setEnabled(True)
            
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Không thể đọc dữ liệu: {str(e)}")
        finally:
            if conn:
                conn.close()
    
    def save_plan_order(self):
        """Lưu thứ tự mới của plan vào database (không xóa dữ liệu)"""
        
        # Lấy thứ tự hiện tại từ listWidget
        current_order = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            current_order.append(item.text())
        
        # Kiểm tra xem có thay đổi thứ tự không
        if current_order == self.original_order:
            QtWidgets.QMessageBox.information(self, "Thông báo", "Không có thay đổi về thứ tự!")
            return
        
        # Xác nhận lưu thay đổi
        reply = QtWidgets.QMessageBox.question(
            self,
            "Xác nhận",
            f"Bạn có chắc chắn muốn thay đổi thứ tự kế hoạch?\n\n"
            f"Số lượng mã: {len(current_order)}\n\n"
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
            
            # Kiểm tra xem cột sort_order có tồn tại không
            cursor.execute("PRAGMA table_info(plan)")
            columns = [column[1] for column in cursor.fetchall()]
            
            # Nếu chưa có cột sort_order, thêm mới
            if 'sort_order' not in columns:
                cursor.execute('ALTER TABLE plan ADD COLUMN sort_order INTEGER DEFAULT 0')
                print("Đã thêm cột sort_order vào bảng plan")
            
            # Bắt đầu transaction
            cursor.execute('BEGIN TRANSACTION')
            
            # Cập nhật sort_order cho từng record
            for idx, ext_code in enumerate(current_order):
                cursor.execute('UPDATE plan SET sort_order = ? WHERE ext_code = ?', (idx, ext_code))
                
                # Ghi vào history cho từng thay đổi
                cursor.execute('''
                    INSERT INTO history (ext_code, operator_code, action, timestamp)
                    VALUES (?, ?, ?, ?)
                ''', (ext_code, self.validated_operator, f'UPDATE_SORT_ORDER_TO_{idx}', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # Commit transaction
            conn.commit()
            
            # Cập nhật original_order
            self.original_order = current_order.copy()
            
            QtWidgets.QMessageBox.information(
                self,
                "Thành công",
                f"Đã lưu thứ tự kế hoạch mới!\n\nSố lượng: {len(current_order)} mã."
            )
            
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