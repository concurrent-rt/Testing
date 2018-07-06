import subprocess
import os
import sys
import time
import threading
import logging
import common


PATH="/home/xeon/veth-jail/jailhouse"
mod_path="/home/xeon/veth-jail/jailhouse/driver/jailhouse.ko"
root_cell_path="configs/x86/rootcell-6134M-virtual-net-console.cell"
nrc1_filepath="configs/x86/non-root-6134M-virtual-net-console-1.c"
nrc2_filepath="configs/x86/non-root-6134M-virtual-net-console-2.c"
nrc1_config="configs/x86/non-root-6134M-virtual-net-console-1.cell"
nrc2_config="configs/x86/non-root-6134M-virtual-net-console-2.cell"


ip1="172.24.0.95"
ip2="196.168.1.55"

timeout =10

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

	logging.info('ANIl: before sshpass')  
	proc=subprocess.Popen(['sshpass -p spanidea scp -o StrictHostKeyChecking=no -r /home/xeon/Downloads/ANIL/stress-ng-master/stress-ng root@%s:/usr/bin/ ' % ip1], stdout=subprocess.PIPE, shell=True)
        logging.info('ANIl: after sshpass')  
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU stress failed on nrc1 with error %s' % stderr)
		set_sshpass_nrc1()


def cpu_stress_root():
	proc=subprocess.Popen(['stress-ng --cpu 0 --timeout 315' ], stdout=subprocess.PIPE,shell=True) 
	stdout,stderr = proc.communicate()	
	rc = proc.poll()
	logging.info(' START CPU STRESS FOR ROOT CELL')
	if rc != 0:
		logging.error('Stress on cpu failed with error %s' % stderr)
	else :
		logging.info('CPU stress in rootcell: %s' % stdout)
		logging.info(' END CPU STRESS FOR ROOT CELL')


def cpu_stress_nrc1():
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	proc=subprocess.Popen(['ifconfig enp0s14 172.24.0.90 netmask 255.255.255.0 up '], stdout=subprocess.PIPE, shell=True)
	
	proc=subprocess.Popen(['sshpass -p spanidea ssh -o StrictHostKeyChecking=no root@%s stress-ng --cpu 0 --timeout 315' % ip1], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU stress failed on nrc1 with error %s' % stderr)
	else :
		logging.info(' START CPU STRESS FOR NON ROOT CELL')			
		logging.info('CPU stress in nrc1: %s' % stdout)
		logging.info(' END CPU STRESS FOR NON ROOT CELL')

'''
def cpu_stress_nrc2(timeout=18000):
	proc=subprocess.Popen(['ssh root@%s \'sudo stress-ng --cpu 0 --timeout 25200' % (ip2,timeout)], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('CPU stress failed on nrc1 with error %s' % stderr)

	logging.info('CPU stress in nrc2: %s' % stdout)

'''



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

	#cpu_count = common.get_number_of_cpus()

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
	
	'''
	if rc == 0:
		common.jailhouse_disable()
	

	if rc != 0 or 'running' not in stdout:
		
		rc = common.jailhouse_enable_cell(root_cell_path)
		time.sleep(20)
		if rc != 0:
			logging.error('Enabling root cell failed with error:%s' % stderr)
			sys.exit()
		else:
			logging.info('Root cell enabled successfully')
	else:
				
		logging.info('Root cell is already enabled')
	'''

	rc = common.jailhouse_enable_cell(root_cell_path)
	#time.sleep(20)
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
	nrc2=get_name(nrc2_filepath)

	print nrc1
	print nrc2



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


	time.sleep(60)	
	set_sshpass_nrc1()
	start=time.time()
	end= start+200
	while start<=end :
		if time.time()%22 == 0 : 		
			common.jailhouse_cell_list()
			cpu_stress_root()
			cpu_stress_nrc1()


