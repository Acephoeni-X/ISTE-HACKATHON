from tkinter import *
from Crypto.Cipher import AES
import base64
import os

def decrypt():
    PADDING = '&'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    keys = key.get()
    encryptedString = encrypted_body.get('1.0', 'end')
    cipher = AES.new(keys)
    decoded = DecodeAES(cipher, encryptedString)
    print(str(decoded).replace('&', ''))

    decrypted_body_Label = Label(root, text = 'Your Decrypted message is: ',width=60, font = ('Sans Serif', 15, 'bold'))
    decrypted_body_Label.place(x=10, y=400)
    decoded = str(decoded).replace('&', '')
    decoded = decoded.replace('b\'', '')
    decoded = decoded.replace('\n', '')
    decoded = decoded.replace('\'', '')
    decrypted_body = Label(root, text = decoded)
    decrypted_body.place(x=10, y=450)


if __name__ == '__main__':
    root = Tk()
    root.geometry('700x700')
    root.title('Decrypter')

    keyPhrase = Label(root, text = 'Enter the key: ', font = ('Sans Serif', 15, 'bold'))
    keyPhrase.place(x=20, y=80)

    global key
    key = StringVar()
    keyEntry = Entry(root, textvariable = key, width = 50)
    keyEntry.place(x=150, y=80)

    encrypted_body_label = Label(root, text = 'Enter the Encrypted Message: ', font = ('Sans Serif', 15, 'bold'))
    encrypted_body_label.place(x=10, y=200)

    global  encrypted_body

    encrypted_body = Text(root, width=60, height = 10)
    encrypted_body.place(x=250, y=200)

    decrypt_button = Button(root, text = 'Decrypt', command = decrypt)
    decrypt_button.place(x=250, y=350)

    root.resizable(False, False)
    root.mainloop()



#decrypt('TjkqCezmL5POW8UCK8nQmH1kscMq+wr6zGixMFduXUg=','Rishi2002&&&&&&&')
