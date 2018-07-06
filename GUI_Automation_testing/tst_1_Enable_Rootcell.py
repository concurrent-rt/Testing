# -*- coding: utf-8 -*-

def main():
    startApplication("AppRun 74M 6M")
    
    
    if object.exists("{type='QMessageBox' unnamed='1' visible='1' windowTitle='Jailhouse Install'}"):
        obj = waitForObject("{type='QMessageBox' unnamed='1' visible='1' windowTitle='Jailhouse Install'}")
        if str(obj.text) == "Please wait Jailhouse is installing...":
            test.log("Jailhouse was not installed. Installing now")
            #clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
        elif str(obj.text) == "Jailhouse is already installed":
            test.log("Jailhouse is already installed")
            clickButton(waitForObject(":Jailhouse Install.OK_QPushButton"))
        else:
            test.fail("Failed to install jailhouse")
    clickButton(waitForObject(":groupBox_12.pushButton_enable_cell_QPushButton"))
    clickButton(waitForObject(":listWidget_CellList.RootCell_QRadioButton"))
    clickButton(waitForObject(":JailhouseEnable.pushButton_StartCell_QPushButton"))
    
    if object.exists("{type='QMessageBox' unnamed='1' visible='1' windowTitle='Enabling cell'}"):
        test.log("")
        clickButton(waitForObject(":Enabling cell.OK_QPushButton"))
        
    
    clickButton(waitForObject(":groupBox_12.pushButton_DisableCell_QPushButton"))
    clickButton(waitForObject(":listWidget_CellList.RootCell_QRadioButton"))
    clickButton(waitForObject(":JailhouseEnable.pushButton_StartCell_QPushButton"))
    
    if object.exists("{type='QMessageBox' unnamed='1' visible='1' windowTitle='Disabling cell'}"):
        test.log("")
        clickButton(waitForObject(":Disabling cell.OK_QPushButton"))
