import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates an encryption key."""
    return Fernet.generate_key()

def save_key(key, filename="key.key"):
    """Saves the key to a file."""
    try:
        with open(filename, "wb") as key_file:
            key_file.write(key)
    except IOError as e:
        print(f"Error saving the key: {e}")

def load_key(filename="key.key"):
    """Loads a key from a file."""
    try:
        with open(filename, "rb") as key_file:
            return key_file.read()
    except IOError as e:
        print(f"Error loading the key: {e}")
        return None

def encrypt_file(file_path, key):
    """Encrypts a file."""
    fernet = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
    except IOError as e:
        print(f"Error encrypting the file {file_path}: {e}")

def decrypt_file(file_path, key):
    """Decrypts a file."""
    fernet = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
    except IOError as e:
        print(f"Error decrypting the file {file_path}: {e}")
    except Exception as e:
        print(f"Error decrypting the data in the file {file_path}: {e}")

def encrypt_folder(folder_path):
    """Encrypts all files in a folder."""
    key = generate_key()
    save_key(key)
    print(f"Encryption key: {key.decode()}")
    for root, _, files in os.walk(folder_path):
        for file in files:
            encrypt_file(os.path.join(root, file), key)

def decrypt_folder(folder_path, key):
    """Decrypts all files in a folder using a key."""
    try:
        fernet = Fernet(key)
    except ValueError as e:
        print(f"Invalid decryption key: {e}")
        return False

    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                decrypt_file(os.path.join(root, file), key)
        print("Decryption completed.")
        return True
    except Exception as e:
        print(f"Error during decryption: {e}")
        return False

def main():
    print("1. Encrypt a folder")
    print("2. Decrypt a folder")
    choice = input("Choose an option (1/2): ")
    folder_path = input("Folder path: ")

    if choice == "1":
        encrypt_folder(folder_path)
    elif choice == "2":
        key = input("Enter the decryption key: ").encode()
        decrypt_folder(folder_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()