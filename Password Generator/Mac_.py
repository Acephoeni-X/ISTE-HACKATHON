from tkinter import *
import random
import array
import onetimepass as otp
import os
import json

global root
global generated_pass
global submit
global randomPassword
global password_size
global frame

def create_password():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(int(password_size.get())-4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
            password = password + x
            
    return password

def write_json(data, filename='file.json'):
    with open ('file.json', 'w') as f:
        json.dump(data, f, indent=4)

def make_json():
    global added
    Font_tuple = ("Comic Sans MS", 10, "bold")
    added = Label(root, text = 'SUCCESSFULLY ADDED !', font = Font_tuple)
    added.place(x=100, y = 500)
    a = entered_username.get()
    b = key_value.get()
    values = {
        a:b
    }
    with open('file.json') as f:
        data = json.load(f)
        temp = data['account']
        temp.append(values)
    write_json(data)  

def on_click():
    randomPassword.set(create_password())

def add_value():
    try:
        get_key.destroy()
        account_name.destroy()
        enterAccountName.destroy()
        yourOTP.destroy()
    except:
        pass
    global username
    global entered_username
    global shared_key
    global username_value
    global add_button
    global shared_key_value
    global key_value
    entered_username = StringVar()
    key_value = StringVar()
    username = Label(root, text = 'ACCOUNT NAME:')
    username.place(x=25, y=350)
    shared_key = Label(root, text = 'SHARED KEY:')
    shared_key.place(x=25, y=400)
    username_value = Entry(root, textvariable=entered_username, width=20)
    username_value.place(x=150, y=350)
    shared_key_value = Entry(root, textvariable=key_value)
    shared_key_value.place(x=150, y=400)
    add_button = Button(root, text = 'Add Account', command=make_json)
    add_button.place(x=120, y = 450)
    
def get_secret_key():
    Font_tuple = ("Comic Sans MS", 15, "bold")
    value = account_id.get()
    with open('file.json', 'r') as f:
        data = json.load(f)
        a = []
        b = []
        for i in range(len(data["account"])):
            a += (data["account"][i].keys())
            b += (data["account"][i].values())
        for i in range(len(a)):
            if value == a[i]:
                global yourOTP
                my_token = ''
                my_token = otp.get_totp(b[i])
                yourOTP = Label(root, text = 'OTP: ', font=Font_tuple)
                yourOTP.place(x=100, y=400)
                if my_token == '':
                    onetimepassword = Label(root, text = 'WRONG SHARED KEY !')
                    onetimepassword.place(x=150, y=400)
                else:
                    onetimepassword = Label(root, text = my_token, font=Font_tuple)
                    onetimepassword.place(x=150, y=400)
        
def get_value():
    try:
        username.destroy()
        shared_key.destroy()
        username_value.destroy()
        add_button.destroy()
        shared_key_value.destroy()
        added.destroy()
    except:
        pass
    global account_name
    global account_id
    global get_key
    global enterAccountName
    account_id = StringVar()
    account_name = Label(root, text = 'ACCOUNT NAME:')
    account_name.place(x=25, y=350)
    enterAccountName = Entry(root, textvariable = account_id)
    enterAccountName.place(x=150, y=350)
    Font_tuple = ("Comic Sans MS", 10, "bold")
    notShowing = Label(root, text = '* NOTE: IF OTP IS NOT SHOWING SHARED KEY MIGHT BE WRONG !', font=Font_tuple)
    notShowing.place(x=20, y=550)
    get_key = Button(root, text = 'GET KEY!', font=(15), command = get_secret_key)
    get_key.place(x=150, y=500)

if __name__=='__main__':
    root = Tk()
    root.geometry('400x600')
    root.title('Password Application')
    randomPassword = StringVar(root)
    password_size = StringVar(root, value='16')
    Font_tuple = ("Comic Sans MS", 15, "bold")
    generate_random_password = Label(root, text = 'Generate Strong Random Password!', font = Font_tuple)
    generate_random_password.place(x=25, y=20)
    Pasword_length = Label(root, text = 'Password Length: ')
    Pasword_length.place(x=50, y=108)
    generated_pass = Entry(root, textvariable = randomPassword, width=30)
    generated_pass.place(x=110, y=70)
    submit = Button(root, text='Generate', command = on_click)
    submit.place(x=150, y=150)
    length = Spinbox(root, from_ = 8, to_ = 120, textvariable = password_size , width = 8)
    length.place(x=170, y=110)

    twoFactor = Label(root, text = '2 Factor authenticator', font = Font_tuple)
    twoFactor.place(x=90, y= 240)
    add = Button(root, text = 'ADD ACCOUNT', command = add_value)
    add.place(x=60, y=300)
    generate = Button(root, text = 'GENERATE', command = get_value)
    generate.place(x=230, y=300)
    root.resizable(False, False)
    root.mainloop()
