# qr_encryptor.py
from Crypto.Cipher import AES
import base64
import qrcode
import urllib.parse

def pad(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
def unpad(s): return s[:-ord(s[-1])]

def encrypt(text, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(text).encode())
    return base64.b64encode(ct).decode()

def decrypt(encoded, key):
    try:
        key = key.ljust(16)[:16].encode()
        cipher = AES.new(key, AES.MODE_ECB)
        decoded = base64.b64decode(encoded)
        return unpad(cipher.decrypt(decoded).decode())
    except:
        return "[Invalid password or corrupted data]"

if __name__ == "__main__":
    mode = input("Mode (E)ncrypt or (D)ecrypt? ").strip().lower()
    if mode == "e":
        secret = input("Enter the secret info: ")
        password = input("Enter password: ")
        encrypted = encrypt(secret, password)
        print(f"\nEncrypted (Base64):\n{encrypted}\n")

        # Generate full URL to online decryptor
        encoded_url = urllib.parse.quote(encrypted)
        full_url = f"https://rcabangon.github.io/qr-decryptor/?data={encoded_url}"
        print(f"🔗 Decryption URL: {full_url}")

        # Generate QR
        img = qrcode.make(full_url).get_image()
        img.save("secret_qr.png")
        print("✅ QR code saved as secret_qr.png")

    elif mode == "d":
        encrypted = input("Paste the encrypted Base64 text: ")
        password = input("Enter password: ")
        decrypted = decrypt(encrypted, password)
        print(f"\nDecrypted:\n{decrypted}")
