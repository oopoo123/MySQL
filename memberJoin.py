#회원가입 프로그램

import  sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("ui/login.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입프로그램")

        self.check_btn.clicked.connect(self.idCheck)
        self.join_btn.clicked.connect(self.join)
        self.loginid_btn.clicked.connect(self.login)
        self.reset_btn.clicked.connect(self.reset)

    def idCheck(self):
        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()

        if result == None: # 회원가입가능
            QMessageBox.warning(self, '가입가능', '입력하신 아이디는 가입 가능한 아이디입니다. 계속해서 가입 진행하세요')
        else:
            QMessageBox.warning(self, '가입불가', '입력하신 아이디는 이미 존재하는 아이디입니다. 다른아이디를 입력하세요')

        cur.close()
        conn.close()

    def join(self):
        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기

        memberid = self.memberid_edit.text()
        memberpw = self.memberpw_edit.text()
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        address = self.address_edit.text()
        age = self.age_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"INSERT INTO member VALUES ('{memberid}', '{memberpw}', '{name}', '{phone}', '{address}', {age})"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        cur.close()
        conn.commit()
        conn.close()


    def login(self):
        loginid = self.loginid_edit.text()
        loginpw = self.logpw_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid='{loginid}' and memberpw='{loginpw}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()

        if result == None:
            self.loginid_text.setText('로그인 실패!!!')
        else:
            self.loginid_text.setText('로그인 성공!!!')

        cur.close()
        conn.close()


    def reset(self):
        self.memberid_edit.clear()
        self.memberpw_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.address_edit.clear()
        self.age_edit.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())