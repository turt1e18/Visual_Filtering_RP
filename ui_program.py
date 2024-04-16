# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QSlider, QPushButton, QApplication, QVBoxLayout, QLabel, QFrame, QWidget, QDialogButtonBox
from PyQt5.QtCore import Qt, QObject, QEvent

class EventFilter(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Up:
                # 위쪽 화살표 키를 눌렀을 때 이전 슬라이더를 포커싱
                if obj == self.ui.blue_slider:
                    self.ui.red_slider.setFocus()
                elif obj == self.ui.green_slider:
                    self.ui.blue_slider.setFocus()
                return True
            elif event.key() == Qt.Key_Down:
                # 아래쪽 화살표 키를 눌렀을 때 다음 슬라이더를 포커싱
                if obj == self.ui.red_slider:
                    self.ui.blue_slider.setFocus()
                elif obj == self.ui.blue_slider:
                    self.ui.green_slider.setFocus()
                elif obj == self.ui.green_slider and event.key() == Qt.Key_Down:
                    self.ui.save_preset_button1.setFocus()
                return True
            elif event.key() == Qt.Key_Left:
            # 좌측 화살표 키를 눌렀을 때 슬라이더 값을 감소시킴
                if obj == self.ui.red_slider:
                    self.ui.red_slider.setValue(self.ui.red_slider.value() - 1)
                elif obj == self.ui.blue_slider:
                    self.ui.blue_slider.setValue(self.ui.blue_slider.value() - 1)
                elif obj == self.ui.green_slider:
                    self.ui.green_slider.setValue(self.ui.green_slider.value() - 1)
                return True
            elif event.key() == Qt.Key_Right:
                # 우측 화살표 키를 눌렀을 때 슬라이더 값을 증가시킴
                if obj == self.ui.red_slider:
                    self.ui.red_slider.setValue(self.ui.red_slider.value() + 1)
                elif obj == self.ui.blue_slider:
                    self.ui.blue_slider.setValue(self.ui.blue_slider.value() + 1)
                elif obj == self.ui.green_slider:
                    self.ui.green_slider.setValue(self.ui.green_slider.value() + 1)
                return True
        return False

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1195, 581)
        
        # 박스 하단의 확인 버튼 구현부
        self.bottom_box = QtWidgets.QDialogButtonBox(Dialog)
        self.bottom_box.setGeometry(QtCore.QRect(260, 510, 341, 32))
        self.bottom_box.setOrientation(QtCore.Qt.Horizontal)
        self.bottom_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.bottom_box.setObjectName("bottom_box")
        
        # 적색 슬라이더 구현부
        self.red_slider = QtWidgets.QSlider(Dialog)
        self.red_slider.setGeometry(QtCore.QRect(60, 120, 501, 51))
        self.red_slider.setMaximum(100)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setObjectName("red_slider")
        # 적색 슬라이더 값을 표시하는 코드
        self.red_slider.valueChanged.connect(self.update_red_value_ui)

        # 청색 슬라이더 구현부
        self.blue_slider = QtWidgets.QSlider(Dialog)
        self.blue_slider.setGeometry(QtCore.QRect(60, 260, 501, 51))
        self.blue_slider.setMaximum(100)
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blue_slider")
        # 청색 슬라이더 값을 표시하는 코드
        self.blue_slider.valueChanged.connect(self.update_blue_value_ui)
        
        # 녹색 슬라이더 구현부
        self.green_slider = QtWidgets.QSlider(Dialog)
        self.green_slider.setGeometry(QtCore.QRect(60, 400, 501, 51))
        self.green_slider.setMaximum(100)
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("green_slider")
        #녹색 슬라이더 값을 표시하는 코드
        self.green_slider.valueChanged.connect(self.update_green_value_ui)
        
        # 좌우측 나누는 중간의 선
        self.div_line = QtWidgets.QFrame(Dialog)
        self.div_line.setGeometry(QtCore.QRect(610, 30, 16, 521))
        self.div_line.setLineWidth(3)
        self.div_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.div_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.div_line.setObjectName("div_line")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(650, 40, 500, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # 우측 화면의 그림 구현부
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        self.label.setStyleSheet("border-radius: 10px;")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("../서류/둘기.gif"))
        self.label.setObjectName("label")
        
        self.verticalLayout.addWidget(self.label)
        
        # 현재 슬라이드 값 표시 TEXT
        self.red_value_level = QtWidgets.QLabel(Dialog)
        self.red_value_level.setGeometry(QtCore.QRect(490, 100, 68, 15))
        self.red_value_level.setObjectName("red_value_level")
        self.red_value_level.setStyleSheet("font-size: 20px; font-weight:bold;")

        self.blue_value_level = QtWidgets.QLabel(Dialog)
        self.blue_value_level.setGeometry(QtCore.QRect(490, 240, 68, 15))
        self.blue_value_level.setObjectName("blue_value_level")
        self.blue_value_level.setStyleSheet("font-size: 20px; font-weight:bold;")
        
        self.green_value_level = QtWidgets.QLabel(Dialog)
        self.green_value_level.setGeometry(QtCore.QRect(490, 370, 68, 15))
        self.green_value_level.setObjectName("green_value_level")
        self.green_value_level.setStyleSheet("font-size: 20px; font-weight:bold;")

        # 슬라이드 좌측 상단의 소개 TEXT
        self.red_text = QtWidgets.QLabel(Dialog)
        self.red_text.setGeometry(QtCore.QRect(60, 74, 100, 31))
        self.red_text.setObjectName("red_text")
        self.red_text.setStyleSheet("font-size: 20px; font-weight:bold;")
        
        self.blue_text = QtWidgets.QLabel(Dialog)
        self.blue_text.setGeometry(QtCore.QRect(60, 215, 100, 31))
        self.blue_text.setObjectName("blue_text")
        self.blue_text.setStyleSheet("font-size: 20px; font-weight:bold;")
        
        self.green_text = QtWidgets.QLabel(Dialog)
        self.green_text.setGeometry(QtCore.QRect(60, 360, 140, 31))
        self.green_text.setObjectName("green_text")
        self.green_text.setStyleSheet("font-size: 20px; font-weight:bold;")

        # 아래는 하단 버튼 부분(데이터 저장 및 불러오기) 구현부
        # 저장용 버튼 3개
        self.save_preset_button1 = QtWidgets.QPushButton(Dialog)
        self.save_preset_button1.setGeometry(QtCore.QRect(100, 480, 100, 30))
        self.save_preset_button1.setText("Save Preset 1")
        self.save_preset_button1.clicked.connect(self.save_preset1)

        self.save_preset_button2 = QtWidgets.QPushButton(Dialog)
        self.save_preset_button2.setGeometry(QtCore.QRect(220, 480, 100, 30))
        self.save_preset_button2.setText("Save Preset 2")
        self.save_preset_button2.clicked.connect(self.save_preset2)

        self.save_preset_button3 = QtWidgets.QPushButton(Dialog)
        self.save_preset_button3.setGeometry(QtCore.QRect(340, 480, 100, 30))
        self.save_preset_button3.setText("Save Preset 3")
        self.save_preset_button3.clicked.connect(self.save_preset3)

        # 불러오기용 버튼 3개
        self.load_preset_button1 = QtWidgets.QPushButton(Dialog)
        self.load_preset_button1.setGeometry(QtCore.QRect(100, 520, 100, 30))
        self.load_preset_button1.setText("Load Preset 1")
        self.load_preset_button1.clicked.connect(self.load_preset1)

        self.load_preset_button2 = QtWidgets.QPushButton(Dialog)
        self.load_preset_button2.setGeometry(QtCore.QRect(220, 520, 100, 30))
        self.load_preset_button2.setText("Load Preset 2")
        self.load_preset_button2.clicked.connect(self.load_preset2)

        self.load_preset_button3 = QtWidgets.QPushButton(Dialog)
        self.load_preset_button3.setGeometry(QtCore.QRect(340, 520, 100, 30))
        self.load_preset_button3.setText("Load Preset 3")
        self.load_preset_button3.clicked.connect(self.load_preset3)
        
        # 슬라이더의 포커스 이동 활성화
        self.red_slider.setFocusPolicy(Qt.StrongFocus)
        self.blue_slider.setFocusPolicy(Qt.StrongFocus)
        self.green_slider.setFocusPolicy(Qt.StrongFocus)

        # 이벤트 필터 생성
        self.event_filter = EventFilter(self)
        
        # 슬라이더 바에 이벤트 필터 설정
        self.red_slider.installEventFilter(self.event_filter)
        self.blue_slider.installEventFilter(self.event_filter)
        self.green_slider.installEventFilter(self.event_filter)

        # 현재 선택된 슬라이더 초기화
        self.current_slider = None

        # UI 완료 코드
        self.retranslateUi(Dialog)
        self.bottom_box.accepted.connect(Dialog.accept) # type: ignore
        self.bottom_box.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

   
    # 프리셋 1에 슬라이더 값 저장하는 함수
    def save_preset1(self):
        red_value = self.red_slider.value()
        blue_value = self.blue_slider.value()
        green_value = self.green_slider.value()

        # JSON 형식으로 저장
        preset_data = {
            "red_value": red_value,
            "blue_value": blue_value,
            "green_value": green_value
        }

        #프로그램이 실행되는 디렉토리 path에 저장
        current_dir = os.path.dirname(os.path.realpath(__file__))
        preset_file = os.path.join(current_dir, "preset1.json")
        try:
            with open("preset1.json", "w") as f:
                json.dump(preset_data, f)
        except IOError:
            QMessageBox.critical(None, "Error", "Failed to save Preset 1")

    # 프리셋 2에 슬라이더 값 저장하는 함수
    def save_preset2(self):
        red_value = self.red_slider.value()
        blue_value = self.blue_slider.value()
        green_value = self.green_slider.value()

        # JSON 형식으로 저장
        preset_data = {
            "red_value": red_value,
            "blue_value": blue_value,
            "green_value": green_value
        }
        
        current_dir = os.path.dirname(os.path.realpath(__file__))
        preset_file = os.path.join(current_dir, "preset2.json")
        try:
            with open("preset2.json", "w") as f:
                json.dump(preset_data, f)
        except IOError:
            QMessageBox.critical(None, "Error", "Failed to save Preset 2")

    # 프리셋 3에 슬라이더 값 저장하는 함수
    def save_preset3(self):
        red_value = self.red_slider.value()
        blue_value = self.blue_slider.value()
        green_value = self.green_slider.value()

        # JSON 형식으로 저장
        preset_data = {
            "red_value": red_value,
            "blue_value": blue_value,
            "green_value": green_value
        }

        current_dir = os.path.dirname(os.path.realpath(__file__))
        preset_file = os.path.join(current_dir, "preset3.json")
        try:
            with open("preset3.json", "w") as f:
                json.dump(preset_data, f)
        except IOError:
            QMessageBox.critical(None, "Error", "Failed to save Preset 3")

    # 프리셋 1 불러오는 함수
    def load_preset1(self):
        try:
            with open("preset1.json", "r") as f:
                preset1_data = json.load(f)
                self.apply_preset(preset1_data)
        except FileNotFoundError:
            QMessageBox.critical(None, "Error", "Preset 1 file not found")

    # 프리셋 2 불러오는 함수
    def load_preset2(self):
        try:
            with open("preset2.json", "r") as f:
                preset2_data = json.load(f)
                self.apply_preset(preset2_data)
        except FileNotFoundError:
            QMessageBox.critical(None, "Error", "Preset 2 file not found")

    # 프리셋 3 불러오는 함수
    def load_preset3(self):
        try:
            with open("preset3.json", "r") as f:
                preset3_data = json.load(f)
                self.apply_preset(preset3_data)
        except FileNotFoundError:
            QMessageBox.critical(None, "Error", "Preset 3 file not found")

    def apply_preset(self, preset_data):
        # 프리셋 데이터를 적용하는 함수
        red_value = preset_data.get("red_value", 0)
        blue_value = preset_data.get("blue_value", 0)
        green_value = preset_data.get("green_value", 0)

        # 각 슬라이더에 값 설정
        self.red_slider.setValue(red_value)
        self.blue_slider.setValue(blue_value)
        self.green_slider.setValue(green_value)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.red_value_level.setText(_translate("Dialog", "0"))
        self.blue_value_level.setText(_translate("Dialog", "0"))
        self.green_value_level.setText(_translate("Dialog", "0"))
        self.red_text.setText(_translate("Dialog", "Red(적색)"))
        self.blue_text.setText(_translate("Dialog", "Blue(청색)"))
        self.green_text.setText(_translate("Dialog", "Green(녹색)"))

    def update_red_value_ui(self, value):
        self.red_value_level.setText(str(value))

    def update_blue_value_ui(self, value):
        self.blue_value_level.setText(str(value))

    def update_green_value_ui(self, value):
        self.green_value_level.setText(str(value))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
