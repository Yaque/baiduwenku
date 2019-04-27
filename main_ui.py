from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMessageBox
import os

from main_thread import MyWorkThread



class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 360)
        MainWindow.setWindowIcon(QIcon('icon.png'))
        MainWindow.setStyleSheet("background-image:url(background.jpg)")
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 200, 50))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(100,100,100,120);}")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 200, 50))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 180, 200, 50))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 80, 50))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:12px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(100,100,100,120);}")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 80, 50))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:12px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(100,100,100,120);}")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 80, 50))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:12px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(100,100,100,120);}")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 260, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,255,255)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 260, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,255,255)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")

        self.label_show = QtWidgets.QLabel(self.centralWidget)
        self.label_show.setGeometry(QtCore.QRect(380, 40, 450, 280))
        self.label_show.setTextFormat(QtCore.Qt.AutoText)
        self.label_show.setObjectName("label_show")
        self.label_show.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:12px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(100,100,100,120);}")

        self.work_thread = MyWorkThread()
        self.work_thread.trigger.connect(self.show_data)

        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "百度文库下载系统"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入搜索关键字"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "其输入保存文件夹名"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "请输入要下载文件的个数，最多600"))
        self.label.setText(_translate("MainWindow", "搜索关键字"))
        self.label_2.setText(_translate("MainWindow", "保存文件夹名"))
        self.label_3.setText(_translate("MainWindow", "下载个数"))
        self.label_show.setText(_translate("MainWindow", "下载尚未开始"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))

    def show_data(self, str_data):
        d = str_data.split("+:+")
        if d[0] == "plsay":
            self.pushButton.setEnabled(True)
            self.label_show.setText("下载完成！请前往文件夹查看")
        else:
            self.label_show.setText(d[1] + "\n" + d[0] + "\n已下载完成\n" + d[2])

    def word_get(self):
        self.pushButton.setEnabled(False)
        search_key = (str)(self.lineEdit.text())
        path_name = (str)(self.lineEdit_2.text())
        number = 0
        try:
            number = (int)(self.lineEdit_3.text())
        except:
            QMessageBox.warning(self,
                                "警告",
                                "出现错误！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()
            self.pushButton.setEnabled(True)

        if search_key == '' or path_name == '':
            QMessageBox.warning(self,
                                "警告",
                                "搜索关键字为空！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()
            self.pushButton.setEnabled(True)
        else:
            try:
                os.mkdir(path_name)
            except:
                pass
            print("ok")
            self.work_thread.set_paramter(search_key, path_name, number)
            self.work_thread.start()

