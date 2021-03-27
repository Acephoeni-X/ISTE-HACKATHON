from Crypto.Cipher import AES
import base64
import os

def decrypt(encryptedString, key):
    PADDING = '&'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    print(str(decoded).replace('&', ''))

# # def decrypt(enc ):
# #         enc = base64.b64decode(enc)
# #         iv = enc[:16]
# #         
# #         cipher = AES.new(key, AES.MODE_CBC, iv )
# #         print(cipher.decrypt(enc))


decrypt('2O/Qh4za4JeiiXd1+As+/A==','kavya&&&&&&&&&&&')
