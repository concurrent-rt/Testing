# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU2"), 10, 3, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU3"), 11, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 144, 6, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot1"), 131, 16, 0, Qt.LeftButton)
    obj = waitForObject("{container=':stackedWidget_2.listWidget_CPUs_QListWidget' text='CPU0' type='QModelIndex'}")
    test.compare(str(obj.enabled), "False")
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU0"), 9, 9, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU0"), 9, 9, 0, Qt.LeftButton)
    doubleClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU0"), 10, 8, 0, Qt.LeftButton)
    doubleClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU0"), 10, 8, 0, Qt.LeftButton)
    doubleClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU0"), 10, 8, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU1"), 13, 8, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU3"), 8, 11, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 137, 15, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "RootCell"), 83, 12, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU2"), 11, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.listWidget_CPUs_QListWidget", "CPU3"), 11, 7, 0, Qt.LeftButton)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    mouseClick(waitForObject(":stackedWidget_2.comboBox_CellList_QComboBox"), 137, 11, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":stackedWidget_2.comboBox_CellList_QComboBox", "NonRoot1"), 126, 11, 0, Qt.LeftButton)
    clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
    clickButton(waitForObject(":Closing Application.Yes_QPushButton"))



    
    
    