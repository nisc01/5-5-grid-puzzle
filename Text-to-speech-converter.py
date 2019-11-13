#!/bin/python3
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QLineEdit
import pyttsx3
import sys
engine=pyttsx3.init()
app=QApplication([])
# Creating a outer window widget
widget=QWidget()
widget.resize(700,500)
widget.setWindowTitle('Text-speech Converter')
# Creating a label
class Label:
    def __init__(self,name,x_position,y_position):
        self.name=name
        self.x_position=x_position
        self.y_position=y_position

    def create_label(self):
        label=QLabel(widget)
        label.setText(self.name)
        label.move(self.x_position,self.y_position)

text=Label('Enter the text',10,15)
text.create_label()
speech_rate=Label('Speech Rate',10,150)
speech_rate.create_label()
# Taking input from GUI through LineEdit
text_in=QLineEdit(widget)
text_in.move(10,40)
text_in.resize(600,30)
# Creating QPushButton
class Button:

    def __init__(self,name,x_position,y_position):
        self.name=name
        self.x_position=x_position
        self.y_position=y_position


    def speech_(self,rate):
        def speech_rate(self):
            engine.setProperty('rate',rate)
            engine.say(text_in.text())
            engine.runAndWait()
        button=QPushButton(widget)
        button.setText(self.name)
        button.move(self.x_position,self.y_position)
        button.clicked.connect(speech_rate)

low=Button('low',90,150)
low.speech_(100)
high=Button('high',190,150)
high.speech_(150)
widget.show()
app.exec_()