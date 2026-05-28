from PyQt5.QtWidgets import QApplication, QListWidget
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

list_widget = QListWidget()

# Cho phép kéo thả đổi vị trí
list_widget.setDragDropMode(QListWidget.InternalMove)

list_widget.addItems([
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
])

list_widget.resize(300, 200)
list_widget.show()

sys.exit(app.exec_())