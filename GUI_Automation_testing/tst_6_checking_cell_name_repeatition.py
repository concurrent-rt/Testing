# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 211, 5, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot1"), 188, 7, 0, Qt.LeftButton)
    doubleClick(waitForObject(":stackedWidget_2.lineEdit_CellName_QLineEdit"), 144, 13, 0, Qt.LeftButton)
    type(waitForObject(":stackedWidget_2.lineEdit_CellName_QLineEdit"), "rootcell")
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    if object.exists("{container=':stackedWidget.stackedWidget_2_QStackedWidget' name='comboBox_CellList' type='QComboBox' visible='1'}"):
        test.fail("test case failed...cell name is repeating")
    else :
        test.passes("Test case pass ..not allowing cell name repeatedly")
        clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
        clickButton(waitForObject(":Closing Application.Yes_QPushButton"))
