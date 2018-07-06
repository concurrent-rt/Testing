# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
    clickButton(waitForObject(":groupBox_Actions.pushButton_import_QPushButton"))
    clickButton(waitForObject(":groupBox_Import.pushButton_import_config_QPushButton"))
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "qemu-gui"), 58, 6, 0, Qt.LeftButton)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 98, 213, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 98, 213, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 98, 213, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":stackedWidget.treeView_QTreeView"), 98, 213, -120, 0, 2)
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "Downloads"), 87, 5, 0, Qt.LeftButton)
    doubleClick(waitForObjectItem(":stackedWidget.treeView_QTreeView", "Nonroot-GUI-edit(1)\\.c"), 139, 3, 0, Qt.LeftButton)
    clickButton(waitForObject(":groupBox_Import.pushButton_create_imported_config_QPushButton"))
    
    if object.exists("{container=':stackedWidget.stackedWidget_2_QStackedWidget' name='lineEdit_CellName' type='QLineEdit' visible='1'}"):
        test.passes("testcase for import file is passed")
        clickButton(waitForObject(":stackedWidget_2.pushButton_QPushButton"))
        clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
        clickButton(waitForObject(":Closing Application.Yes_QPushButton"))
    else :
        test.fail("fail to import file")
