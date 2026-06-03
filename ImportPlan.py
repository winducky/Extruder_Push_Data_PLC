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
        """Đọc file Excel, mỗi dòng lấy ext_code từ cột B và plan_code từ cột C"""
        try:
            # Đọc file Excel
            df = pd.read_excel(file_path, header=None)
            
            data_list = []
            
            # Duyệt từ dòng 2 (index 1) đến hết
            for idx in range(1, len(df)):
                # Lấy ext_code từ cột B (index 1)
                ext_code_value = df.iloc[idx, 1] if len(df.columns) > 1 else None
                # Lấy plan_code từ cột C (index 2)
                plan_code_value = df.iloc[idx, 2] if len(df.columns) > 2 else None
                
                if pd.notna(ext_code_value) and pd.notna(plan_code_value):
                    ext_code = str(ext_code_value).strip()
                    plan_code = str(plan_code_value).strip()
                    if ext_code and plan_code:
                        data_list.append((ext_code, plan_code))
            
            return data_list
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi Đọc File", f"Không thể đọc file Excel:\n{str(e)}")
            return []
    
    def read_csv_file(self, file_path):
        """Đọc file CSV, mỗi dòng lấy ext_code từ cột B và plan_code từ cột C"""
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
            
            data_list = []
            
            # Duyệt từ dòng 2 (index 1) đến hết
            for idx in range(1, len(df)):
                # Lấy ext_code từ cột B (index 1)
                ext_code_value = df.iloc[idx, 1] if len(df.columns) > 1 else None
                # Lấy plan_code từ cột C (index 2)
                plan_code_value = df.iloc[idx, 2] if len(df.columns) > 2 else None
                
                if pd.notna(ext_code_value) and pd.notna(plan_code_value):
                    ext_code = str(ext_code_value).strip()
                    plan_code = str(plan_code_value).strip()
                    if ext_code and plan_code:
                        data_list.append((ext_code, plan_code))
            
            return data_list
            
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
        """Xử lý import kế hoạch:
        1. Xóa hết dữ liệu trong bảng plan
        2. Kiểm tra từng dòng: nếu plan_code đã được SYSTEM LOAD_THE_PROGRAM trong ngày thì bỏ qua
        3. Thêm các dòng chưa được load vào plan với sort_order theo thứ tự trong file
        """
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
            data_list = self.read_excel_file(file_path)
        elif file_extension == '.csv':
            data_list = self.read_csv_file(file_path)
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Định dạng file không được hỗ trợ!")
            return
        
        if not data_list:
            QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không tìm thấy dữ liệu trong file!")
            return
        
        # Hiển thị danh sách dữ liệu đọc được để debug
        print(f"Đọc được {len(data_list)} dòng dữ liệu")
        for ext_code, plan_code in data_list[:5]:
            print(f"ExtCode: {ext_code}, PlanCode: {plan_code}")
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        print(f"Ngày hiện tại: {current_date}")
        
        conn = None
        valid_data = []  # Danh sách dữ liệu hợp lệ (ext_code, plan_code)
        invalid_data = []  # Danh sách dữ liệu không hợp lệ (ext_code, plan_code, lý do)
        
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Kiểm tra từng dòng trong file theo plan_code
            for ext_code, plan_code in data_list:
                if not ext_code or not plan_code:
                    continue
                    
                plan_code = plan_code.strip()
                ext_code = ext_code.strip()
                
                # Kiểm tra plan_code đã được SYSTEM LOAD_THE_PROGRAM trong ngày chưa
                cursor.execute('''
                    SELECT *
                    FROM history 
                    WHERE operator_code = 'SYSTEM'
                    AND plan_code = ?
                    AND DATE(timestamp) = ?
                    LIMIT 1
                ''', (plan_code, current_date))
                
                result = cursor.fetchone()
                
                if result:
                    # Plan code đã được SYSTEM load trong ngày -> không thêm
                    invalid_data.append((ext_code, plan_code))
                    print(f"⚠️ PlanCode '{plan_code}' (ExtCode: {ext_code}) đã được SYSTEM LOAD trong ngày - KHÔNG IMPORT")
                else:
                    # Plan code chưa được load -> được thêm
                    valid_data.append((ext_code, plan_code))
                    print(f"✅ PlanCode '{plan_code}' (ExtCode: {ext_code}) chưa được load - SẼ IMPORT")
            
            # Nếu có dữ liệu không hợp lệ, hiển thị cảnh báo
            if invalid_data:
                warning_msg = f"🚫 Có {len(invalid_data)} dòng KHÔNG được import do plan_code đã được SYSTEM LOAD trong ngày:\n\n"
                for ext_code, plan_code in invalid_data[:10]:
                    warning_msg += f"  - {plan_code} (ExtCode: {ext_code})\n"
                if len(invalid_data) > 10:
                    warning_msg += f"  ... và {len(invalid_data) - 10} dòng khác"
                warning_msg += f"\n\n⚠️ Các dòng này sẽ bị BỎ QUA, không thêm vào kế hoạch!"
                
                QtWidgets.QMessageBox.warning(self, "Cảnh báo - Plan code đã được load", warning_msg)
            
            if not valid_data:
                QtWidgets.QMessageBox.warning(
                    self, 
                    "Cảnh báo", 
                    f"❌ Tất cả {len(data_list)} dòng trong file đều có plan_code đã được SYSTEM LOAD trong ngày hôm nay!\n\nKhông có dữ liệu mới để import."
                )
                return
            
            # Xác nhận import
            # Nhóm theo plan_code để hiển thị
            plan_groups_preview = {}
            for ext_code, plan_code in valid_data:
                if plan_code not in plan_groups_preview:
                    plan_groups_preview[plan_code] = []
                plan_groups_preview[plan_code].append(ext_code)
            
            plan_summary = "\n".join([f"  - {plan_code}: {len(ext_codes)} mã" 
                                    for plan_code, ext_codes in plan_groups_preview.items()])
            
            reply = QtWidgets.QMessageBox.question(
                self, 
                "Xác nhận Import", 
                f"⚠️ CẢNH BÁO: Toàn bộ dữ liệu cũ trong bảng PLAN sẽ bị XÓA!\n\n"
                f"📊 Tổng số dòng trong file: {len(data_list)}\n"
                f"✅ Số dòng hợp lệ (plan_code chưa load, sẽ import): {len(valid_data)}\n"
                f"❌ Số dòng bị loại (plan_code đã load, không import): {len(invalid_data)}\n\n"
                f"📋 Chi tiết các plan_code sẽ được import:\n{plan_summary}\n\n"
                f"📝 Danh sách chi tiết (10 dòng đầu):\n"
                f"{chr(10).join([f'  - {ext} (Plan: {plan})' for ext, plan in valid_data[:10]])}"
                f"{'...' if len(valid_data) > 10 else ''}\n\n"
                f"⚠️ Các plan_code đã load sẽ bị BỎ QUA!\n\n"
                f"Bạn có chắc chắn muốn import dữ liệu mới không?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            
            if reply != QtWidgets.QMessageBox.Yes:
                return
            
            # Bắt đầu transaction
            cursor.execute('BEGIN TRANSACTION')
            
            # 1. Xóa hết dữ liệu cũ trong bảng plan
            cursor.execute('DELETE FROM plan')
            deleted_count = cursor.rowcount
            print(f"🗑️ Đã xóa {deleted_count} dòng dữ liệu cũ trong bảng plan")
            
            # Ghi vào history hành động xóa
            cursor.execute('''
                INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', ('ALL', self.validated_operator, 'CLEAR_ALL_PLAN_TABLE', 'ALL', 
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # 2. Import dữ liệu mới theo thứ tự trong file (CHỈ import các dòng hợp lệ - plan_code chưa load)
            success_count = 0
            error_count = 0
            
            for idx, (ext_code, plan_code) in enumerate(valid_data):
                try:
                    # Thêm mới vào bảng plan với sort_order theo thứ tự file
                    cursor.execute(
                        'INSERT INTO plan (ext_code, sort_order, plan_code) VALUES (?, ?, ?)', 
                        (ext_code, idx, plan_code)
                    )
                    success_count += 1
                    print(f"✅ Import thành công: {ext_code} (Plan: {plan_code}) - sort_order: {idx}")
                    
                    # Ghi vào bảng history cho từng mã
                    cursor.execute('''
                        INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (ext_code, self.validated_operator, f'IMPORT_PLAN_SORT_ORDER_{idx}', plan_code, 
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    
                except sqlite3.Error as e:
                    error_count += 1
                    print(f"❌ Lỗi khi import ExtCode '{ext_code}' cho plan '{plan_code}': {str(e)}")
                    continue
            
            # Commit transaction
            conn.commit()
            
            # Nhóm kết quả theo plan_code để hiển thị
            result_plan_groups = {}
            for ext_code, plan_code in valid_data:
                if plan_code not in result_plan_groups:
                    result_plan_groups[plan_code] = 0
                result_plan_groups[plan_code] += 1
            
            plan_result_summary = "\n".join([f"  - {plan_code}: {count} mã" 
                                            for plan_code, count in result_plan_groups.items()])
            
            # Hiển thị kết quả
            result_message = f"📊 KẾT QUẢ IMPORT:\n\n"
            result_message += f"🗑️ Đã xóa dữ liệu cũ: {deleted_count} dòng\n"
            result_message += f"📊 Tổng số dòng trong file: {len(data_list)}\n"
            result_message += f"✅ IMPORT THÀNH CÔNG: {success_count} dòng\n"
            result_message += f"❌ Lỗi: {error_count}\n"
            result_message += f"🚫 BỊ LOẠI (plan_code đã load trong ngày): {len(invalid_data)} dòng\n\n"
            result_message += f"📋 Chi tiết theo plan_code (đã import):\n{plan_result_summary}\n"
            result_message += f"🎯 Sort_order được đánh theo thứ tự trong file (0 đến {success_count-1 if success_count > 0 else 0})"
            
            QtWidgets.QMessageBox.information(self, "Kết quả Import", result_message)
            
            # Nếu có dữ liệu được import thành công, phát signal và đóng cửa sổ
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