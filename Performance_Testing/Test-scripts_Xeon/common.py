import subprocess
import os
import logging
import time

#PATH="/home/jail/Jailhouse-master"
redhawk_image="/home/xeon/veth-jail/jailhouse/bzImage-redhawk"
rootfs_path="/home/xeon/veth-jail/jailhouse/initrd-full.img"
#nrc_path="/home/jail/configs/x86/shm-nonrootcell.c"

def jailhouse_cell_list():
	proc=subprocess.Popen(['jailhouse cell list'],  stdout=subprocess.PIPE,shell=True) 
	stdout,stderr = proc.communicate()	
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to execute jailhouse cell list')
		logging.error('Error returned: %s' % stderr)

	else:
		logging.info('Working fine') 
	
	return stdout



def jailhouse_create_cell(path):
	proc=subprocess.Popen(['jailhouse cell create %s' % path], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to create cell')
		logging.error('Error returned: %s' % stderr)
	

def jailhouse_enable_cell(path):
	proc=subprocess.Popen(['jailhouse enable %s' % path], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to enable cell')
		logging.error('Error returned: %s' % stderr)
	return rc

def jailhouse_disable():
	proc=subprocess.Popen(['jailhouse disable'], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to disable jailhouse')
		logging.error('Error returned: %s' % stderr)
	#return rc



def jailhouse_cell_linux(config_path,ip):
	proc=subprocess.Popen(['jailhouse cell linux %s %s -i %s -c "console=ttyS0,115200 8250.nr_uarts=1 ip=%s"' % (config_path,redhawk_image,rootfs_path,ip)], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to create nonroot cell')
		logging.error('Error returned: %s' % stderr)
	else:
		logging.info('Created nonroot cell')
		


def jailhouse_load_cell(cell_name,path):
	proc=subprocess.Popen(['jailhouse cell load %s %s' % (cell_name,path)], stdout=subprocess.PIPE,shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to load cell')
		logging.error('Error returned: %s' % stderr)


def jailhouse_destroy_cell(cell_name):
	proc=subprocess.Popen(['jailhouse cell destroy %s' % cell_name], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to destroy cell')
		logging.error('Error returned: %s' % stderr)


def jailhouse_start_cell(cell_name):
	proc=subprocess.Popen(['jailhouse cell start %s' % cell_name], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to start cell')
		logging.error('Error returned: %s' % stderr)


def jailhouse_shutdown_cell(cell_name):
	proc=subprocess.Popen(['jailhouse cell shutdown %s' % cell_name], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to shutdown cell')
		logging.error('Error returned: %s' % stderr)


def get_number_of_cpus():
	proc=subprocess.Popen(['nproc'], stdout=subprocess.PIPE, shell=True)
	stdout,stderr = proc.communicate()
	rc = proc.poll()
	if rc != 0:
		logging.error('Failed to get number of CPUs')
	else:
		logging.info('Number of CPUs')
	cpu_count = int(stdout)
	return cpu_count


if __name__=="__main__":
	os.chdir(PATH)
