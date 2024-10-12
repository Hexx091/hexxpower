
from cryptography.fernet import Fernet
import subprocess

# Kunci enkripsi, disimpan dengan aman
key = b'Ff6whYf1Sngpl9ZwhzKl88mHrhOISZoYJ5XyJ0iJSXI='
cipher_suite = Fernet(key)

# Password 'warpower1520' yang telah dienkripsi
encrypted_password = b'gAAAAABlYGBjMH8kq36MejZts9EqWxg1AbCkPeRLFdIQVBB4dS6R7JxW2lpNEUjPL-1MjUihHSc8FAFvd3smHne1sQWvAQZ-7g=='

def check_password(input_password):
    # Dekripsi password dan bandingkan dengan input pengguna
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return input_password == decrypted_password

def run_test2():
    # Menjalankan skrip test2.py setelah otentikasi berhasil
    subprocess.run(["python3", "test2.py"])

if __name__ == "__main__":
    password = input("Enter password to access test2.py: ")
    if check_password(password):
        print("Access granted.")
        run_test2()
    else:
        print("Access denied. Incorrect password.")
