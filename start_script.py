import subprocess, os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
python_exec = 'py -3.6'


# Code starts here.

filename = 'winstatus.py'

while True:
    """However, you should be careful with the '.wait()'"""
    p = subprocess.Popen(python_exec + " " + SCRIPT_DIR + "\\" + filename, shell=True).wait()

    if p != 0:
        continue
    else:
        break
