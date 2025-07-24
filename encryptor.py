import qrcode, urllib.parse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt(text, password):
    key = password.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(text.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted).decode()

# Example usage
plaintext = "This is a secret message!"
password = "myPass123"

encrypted_data = encrypt(plaintext, password)
url = "https://your-username.github.io/qr-decryptor/?data=" + urllib.parse.quote(encrypted_data)
qrcode.make(url).save("qr_code.png")
print("QR code generated! Scan it to open your hosted decryptor page.")
