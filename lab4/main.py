import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox,QColorDialog,QMainWindow)
import labgui  # Это наш конвертированный файл дизайна
from PyQt5.QtGui import QIcon,QFont,QColor
import time

class ExampleApp(QtWidgets.QMainWindow, labgui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        btn=self.Button
        btn.clicked.connect(self.checker)


    def checker(self):
        from_system=int(self.Input_1.text())
        system=int(self.Input_2.text())
        number=str(self.Num.text())
        try:
            if from_system>=2 and from_system<=16:
                pass
            else:
                msg=QMessageBox()
                msg.setText("Неверно введена СС.")
                msg.exec_()
                self.Input_1.clear()
                self.Input_2.clear()
                self.Num.clear()
        except:
            msg=QMessageBox()
            msg.setText("Неверно введена СС.")
            msg.exec_()
            self.Input_1.clear()
            self.Input_2.clear()
            self.Num.clear()
        try:
            if system>=2 and system<=16:
                pass
            else:
                msg=QMessageBox()
                msg.setText("Неверно введена СС.")
                msg.exec_()
                self.Input_1.clear()
                self.Input_2.clear()
                self.Num.clear()
        except:
            msg=QMessageBox()
            msg.setText("Неверно введена СС.")
            msg.exec_()
            self.Input_1.clear()
            self.Input_2.clear()
            self.Num.clear()
        self.convertor(number,system,from_system)


    def convertor(self,num, to_base=10, from_base=10):
        res=self.result
        try:
            if isinstance(num, str):
                n = int(num, from_base)
            else:
                n = int(num)
            alphabet = "0123456789ABCDEF"
            if n < to_base:
                return res.setText(alphabet[n])
            else:
                return res.setText(self.convertor(n // to_base, to_base) + alphabet[n % to_base])
        except(ValueError):
            msg=QMessageBox()
            msg.setText("Неверно введено число.")
            msg.exec_()
            self.Input_1.clear()
            self.Input_2.clear()
            return(self.Num.clear())


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы действительно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__== '__main__':
	main()