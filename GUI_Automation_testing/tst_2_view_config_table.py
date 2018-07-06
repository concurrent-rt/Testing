# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    clickButton(waitForObject(":groupBox_Actions.pushButton_import_QPushButton"))
    clickButton(waitForObject(":groupBox_Import.pushButton_import_config_QPushButton"))
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "qemu-gui"), 45, 5, 0, Qt.LeftButton)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 62, 238, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 62, 238, -120, 0, 2)
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "Downloads"), 59, 8, 0, Qt.LeftButton)
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "Nonroot-GUI-edit(1)\\.c"), 60, 4, 0, Qt.LeftButton)
    clickButton(waitForObject(":groupBox_Import.pushButton_create_imported_config_QPushButton"))
   
    if object.exists("{container=':stackedWidget.stackedWidget_2_QStackedWidget' name='pushButton' type='QPushButton' visible='1'}"):       
        clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
        clickButton(waitForObject(":groupBox_Actions.pushButton_View_Configuration_QPushButton"))
        clickButton(waitForObject(":groupBox_Actions.pushButton_View_Configuration_QPushButton"))
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 259, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 259, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 259, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 259, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 259, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(":View Configuration_QTableView"), 368, 260, 120, 0, 2)
        test.passes("View COnfig test pass")
        
        clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
        clickButton(waitForObject(":Closing Application.Yes_QPushButton"))
        
    else :
        test.fail("fail view config testcase")

