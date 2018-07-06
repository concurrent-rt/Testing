
# Need to modified some code because it's stopping when it execute 'iperf -s' command, 
# It should run Background 


import subprocess
import os
import sys
import time
import threading
import logging
import common


PATH="/home/test/jailhouse"
mod_path="/home/test/jailhouse/driver/jailhouse.ko"
root_cell_path="configs/x86/rootcell-8256M-working.cell"
nrc1_filepath="configs/x86/non-rootcell-working-8256M.c"
nrc1_config="configs/x86/non-rootcell-working-8256M.cell"

ip1="172.24.0.95"

timeout="8s"

def set_sshpass_nrc1():
	# commands to copy stress-ng file to non rootcell.       	
	while True:	
		proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
		proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
		proc=subprocess.Popen(['ping -c4 172.24.0.95 | wc '],stdout=subprocess.PIPE, shell=True)
		stdout,stderr = proc.communicate()
		logging.info('runnung while')
		time.sleep(10)
		rc = proc.poll()
		if '9' not in stdout:
			logging.info(' IN IF : %s' % stdout)		
		else:			
			logging.info(' IN ELSE : %s' % stdout)			
			break

	logging.info('Before SCP of stress-ng')  
	proc=subprocess.Popen(['sshpass -p spanidea scp -o StrictHostKeyChecking=no -r /root/sanket/stress-ng root@%s:/usr/bin/ ' % ip1], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('SCP stress-ng failed %s' % stderr)
		set_sshpass_nrc1()
	else :
		logging.info('SCP of stress-ng SUCCESS')  


	logging.info('Before SCP of iperf')  
	proc=subprocess.Popen(['sshpass -p spanidea scp -o StrictHostKeyChecking=no -r /root/sanket/iperf root@%s:/usr/bin/ ' % ip1], stdout=subprocess.PIPE, shell=True)	
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU stress failed on nrc1 with error %s' % stderr)
		set_sshpass_nrc1()
	else :
		logging.info('SCP of iperf SUCCESS')  


#TCP server iperf
def cpu_iperf_nrc1():
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	
	proc=subprocess.Popen(['sshpass -p spanidea ssh -o StrictHostKeyChecking=no root@%s iperf -s &' % ip1], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU iperf failed on nrc1 with error %s' % stderr)
	else :
		logging.info(' START iperf on NON ROOT CELL (SERVER) ')			
		logging.info(' %s' % stdout)
                logging.info(' END iperf on NON ROOT CELL')


#TCP client iperf
def cpu_iperf_root():
	proc=subprocess.Popen(['iperf -c %s' % ip1 ], stdout=subprocess.PIPE,shell=True) 
	stdout,stderr = proc.communicate()	
	rc = proc.poll()
	logging.info(' START IPERF ROOT CELL (CLIENT)')
	if rc != 0:
		logging.error('iperf failed with error %s' % stderr)
	else :
		logging.info('%s' % stdout)
	        logging.info(' END CPU STRESS FOR ROOT CELL')


#STRESS_NG Root cell
def cpu_stress_root():
	proc=subprocess.Popen(['stress-ng --cpu 10 --io 7 --vm 7 --vm-bytes 256M --timeout %s' % timeout ], stdout=subprocess.PIPE,shell=True) 
	stdout,stderr = proc.communicate()	
	rc = proc.poll()
	logging.info(' START CPU STRESS FOR ROOT CELL')
	if rc != 0:
		logging.error('Stress on cpu failed with error %s' % stderr)
	else :
		logging.info('CPU stress in rootcell: %s' % stdout)
	        proc=subprocess.Popen(['uptime'], stdout=subprocess.PIPE,shell=True)
        	stdout,stderr = proc.communicate()
		logging.info('%s',stdout)
		logging.info(' END CPU STRESS FOR ROOT CELL')


def cpu_stress_nrc1():
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	
	proc=subprocess.Popen(['sshpass -p spanidea ssh -o StrictHostKeyChecking=no root@%s stress-ng --cpu 1  --io 1 --vm 1 --vm-bytes 256M --timeout %s' % (ip1,timeout)], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU stress failed on nrc1 with error %s' % stderr)
	else :
		logging.info(' START CPU STRESS FOR NON ROOT CELL')			
		logging.info('CPU stress in nrc1: %s' % stdout)
                proc=subprocess.Popen(['sshpass -p spanidea ssh -o StrictHostKeyChecking=no root@%s uptime' % ip1 ], stdout=subprocess.PIPE,shell=True)
                stdout,stderr = proc.communicate()
                logging.info('%s',stdout)		
		logging.info(' END CPU STRESS FOR NON ROOT CELL')


def get_name(filename):
	f=open(filename)
	for line in f:
		if ".name" in line:
			list=line.split()
			name=list[2]
			name=name.strip('",')
			return name


if __name__=="__main__":
	os.chdir(PATH)

	logging.basicConfig(filename='test2.log', filemode='w', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

	# unset ttyS0 and ttyS1 
	unset1=subprocess.Popen(['setserial /dev/ttyS0 uart none'], stdout=subprocess.PIPE, shell=True)
	unset2=subprocess.Popen(['setserial /dev/ttyS1 uart none'], stdout=subprocess.PIPE, shell=True)

	#Check if jailhouse module is loaded
	lsmod=subprocess.Popen(['lsmod | grep jailhouse'], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = lsmod.communicate()
	rc = lsmod.poll()
	if rc != 0:
		logging.info('Jailhouse module is not installed')
		#Install the jailhouse module
		insmod=subprocess.Popen(['insmod %s' % mod_path], stdout=subprocess.PIPE, shell=True)
		stdout,stderr = insmod.communicate()
		rc = insmod.poll()
		if rc != 0:
			logging.error('Installing jailhouse module failed')
			sys.exit()
		else:
			logging.info('Installed jailhouse module')
	else:
		logging.info('Jailhouse module is already installed')
	


	#Enable the root cell
	proc=subprocess.Popen(['jailhouse cell list | grep RootCell'], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	rc = common.jailhouse_enable_cell(root_cell_path)
	time.sleep(20)
	if rc != 0:
		logging.error('Enabling root cell failed with error:%s' % stderr)
		sys.exit()
	else:
		logging.info('Root cell enabled successfully')
	time.sleep(5)
	

	#check if root cell is in running state	
	
	proc=subprocess.Popen(['jailhouse cell list | grep RootCell'], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0 or 'running' not in stdout:
		logging.error('Root cell is not in running state')
		sys.exit()
	else:
		logging.info('Root cell is in running state')


	nrc1=get_name(nrc1_filepath)
	print nrc1

	#Create first non root cell
	common.jailhouse_cell_linux(nrc1_config,ip1)
	time.sleep(2)		
	cell_list = common.jailhouse_cell_list()
	

	#check if nonroot cell 1 is displayed in jailhouse cell list
	if nrc1 not in cell_list:
		logging.error('%s not listed in jailhouse cell list output' % nrc1)
		sys.exit()
	else:
		proc=subprocess.Popen(['jailhouse cell list | grep %s | awk \'{ print $3 }\'' % nrc1], stdout=subprocess.PIPE, shell=True)
		stdout,stderr = proc.communicate()
		rc = proc.poll()
		print stdout
		if 'running' not in stdout:
			logging.error('%s is not in running state' % nrc1)
			sys.exit()
		else:
			logging.info('%s is created and running successfully' % nrc1)	


	time.sleep(30)	
	set_sshpass_nrc1()

	cpu_iperf_nrc1()
	time.sleep(10)
	cpu_iperf_root()
	time.sleep(15)


	start=time.time()
	end= start+300

	#applied stress on every 120sec on Root cell and Non Root Cell
	while start<=end :
		if time.time()%20 == 0 : 		
			common.jailhouse_cell_list()
			cpu_stress_root()
			cpu_stress_nrc1()

