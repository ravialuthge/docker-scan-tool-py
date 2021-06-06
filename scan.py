import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate
import sys
import getopt
import test_cases.docker_containers
import test_cases.docker_host
import test_cases.docker_images
import runpy
from plugins.datadir import dockerdatadirscan
from plugins.dockeruser import dockeruserscan
from plugins.common import outputpl
from test_cases.process import cis_version
from test_cases.docker_host import cis_version_120

def output():
	

	table = test_cases.docker_images.container_user()
	update_instruction_table = test_cases.docker_images.update_ins()

	table_he = test_cases.docker_containers.health_check()
	table_apparmor = test_cases.docker_containers.apparmor()
	
	full_cmd_arguments = sys.argv

	banner = (colored("# --------------------------------------------------------------------------------------------\n\
# CIS Docker {0} Benchmark\n\
# # {1}\n\
# --------------------------------------------------------------------------------------------\n\
	", 'green', attrs=['bold']))


	sc_ho	= (colored('Docker Host',attrs=['bold']))
	sc_im	= (colored('Docker Images',attrs=['bold']))
	sc_im_1	= (tabulate(table))
	sc_im_2	= (tabulate(update_instruction_table))
	sc_co   = (colored('Docker Containers',attrs=['bold']))
	sc_co_1 = (tabulate(table_he))
	sc_co_2 = (tabulate(table_apparmor))
	sc_ho_plugin_120 = cis_version(version_plugins=[cis_version_120()])


	arguments = len(sys.argv) -1
	if arguments == 0:
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_120.version_run()
		print (sc_im)
		print (sc_im_1)
		print (sc_im_2)
		print (sc_co)
		print (sc_co_1)
		print (sc_co_2)
		
	elif (sys.argv[1] == '-p' or sys.argv[1] == '--plugin') and sys.argv[2] == 'testplugin':
		sc_ho_plugin_120.version_run()
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and sys.argv[2] == '1.1.0':
		sub_version="1.1.0"
		main_version="v1.1.0 - 07-06-2017"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and (sys.argv[2] == '1.0.0'):
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_a="1.11.0"
		print (banner .format(sub_version_a, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_b="1.12.0"
		print (banner .format(sub_version_b, main_version))
		print (sc_ho)

		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_c="1.13.0"
		print (banner .format(sub_version_c, main_version))
		print (sc_ho)
		
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)	
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.6':
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.11.0':
		sub_version="1.11.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.12.0':
		sub_version="1.12.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.13.0':
		sub_version="1.13.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'host':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'images':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_im)
		print (sc_im_1)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'containers':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
		print ("help")
	else:
		print ("error")


if __name__ == "__main__":     
	output()
os.remove("re.txt")
os.remove("re_st.txt")
os.remove("re_he.txt")
os.remove("re_st_he.txt")
os.remove("re_up.txt")
os.remove("re_st_up.txt")
os.remove("re_apparmor.txt")
os.remove("re_st_apparmor.txt")