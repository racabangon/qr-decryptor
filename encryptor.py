import qrcode
import urllib.parse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt(text, password):
    key = password.ljust(16)[:16].encode()  # AES needs 16-byte key
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(text.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted).decode()

# Input text and password
plaintext = "This is a secret message!"
password = "myPass123"

# Encrypt text and build URL
encrypted_data = encrypt(plaintext, password)
url = "https://rcabangon.github.io/qr-decryptor/?data=" + urllib.parse.quote(encrypted_data)

# Create and save QR code
img = qrcode.make(url).get_image()
img.save("qr_code.png")

print("✅ QR code saved as 'qr_code.png'")
print("🔗 URL:", url)
