# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
    setWindowState(waitForObject(":MainWindow_MainWindow"), WindowState.Normal)
    clickButton(waitForObject(":frame_3.pushButton_15_QPushButton"))
    scrollTo(waitForObject(":tableWidget_cell_config_2_QScrollBar_2"), 1376)
    sendEvent("QWheelEvent", waitForObject(":tableWidget_cell_config_2_QLineEdit_20"), 130, 7, -120, 0, 2)
    clickButton(waitForObject(":groupBox_4.pushButton_Mem_Config_Add_QPushButton"))
    scrollTo(waitForObject(":tableWidget_cell_config_2_QScrollBar_2"), 1413)
    sendEvent("QMouseEvent", waitForObject(":tableWidget_cell_config_2_QScrollBar_2"), QEvent.MouseButtonDblClick, 6, 256, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":tableWidget_cell_config_2_QScrollBar_2"), QEvent.MouseButtonRelease, 6, 256, Qt.LeftButton, 0, 0)
    scrollTo(waitForObject(":tableWidget_cell_config_2_QScrollBar_2"), 1416)
    clickButton(waitForObject(":groupBox_4.pushButton_save_mem_region_QPushButton"))
    
    obj = waitForObject("{type='QMessageBox' unnamed='1' visible='1' windowTitle='wrong input'}")
    
    test.compare(str(obj.windowTitle), "wrong input" , "Empty Row Checking")
    
    clickButton(waitForObject(":wrong input.OK_QPushButton"))

    scrollTo(waitForObject(":tableWidget_cell_config_2_QScrollBar"), 384)
    mouseClick(waitForObject(":tableWidget_cell_config_2_QLineEdit_21"), 62, 17, 0, Qt.LeftButton)
    mouseClick(waitForObject(":tableWidget_cell_config_2_QLineEdit_21"), 62, 17, 0, Qt.LeftButton)
    type(waitForObject(":tableWidget_cell_config_2_QLineEdit_21"), "sddssd")
    mouseClick(waitForObject(":tableWidget_cell_config_2_QLineEdit_21"), 65, 17, 0, Qt.LeftButton)
    mouseClick(waitForObject(":tableWidget_cell_config_2_QLineEdit_22"), 55, 12, 0, Qt.LeftButton)
    type(waitForObject(":tableWidget_cell_config_2_QLineEdit_22"), "weew")
    mouseClick(waitForObject(":tableWidget_cell_config_2_QLineEdit_23"), 43, 26, 0, Qt.LeftButton)
    type(waitForObject(":tableWidget_cell_config_2_QLineEdit_23"), "rereer")
    clickButton(waitForObject(":groupBox_4.pushButton_save_mem_region_QPushButton"))
    
    obj = waitForObject("{type='QMessageBox' unnamed='1' visible='1' windowTitle='wrong input'}")
    test.compare(str(obj.windowTitle), "wrong input" , "Wrong Input Checking")
    

    clickButton(waitForObject(":wrong input.OK_QPushButton"))
    clickButton(waitForObject(":groupBox_12.pushButton_Exit_QPushButton"))
    clickButton(waitForObject(":Closing Application.Yes_QPushButton"))
