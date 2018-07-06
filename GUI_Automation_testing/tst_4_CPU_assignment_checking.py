# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    doubleClick(waitForObject(":stackedWidget.lineEdit_NO_CELLS_QLineEdit"), 40, 2, 0, Qt.LeftButton)
    type(waitForObject(":stackedWidget.lineEdit_NO_CELLS_QLineEdit"), "<Keypad_3>")
    type(waitForObject(":stackedWidget.lineEdit_NO_CELLS_QLineEdit"), "<Keypad_Enter>")
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 80, 14, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot1"), 79, 8, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU1"), 11, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU2"), 10, 9, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU3"), 7, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 90, 11, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot2"), 90, 16, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU2"), 10, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU3"), 9, 8, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 140, 9, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot1"), 132, 5, 0, Qt.LeftButton)
    
    obj = waitForObject("{container=':stackedWidget_2.listWidget_CPUs_QListWidget' text='CPU2' type='QModelIndex'}")
    test.compare(str(obj.checkState), "unchecked")
    
    clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
    clickButton(waitForObject(":Closing Application.Yes_QPushButton"))
