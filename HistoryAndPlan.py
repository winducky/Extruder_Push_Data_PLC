import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import warnings
import os
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

class Ui_HistoryPlan(QtWidgets.QWidget):
    history_plan = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Kết nối sự kiện
        self.DateFillterHistory.dateChanged.connect(self.load_history)
        
        # Load dữ liệu ban đầu
        self.load_planning()
        self.load_history()
    
    def setupUi(self, HistoryPlan):
        HistoryPlan.setObjectName("HistoryPlan")
        HistoryPlan.resize(1011, 708)
        HistoryPlan.setMinimumSize(QtCore.QSize(1011, 708))
        HistoryPlan.setMaximumSize(QtCore.QSize(1011, 708))
        
        self.groupBox = QtWidgets.QGroupBox(HistoryPlan)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 491, 701))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # Sử dụng QListWidget thay vì QListView để dễ dàng custom item
        self.ViewPlanning = QtWidgets.QListWidget(self.groupBox)
        self.ViewPlanning.setGeometry(QtCore.QRect(10, 80, 471, 611))
        self.ViewPlanning.setObjectName("ViewPlanning")
        # Chặn click chọn item
        self.ViewPlanning.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ViewPlanning.setFocusPolicy(QtCore.Qt.NoFocus)  # Không nhận focus
        self.ViewPlanning.setStyleSheet("""
            QListWidget {
                font-size: 12pt;
                font-family: Arial;
                outline: none;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #dee2e6;
                min-height: 45px;
            }
            QListWidget::item:hover {
                background-color: transparent;
            }
        """)
        
        self.groupBox_2 = QtWidgets.QGroupBox(HistoryPlan)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 0, 491, 701))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # Sử dụng QListWidget thay vì QListView để dễ dàng custom item
        self.ViewHistory = QtWidgets.QListWidget(self.groupBox_2)
        self.ViewHistory.setGeometry(QtCore.QRect(10, 80, 471, 611))
        self.ViewHistory.setObjectName("ViewHistory")
        # Chặn click chọn item
        self.ViewHistory.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ViewHistory.setFocusPolicy(QtCore.Qt.NoFocus)  # Không nhận focus
        self.ViewHistory.setStyleSheet("""
            QListWidget {
                font-size: 12pt;
                font-family: Arial;
                outline: none;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #dee2e6;
                min-height: 45px;
            }
            QListWidget::item:hover {
                background-color: transparent;
            }
        """)
        
        self.DateFillterHistory = QtWidgets.QDateEdit(self.groupBox_2)
        self.DateFillterHistory.setGeometry(QtCore.QRect(240, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DateFillterHistory.setFont(font)
        self.DateFillterHistory.setAlignment(QtCore.Qt.AlignCenter)
        self.DateFillterHistory.setCalendarPopup(True)
        self.DateFillterHistory.setDateTime(QtCore.QDateTime.currentDateTime())
        self.DateFillterHistory.setObjectName("DateFillterHistory")
        
        self.retranslateUi(HistoryPlan)
        QtCore.QMetaObject.connectSlotsByName(HistoryPlan)
    
    def retranslateUi(self, HistoryPlan):
        _translate = QtCore.QCoreApplication.translate
        HistoryPlan.setWindowTitle(_translate("HistoryPlan", "Lịch Sử Và Kế Hoạch"))
        self.label.setText(_translate("HistoryPlan", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Kế Hoạch Chạy\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Planning\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_2.setText(_translate("HistoryPlan", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Lịch Sử Chạy\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"History\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
    
    def load_planning(self):
        """Load kế hoạch hiện tại từ bảng plan"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Lấy tất cả dữ liệu từ bảng plan, sắp xếp theo sort_order
            cursor.execute('''
                SELECT ext_code, plan_code, sort_order 
                FROM plan 
                ORDER BY sort_order, id
            ''')
            
            plans = cursor.fetchall()
            
            # Xóa dữ liệu cũ
            self.ViewPlanning.clear()
            
            if not plans:
                # Hiển thị thông báo không có dữ liệu
                item = QListWidgetItem("📋 Không có kế hoạch nào trong database")
                item.setForeground(QtGui.QColor(150, 150, 150))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ViewPlanning.addItem(item)
                return
            
            # Thêm các item vào ViewPlanning
            for ext_code, plan_code, sort_order in plans:
                # Format hiển thị: [sort_order] ext_code - plan_code
                display_text = f"[{sort_order}] {ext_code} - {plan_code}"
                item = QListWidgetItem(display_text)
                
                # Set font
                font = QtGui.QFont()
                font.setPointSize(11)
                item.setFont(font)
                
                # Set màu sắc cho sort_order
                if sort_order == 0:
                    item.setForeground(QtGui.QColor(0, 120, 215))  # Màu xanh cho item đầu
                else:
                    item.setForeground(QtGui.QColor(0, 0, 0))  # Màu đen cho item khác
                
                self.ViewPlanning.addItem(item)
            
            # Cập nhật số lượng item
            self.ViewPlanning.setToolTip(f"Tổng số: {len(plans)} kế hoạch")
            
        except sqlite3.Error as e:
            print(f"Lỗi database khi load planning: {str(e)}")
            item = QListWidgetItem(f"❌ Lỗi: {str(e)}")
            item.setForeground(QtGui.QColor(255, 0, 0))
            self.ViewPlanning.addItem(item)
        finally:
            if conn:
                conn.close()
    
    def load_history(self):
        """Load lịch sử từ bảng history theo ngày được chọn, operator = SYSTEM"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Lấy ngày được chọn từ DateFilter
            selected_date = self.DateFillterHistory.date().toString("yyyy-MM-dd")
            print(f"Load history cho ngày: {selected_date}")
            
            # Lấy dữ liệu từ history với điều kiện: operator_code = 'SYSTEM' và timestamp theo ngày
            cursor.execute('''
                SELECT ext_code, timestamp, plan_code, action
                FROM history 
                WHERE operator_code = 'SYSTEM'
                AND DATE(timestamp) = ?
                ORDER BY id ASC
            ''', (selected_date,))
            
            histories = cursor.fetchall()
            
            # Xóa dữ liệu cũ
            self.ViewHistory.clear()
            
            if not histories:
                # Hiển thị thông báo không có dữ liệu
                item = QListWidgetItem(f"📋 Không có lịch sử nào cho ngày {selected_date}")
                item.setForeground(QtGui.QColor(150, 150, 150))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ViewHistory.addItem(item)
                return
            
            # Thêm các item vào ViewHistory
            for ext_code, timestamp, plan_code, action in histories:
                # Chỉ hiển thị các action là LOAD_THE_PROGRAM
                if 'LOAD_THE_PROGRAM' in action:
                    # Format timestamp: dd/mm/yyyy hh:mm
                    try:
                        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                        formatted_time = dt.strftime("%d/%m/%Y %H:%M")
                    except:
                        formatted_time = timestamp
                    
                    # Format hiển thị: ext_code - timestamp (dd/mm/yyyy hh:mm)
                    display_text = f"{ext_code} - {formatted_time}"
                    item = QListWidgetItem(display_text)
                    
                    # Set font
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    item.setFont(font)
                    
                    # Set màu sắc
                    item.setForeground(QtGui.QColor(0, 100, 0))  # Màu xanh lá
                    
                    self.ViewHistory.addItem(item)
            
            # Cập nhật số lượng item
            self.ViewHistory.setToolTip(f"Tổng số: {self.ViewHistory.count()} lịch sử cho ngày {selected_date}")
            
            # Nếu không có item nào được thêm (do không có LOAD_THE_PROGRAM)
            if self.ViewHistory.count() == 0:
                item = QListWidgetItem(f"📋 Không có lịch sử LOAD_THE_PROGRAM cho ngày {selected_date}")
                item.setForeground(QtGui.QColor(150, 150, 150))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ViewHistory.addItem(item)
            
        except sqlite3.Error as e:
            print(f"Lỗi database khi load history: {str(e)}")
            item = QListWidgetItem(f"❌ Lỗi: {str(e)}")
            item.setForeground(QtGui.QColor(255, 0, 0))
            self.ViewHistory.addItem(item)
        finally:
            if conn:
                conn.close()
    
    def refresh_data(self):
        """Refresh dữ liệu (gọi khi có thay đổi từ bên ngoài)"""
        self.load_planning()
        self.load_history()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_HistoryPlan()
    window.show()
    sys.exit(app.exec_())