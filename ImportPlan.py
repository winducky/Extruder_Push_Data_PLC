import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import warnings
import pandas as pd
import os
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
    
    return os.path.join(base_path, relative_path)
class Ui_ImportPlan(object):
    def setupUi(self, ImportPlan):
        ImportPlan.setObjectName("ImportPlan")
        ImportPlan.resize(664, 140)
        ImportPlan.setMinimumSize(QtCore.QSize(664, 140))
        ImportPlan.setMaximumSize(QtCore.QSize(664, 140))
        
        self.ImportFilePath = QtWidgets.QLineEdit(ImportPlan)
        self.ImportFilePath.setEnabled(False)
        self.ImportFilePath.setGeometry(QtCore.QRect(10, 10, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ImportFilePath.setFont(font)
        self.ImportFilePath.setAutoFillBackground(False)
        self.ImportFilePath.setText("")
        self.ImportFilePath.setReadOnly(False)
        self.ImportFilePath.setObjectName("ImportFilePath")
        
        self.btnImportPlan = QtWidgets.QPushButton(ImportPlan)
        self.btnImportPlan.setEnabled(False)
        self.btnImportPlan.setGeometry(QtCore.QRect(490, 80, 161, 51))
        self.btnImportPlan.setMinimumSize(QtCore.QSize(151, 51))
        self.btnImportPlan.setMaximumSize(QtCore.QSize(1111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnImportPlan.setFont(font)
        self.btnImportPlan.setStyleSheet("QPushButton {\n"
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
        icon_path = get_resource_path("images/import.png")
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnImportPlan.setIcon(icon)
        self.btnImportPlan.setIconSize(QtCore.QSize(32, 32))
        self.btnImportPlan.setObjectName("btnImportPlan")
        
        self.OperatorChangePlan = QtWidgets.QLineEdit(ImportPlan)
        self.OperatorChangePlan.setGeometry(QtCore.QRect(490, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OperatorChangePlan.setFont(font)
        # Set password mode - ẩn ký tự
        self.OperatorChangePlan.setEchoMode(QtWidgets.QLineEdit.Password)
        self.OperatorChangePlan.setObjectName("OperatorChangePlan")

        self.retranslateUi(ImportPlan)
        QtCore.QMetaObject.connectSlotsByName(ImportPlan)

    def retranslateUi(self, ImportPlan):
        _translate = QtCore.QCoreApplication.translate
        ImportPlan.setWindowTitle(_translate("ImportPlan", "Import Plan"))
        self.ImportFilePath.setPlaceholderText(_translate("ImportPlan", "Chọn File Kế Hoạch"))
        self.btnImportPlan.setText(_translate("ImportPlan", "Nhập\n"
"Import"))
        self.OperatorChangePlan.setPlaceholderText(_translate("ImportPlan", "Operator Code"))


class ImportPlanWindow(QtWidgets.QWidget):
    plan_imported = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImportPlan()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện
        self.ui.OperatorChangePlan.returnPressed.connect(self.check_operator)
        self.ui.btnImportPlan.clicked.connect(self.import_plan)
        self.ui.ImportFilePath.textChanged.connect(self.check_file_path)
        
        # Biến lưu operator_code đã xác thực
        self.validated_operator = None
    
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
                
                # Disable ô nhập operator và giữ giá trị
                self.ui.OperatorChangePlan.setEnabled(False)
                
                # Enable các trường khác
                self.ui.ImportFilePath.setEnabled(True)
                self.ui.btnImportPlan.setEnabled(True)

                # Open explorer để chọn file kế hoạch .xlsx, .xls, .csv
                options = QtWidgets.QFileDialog.Options()
                file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                    self,
                    "Chọn File Kế Hoạch",
                    "",
                    "Excel Files (*.xlsx *.xls *.xlsm);;CSV Files (*.csv)",
                    options=options
                )
                if file_path:
                    self.ui.ImportFilePath.setText(file_path) 

            else:
                QtWidgets.QMessageBox.warning(self, "Lỗi", f"Operator '{operator_input}' không tồn tại trong database!")
                self.ui.OperatorChangePlan.clear()
                self.ui.OperatorChangePlan.setFocus()
                
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Không thể kết nối database: {str(e)}")
        finally:
            if conn:
                conn.close()
    
    def check_file_path(self):
        """Kiểm tra file path khi có thay đổi"""
        file_path = self.ui.ImportFilePath.text().strip()
        if file_path and self.validated_operator:
            self.ui.btnImportPlan.setEnabled(True)
        else:
            self.ui.btnImportPlan.setEnabled(False)
    
    def read_excel_file(self, file_path):
        """Đọc file Excel và lấy dữ liệu từ cột B (index 1) từ dòng B2 trở đi"""
        try:
            # Đọc file Excel
            df = pd.read_excel(file_path, header=None)
            
            # Lấy cột B (index 1) từ dòng 2 (index 1) trở đi
            # Bỏ qua các dòng trống và NaN
            ext_codes = df.iloc[1:, 1].dropna().tolist()
            
            # Chuyển đổi sang string và loại bỏ khoảng trắng
            ext_codes = [str(code).strip() for code in ext_codes if str(code).strip()]
            
            return ext_codes
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Đọc File", f"Không thể đọc file Excel:\n{str(e)}")
            return []
    
    def read_csv_file(self, file_path):
        """Đọc file CSV và lấy dữ liệu từ cột B (cột thứ 2) từ dòng 2 trở đi"""
        try:
            # Đọc file CSV với nhiều encoding khác nhau
            encodings = ['utf-8', 'latin1', 'cp1252', 'utf-16']
            df = None
            
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, header=None, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            
            if df is None:
                raise Exception("Không thể đọc file CSV với bất kỳ encoding nào")
            
            # Lấy cột thứ 2 (index 1) từ dòng 2 (index 1) trở đi
            ext_codes = df.iloc[1:, 1].dropna().tolist()
            
            # Chuyển đổi sang string và loại bỏ khoảng trắng
            ext_codes = [str(code).strip() for code in ext_codes if str(code).strip()]
            
            return ext_codes
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Đọc File", f"Không thể đọc file CSV:\n{str(e)}")
            return []
    
    def ensure_sort_order_column(self, cursor):
        """Kiểm tra và thêm cột sort_order nếu chưa có"""
        cursor.execute("PRAGMA table_info(plan)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'sort_order' not in columns:
            cursor.execute('ALTER TABLE plan ADD COLUMN sort_order INTEGER DEFAULT 0')
            print("Đã thêm cột sort_order vào bảng plan")
            return True
        return False
    
    def import_plan(self):
        """Xử lý import kế hoạch (xóa dữ liệu cũ trước khi import và thêm sort_order)"""
        file_path = self.ui.ImportFilePath.text().strip()
        
        if not file_path:
            QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn file kế hoạch!")
            return
        
        # Kiểm tra file tồn tại
        if not os.path.exists(file_path):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "File không tồn tại!")
            return
        
        # Đọc dữ liệu từ file
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension in ['.xlsx', '.xls', '.xlsm']:
            ext_codes = self.read_excel_file(file_path)
        elif file_extension == '.csv':
            ext_codes = self.read_csv_file(file_path)
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Định dạng file không được hỗ trợ!")
            return
        
        if not ext_codes:
            QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không tìm thấy dữ liệu ExtCode trong file (cột B từ dòng 2 trở đi)!")
            return
        
        # Xác nhận import
        reply = QtWidgets.QMessageBox.question(
            self, 
            "Xác nhận Import", 
            f"⚠️ CẢNH BÁO: Toàn bộ dữ liệu cũ trong bảng PLAN sẽ bị XÓA!\n\n"
            f"Tìm thấy {len(ext_codes)} mã ExtCode mới.\n\n"
            f"Danh sách mã mới:\n{', '.join(ext_codes[:10])}{'...' if len(ext_codes) > 10 else ''}\n\n"
            f"Bạn có chắc chắn muốn thay thế toàn bộ dữ liệu không?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply != QtWidgets.QMessageBox.Yes:
            return
        
        # Import vào database
        conn = None
        success_count = 0
        error_count = 0
        
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Kiểm tra và thêm cột sort_order nếu chưa có
            self.ensure_sort_order_column(cursor)
            
            # Bắt đầu transaction
            cursor.execute('BEGIN TRANSACTION')
            
            # Xóa hết dữ liệu cũ trong bảng plan
            cursor.execute('DELETE FROM plan')
            deleted_count = cursor.rowcount
            print(f"Đã xóa {deleted_count} dòng dữ liệu cũ trong bảng plan")
            
            # Ghi vào history hành động xóa
            cursor.execute('''
                INSERT INTO history (ext_code, operator_code, action, timestamp)
                VALUES (?, ?, ?, ?)
            ''', ('ALL', self.validated_operator, 'CLEAR_PLAN_TABLE', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # Import dữ liệu mới với sort_order
            for idx, ext_code in enumerate(ext_codes):
                try:
                    # Thêm mới vào bảng plan với sort_order
                    cursor.execute('INSERT INTO plan (ext_code, sort_order) VALUES (?, ?)', (ext_code, idx))
                    success_count += 1
                    
                    # Ghi vào bảng history cho từng mã
                    cursor.execute('''
                        INSERT INTO history (ext_code, operator_code, action, timestamp)
                        VALUES (?, ?, ?, ?)
                    ''', (ext_code, self.validated_operator, f'IMPORT_PLAN_SORT_ORDER_{idx}', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    
                except sqlite3.Error as e:
                    error_count += 1
                    print(f"Lỗi khi import ExtCode '{ext_code}': {str(e)}")
                    continue
            
            # Commit transaction
            conn.commit()
            
            # Hiển thị kết quả
            result_message = f"Kết quả import:\n\n"
            result_message += f"🗑️ Đã xóa dữ liệu cũ: {deleted_count}\n"
            result_message += f"✅ Import thành công: {success_count}\n"
            result_message += f"❌ Lỗi: {error_count}\n"
            result_message += f"📊 Tổng số mã mới: {len(ext_codes)}\n"
            result_message += f"🎯 Đã thêm sort_order từ 0 đến {len(ext_codes)-1}"
            
            QtWidgets.QMessageBox.information(self, "Kết quả Import", result_message)
            
            # Nếu có dữ liệu được import thành công, đóng cửa sổ
            if success_count > 0:
                self.plan_imported.emit()
                self.close()
                        
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            QtWidgets.QMessageBox.critical(self, "Lỗi Database", f"Lỗi khi import dữ liệu:\n{str(e)}")
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImportPlanWindow()
    window.show()
    sys.exit(app.exec_())