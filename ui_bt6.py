#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program centers a window 
on the screen. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget,
     QLabel, QLineEdit, QTextEdit, QGridLayout, QLCDNumber, QSlider, 
     QMainWindow, QLineEdit, QInputDialog, QGroupBox)

class Ui_btneu6(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.createGridGroupBox()
        self.creatVboxGroupBox()

        mainLayout = QVBoxLayout()
        hboxLayout = QVBoxLayout()
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addWidget(self.vboxGroupBox)
        mainLayout.addLayout(hboxLayout)
        self.setLayout(mainLayout)
        
        #self.statusBar()
        self.resize(300, 200)
        self.center()
        self.setWindowTitle('登陆六维')
        self.show()

    def createGridGroupBox(self):

        self.gridGroupBox = QGroupBox("输入")
        layout = QGridLayout()

        title = QLabel('用户名')
        author = QLabel('密码')
        review = QLabel('搜索关键词')
        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.authorEdit.setEchoMode(QLineEdit.Password)
        self.reviewEdit = QLineEdit()

        layout.setSpacing(10)

        layout.addWidget(title, 1, 0)
        layout.addWidget(self.titleEdit, 1, 1)

        layout.addWidget(author, 2, 0)
        layout.addWidget(self.authorEdit, 2, 1)

        layout.addWidget(review, 3, 0)
        layout.addWidget(self.reviewEdit, 3, 1)

        self.gridGroupBox.setLayout(layout)

    def creatVboxGroupBox(self):

        self.vboxGroupBox = QGroupBox("功能")
        layout = QHBoxLayout()

        okButton = QPushButton("登陆")
        cancelButton = QPushButton("搜索")

        okButton.clicked.connect(self.login_button)
        cancelButton.clicked.connect(self.search_button)

        #layout.addStretch(20)
        layout.addWidget(okButton)
        layout.addWidget(cancelButton)

        vbox_layout = QVBoxLayout()
        vbox_layout.addStretch(1)
        vbox_layout.addLayout(layout)

        self.vboxGroupBox.setLayout(vbox_layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()

    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))

    def login_button(self):
        username = self.titleEdit.text()
        password = self.authorEdit.text()
        return (username,password)

    def search_button(self):
        keyword = self.reviewEdit.text()
        return (keyword)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Ui_btneu6() 
    sys.exit(app.exec_())