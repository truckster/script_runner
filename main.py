import os
import sys
import subprocess
from glob import glob
from time import gmtime, strftime, localtime


def process_status(text):
    print(strftime("%X", localtime()) + " %s" % text)
    return 0


script_path = "/home/gpu/Simulation/test/"
output_path = "/home/gpu/Simulation/maximus/"
os.chdir(script_path)
for file in glob("*.sh"):
    process_status("Running script: " + file)
    p = subprocess.Popen(script_path + file)

    p_status = p.wait()



