import os, subprocess

cur_dir = os.getcwd()
conf_file= cur_dir + "scripts/iota_api/conf"

subprocess.call(["cp", conf_file, conf_file + ".bak"])
