import sys, os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import warnings
from datetime import datetime

warnings.filterwarnings('ignore', category=DeprecationWarning)

def get_resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối đến resource (icon, image, etc.)"""
    if getattr(sys, 'frozen', False):  
        base_path = os.path.dirname(sys.executable)  # Lấy thư mục chứa file .exe
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 530, 1901, 141))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 40, 581, 71))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 121, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.Length = QtWidgets.QLineEdit(self.widget)
        self.Length.setGeometry(QtCore.QRect(120, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Length.setFont(font)
        self.Length.setAutoFillBackground(False)
        self.Length.setReadOnly(True)
        self.Length.setObjectName("Length")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(460, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setGeometry(QtCore.QRect(640, 40, 581, 71))
        self.widget_2.setObjectName("widget_2")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 151, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.Height = QtWidgets.QLineEdit(self.widget_2)
        self.Height.setGeometry(QtCore.QRect(150, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Height.setFont(font)
        self.Height.setAutoFillBackground(False)
        self.Height.setReadOnly(True)
        self.Height.setObjectName("Height")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(480, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setGeometry(QtCore.QRect(1270, 40, 581, 71))
        self.widget_3.setObjectName("widget_3")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 151, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.Weight = QtWidgets.QLineEdit(self.widget_3)
        self.Weight.setGeometry(QtCore.QRect(160, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Weight.setFont(font)
        self.Weight.setAutoFillBackground(False)
        self.Weight.setReadOnly(True)
        self.Weight.setObjectName("Weight")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(490, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 1901, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_4.setGeometry(QtCore.QRect(30, 40, 891, 71))
        self.widget_4.setObjectName("widget_4")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 251, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.UpperScrew = QtWidgets.QLineEdit(self.widget_4)
        self.UpperScrew.setGeometry(QtCore.QRect(250, 10, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.UpperScrew.setFont(font)
        self.UpperScrew.setAutoFillBackground(False)
        self.UpperScrew.setReadOnly(True)
        self.UpperScrew.setObjectName("UpperScrew")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setGeometry(QtCore.QRect(750, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_5.setGeometry(QtCore.QRect(30, 140, 891, 71))
        self.widget_5.setObjectName("widget_5")
        self.label_14 = QtWidgets.QLabel(self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 251, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.LowerScrew = QtWidgets.QLineEdit(self.widget_5)
        self.LowerScrew.setGeometry(QtCore.QRect(250, 10, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LowerScrew.setFont(font)
        self.LowerScrew.setAutoFillBackground(False)
        self.LowerScrew.setReadOnly(True)
        self.LowerScrew.setObjectName("LowerScrew")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(750, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.widget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_6.setGeometry(QtCore.QRect(990, 40, 871, 71))
        self.widget_6.setObjectName("widget_6")
        self.label_19 = QtWidgets.QLabel(self.widget_6)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 251, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.RollSpeed = QtWidgets.QLineEdit(self.widget_6)
        self.RollSpeed.setGeometry(QtCore.QRect(250, 10, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RollSpeed.setFont(font)
        self.RollSpeed.setAutoFillBackground(False)
        self.RollSpeed.setReadOnly(True)
        self.RollSpeed.setObjectName("RollSpeed")
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setGeometry(QtCore.QRect(760, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.widget_10 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_10.setGeometry(QtCore.QRect(990, 140, 871, 71))
        self.widget_10.setObjectName("widget_10")
        self.label_21 = QtWidgets.QLabel(self.widget_10)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 251, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.TUCSpeed = QtWidgets.QLineEdit(self.widget_10)
        self.TUCSpeed.setGeometry(QtCore.QRect(250, 10, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TUCSpeed.setFont(font)
        self.TUCSpeed.setAutoFillBackground(False)
        self.TUCSpeed.setReadOnly(True)
        self.TUCSpeed.setObjectName("TUCSpeed")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 690, 1901, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget_7 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_7.setGeometry(QtCore.QRect(80, 20, 221, 131))
        self.widget_7.setObjectName("widget_7")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.ConveyoRoller = QtWidgets.QLineEdit(self.widget_7)
        self.ConveyoRoller.setGeometry(QtCore.QRect(10, 60, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConveyoRoller.setFont(font)
        self.ConveyoRoller.setAutoFillBackground(False)
        self.ConveyoRoller.setReadOnly(True)
        self.ConveyoRoller.setObjectName("ConveyoRoller")
        self.widget_8 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_8.setGeometry(QtCore.QRect(450, 20, 201, 131))
        self.widget_8.setObjectName("widget_8")
        self.label_15 = QtWidgets.QLabel(self.widget_8)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.ConveyorSlope = QtWidgets.QLineEdit(self.widget_8)
        self.ConveyorSlope.setGeometry(QtCore.QRect(10, 60, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConveyorSlope.setFont(font)
        self.ConveyorSlope.setAutoFillBackground(False)
        self.ConveyorSlope.setReadOnly(True)
        self.ConveyorSlope.setObjectName("ConveyorSlope")
        self.widget_9 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_9.setGeometry(QtCore.QRect(790, 20, 271, 131))
        self.widget_9.setObjectName("widget_9")
        self.label_20 = QtWidgets.QLabel(self.widget_9)
        self.label_20.setGeometry(QtCore.QRect(10, 0, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.ConveyorRollerBelts = QtWidgets.QLineEdit(self.widget_9)
        self.ConveyorRollerBelts.setGeometry(QtCore.QRect(30, 60, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConveyorRollerBelts.setFont(font)
        self.ConveyorRollerBelts.setAutoFillBackground(False)
        self.ConveyorRollerBelts.setReadOnly(True)
        self.ConveyorRollerBelts.setObjectName("ConveyorRollerBelts")
        self.widget_11 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_11.setGeometry(QtCore.QRect(1170, 20, 231, 131))
        self.widget_11.setObjectName("widget_11")
        self.label_22 = QtWidgets.QLabel(self.widget_11)
        self.label_22.setGeometry(QtCore.QRect(10, 0, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.ConveyorCoolingBelt = QtWidgets.QLineEdit(self.widget_11)
        self.ConveyorCoolingBelt.setGeometry(QtCore.QRect(20, 60, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConveyorCoolingBelt.setFont(font)
        self.ConveyorCoolingBelt.setAutoFillBackground(False)
        self.ConveyorCoolingBelt.setReadOnly(True)
        self.ConveyorCoolingBelt.setObjectName("ConveyorCoolingBelt")
        self.widget_13 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_13.setGeometry(QtCore.QRect(1560, 20, 221, 131))
        self.widget_13.setObjectName("widget_13")
        self.label_26 = QtWidgets.QLabel(self.widget_13)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.TUCRoller = QtWidgets.QLineEdit(self.widget_13)
        self.TUCRoller.setGeometry(QtCore.QRect(10, 60, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TUCRoller.setFont(font)
        self.TUCRoller.setAutoFillBackground(False)
        self.TUCRoller.setReadOnly(True)
        self.TUCRoller.setObjectName("TUCRoller")
        self.widget_12 = QtWidgets.QWidget(self.centralwidget)
        self.widget_12.setGeometry(QtCore.QRect(490, 20, 891, 161))
        self.widget_12.setObjectName("widget_12")
        self.label_23 = QtWidgets.QLabel(self.widget_12)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 141, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.ExtCode = QtWidgets.QLineEdit(self.widget_12)
        self.ExtCode.setGeometry(QtCore.QRect(140, 10, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ExtCode.setFont(font)
        self.ExtCode.setAutoFillBackground(False)
        self.ExtCode.setText("")
        self.ExtCode.setReadOnly(True)
        self.ExtCode.setObjectName("ExtCode")
        self.LoadDataToPLC = QtWidgets.QPushButton(self.widget_12)
        self.LoadDataToPLC.setGeometry(QtCore.QRect(630, 15, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LoadDataToPLC.setFont(font)
        self.LoadDataToPLC.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadDataToPLC.setStyleSheet("QPushButton {\n"
"    background-color: #0d6efd;\n"
"    color: white;\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-size: 12pt;\n"
"    font-weight: 600;\n"
"\n"
"    padding: 6px 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3385ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0b5ed7;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/cabinet.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.LoadDataToPLC.setIcon(icon)
        self.LoadDataToPLC.setIconSize(QtCore.QSize(32, 32))
        self.LoadDataToPLC.setObjectName("LoadDataToPLC")
        self.label_24 = QtWidgets.QLabel(self.widget_12)
        self.label_24.setGeometry(QtCore.QRect(0, 90, 141, 78))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.TireName = QtWidgets.QLineEdit(self.widget_12)
        self.TireName.setGeometry(QtCore.QRect(140, 100, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TireName.setFont(font)
        self.TireName.setAutoFillBackground(False)
        self.TireName.setReadOnly(True)
        self.TireName.setObjectName("TireName")
        self.label_23.raise_()
        self.LoadDataToPLC.raise_()
        self.label_24.raise_()
        self.TireName.raise_()
        self.ExtCode.raise_()
        self.CloseApp = QtWidgets.QPushButton(self.centralwidget)
        self.CloseApp.setGeometry(QtCore.QRect(1680, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CloseApp.setFont(font)
        self.CloseApp.setStyleSheet("QPushButton {\n"
"    background-color: #ff6b6b;\n"
"    color: white;\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"\n"
"    padding: 3px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #dc3545;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b02a37;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.CloseApp.setIcon(icon1)
        self.CloseApp.setIconSize(QtCore.QSize(32, 32))
        self.CloseApp.setObjectName("CloseApp")
        self.ImportPlan = QtWidgets.QPushButton(self.centralwidget)
        self.ImportPlan.setGeometry(QtCore.QRect(1680, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ImportPlan.setFont(font)
        self.ImportPlan.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ImportPlan.setIcon(icon2)
        self.ImportPlan.setIconSize(QtCore.QSize(32, 32))
        self.ImportPlan.setObjectName("ImportPlan")
        self.ChangePlan = QtWidgets.QPushButton(self.centralwidget)
        self.ChangePlan.setGeometry(QtCore.QRect(1680, 150, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ChangePlan.setFont(font)
        self.ChangePlan.setStyleSheet("QPushButton {\n"
"    background-color: #ffc107;\n"
"    color: black;\n"
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
"    background-color: #ffcd39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d39e00;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/video-editing.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("C:/Users/dan.it/.designer/backup/images/video-editing.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.ChangePlan.setIcon(icon3)
        self.ChangePlan.setIconSize(QtCore.QSize(32, 32))
        self.ChangePlan.setObjectName("ChangePlan")
        self.HistoryAndPlan = QtWidgets.QPushButton(self.centralwidget)
        self.HistoryAndPlan.setGeometry(QtCore.QRect(1680, 220, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.HistoryAndPlan.setFont(font)
        self.HistoryAndPlan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HistoryAndPlan.setStyleSheet("QPushButton {\n"
"    background-color: #6c757d;\n"
"    color: white;\n"
"\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"    font-size: 12pt;\n"
"    font-weight: 600;\n"
"\n"
"    padding: 6px 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7c848b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5c636a;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/project.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.HistoryAndPlan.setIcon(icon4)
        self.HistoryAndPlan.setIconSize(QtCore.QSize(32, 32))
        self.HistoryAndPlan.setObjectName("HistoryAndPlan")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Extruder Program"))
        self.groupBox.setTitle(_translate("MainWindow", "Kích thước, Trọng Lượng"))
        self.label_4.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Chiều Dài\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Length\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">mm</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Chiều Rộng\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Height\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">mm</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Trọng Lượng\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Weight\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">g/pcs</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tốc Độ"))
        self.label_6.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Đỉnh Extruder Tốc Độ\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Upper Screw\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">RPM</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Đáy Extruder Tốc Độ\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Lower Screw\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">RPM</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Con lăn đầu tiên\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"1st roller speet set\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-style:italic;\">m/min</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Tốc Độ Máy Roll\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Roll TUC Speed\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Độ Căng"))
        self.label_7.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Con Lăn Băng Tải\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Conveyor Rollers\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_15.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Sườn Dốc Băng Tải\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Conveyor Slope\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_20.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Đai Băng Tải Trên Con Lăn\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Roller Conveyor Belts\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_22.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"So 1 Băng Tải Làm Mát\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"No. 1 Cooling Conveyor Belt\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_26.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"TUC Con Lăn\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"TUC Roller\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.label_23.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Mẫ Ép Suất\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Extruder Code\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.ExtCode.setPlaceholderText(_translate("MainWindow", "Nhập mã Ép Suất"))
        self.LoadDataToPLC.setText(_translate("MainWindow", "Nạp Dữ Liệu Vào PLC\n"
"Push Data To PLC"))
        self.label_24.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"Mã Lốp\n"
"</p>\n"
"\n"
"<p style=\"margin:0px; line-height:100%;\">\n"
"<span style=\"font-size:11pt; font-style:italic;\">\n"
"Tire Code\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.CloseApp.setText(_translate("MainWindow", "Đóng Ứng Dụng\n"
"Close Application"))
        self.ImportPlan.setText(_translate("MainWindow", "Nhập Kế Hoạch\n"
"Import Plan"))
        self.ChangePlan.setText(_translate("MainWindow", "Thay Đổi Kế Hoạch\n"
"Change Plan"))
        self.HistoryAndPlan.setText(_translate("MainWindow", "Lịch Sử, Kế Hoạch\n"
"History, Plan"))

    def open_import_plan(self):
        from ImportPlan import ImportPlanWindow
        self.import_plan_window = ImportPlanWindow()
        # Kết nối signal để reload dữ liệu khi import xong
        self.import_plan_window.plan_imported.connect(self.on_plan_changed)
        self.import_plan_window.show()

    def open_change_plan(self):
        from ChangePlan import ChangePlanWindow
        self.change_plan_window = ChangePlanWindow()
        # Kết nối signal để reload dữ liệu khi plan thay đổi
        self.change_plan_window.plan_changed.connect(self.on_plan_changed)
        self.change_plan_window.show()

    def on_plan_changed(self):
        """Xử lý khi plan thay đổi từ ChangePlan"""
        print("Plan đã thay đổi, đang reload dữ liệu...")
        self.load_first_plan()
    
    def open_history_and_plan(self):
        from HistoryAndPlan import Ui_HistoryPlan
        self.history_and_plan_window = Ui_HistoryPlan()
        self.history_and_plan_window.show()

    # Hàm tiện ích để format số, nếu là float mà có phần thập phân là .0 thì chỉ hiển thị phần nguyên
    def format_number(self, value):
        if value is None:
            return ""
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)
    # Hàm để load dữ liệu spec theo ext_code
    def load_spec_data(self, ext_code):
        """Load dữ liệu từ bảng spec theo ext_code"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT tire_name, length, height, weight, 
                    upper_screw_speed, lower_screw_speed, 
                    roller_speed_1st, roll_tuc_speed,
                    conveyor_roller, conveyor_slope, 
                    roller_conveyor_belt, cooling_conveyor_belt, tuc_roller
                FROM spec WHERE ext_code = ?
            ''', (ext_code,))
            
            result = cursor.fetchone()
            
            if result:
                (tire_name, length, height, weight, 
                upper_screw, lower_screw, roll_speed, tuc_speed,
                conveyor_roller, conveyor_slope, roller_belt, cooling_belt, tuc_roller) = result
                
                # Gán dữ liệu vào các trường
                self.TireName.setText(str(tire_name) if tire_name else "")
                self.Length.setText(self.format_number(length))
                self.Height.setText(self.format_number(height))
                self.Weight.setText(self.format_number(weight))
                self.UpperScrew.setText(self.format_number(upper_screw))
                self.LowerScrew.setText(self.format_number(lower_screw))
                self.RollSpeed.setText(self.format_number(roll_speed))
                self.TUCSpeed.setText(self.format_number(tuc_speed))
                self.ConveyoRoller.setText(self.format_number(conveyor_roller))
                self.ConveyorSlope.setText(self.format_number(conveyor_slope))
                self.ConveyorRollerBelts.setText(self.format_number(roller_belt))
                self.ConveyorCoolingBelt.setText(self.format_number(cooling_belt))
                self.TUCRoller.setText(self.format_number(tuc_roller))
            else:
                # Không tìm thấy spec, clear các field
                self.clear_all_fields()
                QtWidgets.QMessageBox.warning(
                    None, 
                    "Cảnh báo", 
                    f"Không tìm thấy thông số cho mã {ext_code} trong database!"
                )
                
        except sqlite3.Error as e:
            print(f"Lỗi database: {str(e)}")
        finally:
            if conn:
                conn.close()
    
    def clear_all_fields(self):
        """Xóa tất cả các trường dữ liệu"""
        self.TireName.clear()
        self.Length.clear()
        self.Height.clear()
        self.Weight.clear()
        self.UpperScrew.clear()
        self.LowerScrew.clear()
        self.RollSpeed.clear()
        self.TUCSpeed.clear()
        self.ConveyoRoller.clear()
        self.ConveyorSlope.clear()
        self.ConveyorRollerBelts.clear()
        self.ConveyorCoolingBelt.clear()
        self.TUCRoller.clear()
    
    def load_first_plan(self):
        """Load item đầu tiên (sort_order bé nhất) từ bảng plan"""
        conn = None
        try:
            conn = sqlite3.connect('extruder.sqlite')
            cursor = conn.cursor()
            
            # Lấy ext_code, id, sort_order và plan_code của item đầu tiên
            cursor.execute('''
                SELECT ext_code, id, sort_order, plan_code FROM plan 
                ORDER BY sort_order, id 
                LIMIT 1
            ''')
            result = cursor.fetchone()
            
            if result:
                ext_code, plan_id, sort_order, plan_code = result
                self.ExtCode.setText(ext_code)
                # Lưu lại plan_id, sort_order và plan_code để xóa sau
                self.current_plan_id = plan_id
                self.current_sort_order = sort_order
                self.current_plan_code = plan_code  # Lưu plan_code
                # Load spec data
                self.load_spec_data(ext_code)
                
                # Hiển thị plan_code lên title hoặc status bar (nếu có)
                print(f"Đang load: ExtCode={ext_code}, PlanCode={plan_code}, SortOrder={sort_order}")
            else:
                # Không có dữ liệu trong plan
                self.ExtCode.setText("")
                self.clear_all_fields()
                self.current_plan_id = None
                self.current_sort_order = None
                self.current_plan_code = None  # Reset plan_code
                print("Không có dữ liệu kế hoạch")
                
        except sqlite3.Error as e:
            print(f"Lỗi database: {str(e)}")
        finally:
            if conn:
                conn.close()

    def load_to_plc(self):
        """Xử lý khi nhấn nút LoadDataToPLC"""
        current_ext_code = self.ExtCode.text().strip()
        
        if not current_ext_code:
            QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Không có mã kế hoạch để load!")
            return
        
        if not hasattr(self, 'current_plan_id') or self.current_plan_id is None:
            QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Không tìm thấy ID kế hoạch!")
            return
        
        # Lấy plan_code hiện tại
        current_plan_code = getattr(self, 'current_plan_code', None)
        
        # Xác nhận load
        confirm_msg = f"Bạn có chắc chắn muốn load chương trình cho mã:\n{current_ext_code}\n"
        confirm_msg += f"ID: {self.current_plan_id} | Sort Order: {self.current_sort_order}"
        if current_plan_code:
            confirm_msg += f" | Plan Code: {current_plan_code}"
        
        reply = QtWidgets.QMessageBox.question(
            None,
            "Xác nhận",
            confirm_msg,
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
            
            # Xóa item hiện tại bằng ID (chính xác tuyệt đối)
            cursor.execute('DELETE FROM plan WHERE id = ?', (self.current_plan_id,))
            deleted_count = cursor.rowcount
            print(f"Đã xóa {deleted_count} dòng: ID={self.current_plan_id}, ExtCode={current_ext_code}, PlanCode={current_plan_code}")
            
            # Ghi vào history với plan_code
            cursor.execute('''
                INSERT INTO history (ext_code, operator_code, action, plan_code, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (current_ext_code, 'SYSTEM', 
                f'LOAD_THE_PROGRAM_ID_{self.current_plan_id}_SORT_ORDER_{self.current_sort_order}', 
                current_plan_code,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # Commit transaction
            conn.commit()
            
            # Hiển thị thông báo thành công
            success_msg = f"Đã load chương trình cho mã:\n{current_ext_code}\n\nĐã xóa khỏi danh sách kế hoạch!"
            if current_plan_code:
                success_msg += f"\nPlan Code: {current_plan_code}"
            
            QtWidgets.QMessageBox.information(
                None,
                "Thành công",
                success_msg
            )
            
            # Load item tiếp theo
            self.load_first_plan()
            
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            QtWidgets.QMessageBox.critical(None, "Lỗi Database", f"Lỗi khi load chương trình:\n{str(e)}")
        finally:
            if conn:
                conn.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # Load plan đầu tiên khi khởi động
    ui.load_first_plan()
    
    # Connect the close button
    ui.CloseApp.clicked.connect(MainWindow.close)
    
    # Connect the Import Plan button
    ui.ImportPlan.clicked.connect(ui.open_import_plan)
    
    # Connect the Change Plan button
    ui.ChangePlan.clicked.connect(ui.open_change_plan)
    
    # Connect the Load Data To PLC button
    ui.LoadDataToPLC.clicked.connect(ui.load_to_plc)
    
    # Connect the History and Plan button
    ui.HistoryAndPlan.clicked.connect(ui.open_history_and_plan)
    # Fullscreen kiosk
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    
    sys.exit(app.exec_())