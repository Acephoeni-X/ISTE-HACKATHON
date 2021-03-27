from Crypto.Cipher import AES
import base64
import os

def decrypt(encryptedString):
    PADDING = '&'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    key = 'Rishi2002'.ljust(16, '&')
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    print(str(decoded).replace('&', ''))

# # def decrypt(enc ):
# #         enc = base64.b64decode(enc)
# #         iv = enc[:16]
# #         
# #         cipher = AES.new(key, AES.MODE_CBC, iv )
# #         print(cipher.decrypt(enc))


decrypt('pkMl/h3pbVjG5+bcnkArft6M80w/A4CdxK9RcHu7KeGYWe666BgKtTUaFiEDcak43OKki2LyguO7IMkjYN1Si9zipIti8oLjuyDJI2DdUovc4qSLYvKC47sgySNg3VKL3OKki2LyguO7IMkjYN1Si9zipIti8oLjuyDJI2DdUos=')
