import os 
#import subprocess

cur_dir = os.getcwd()
conf_file= cur_dir + "/scripts/iota_api/conf"

#subprocess.call(["cp", conf_file, conf_file + ".bak"])
os.popen("cp %s %s" % (conf_file, conf_file + ".bak"))
