import os 

os.system('pip install onetimepass')
os.system('pip install json')


import json

boilerplate = {
    "account":[]
}
with open('file.json' , 'w') as f:
    json.dump(boilerplate, f, indent=4)
