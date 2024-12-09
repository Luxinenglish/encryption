import os
from cryptography.fernet import Fernet

def generate_key():
    """Génère une clé de chiffrement."""
    return Fernet.generate_key()

def save_key(key, filename="key.key"):
    """Sauvegarde la clé dans un fichier."""
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="key.key"):
    """Charge une clé depuis un fichier."""
    with open(filename, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    """Encrypte un fichier."""
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Décrypte un fichier."""
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path):
    """Encrypte tous les fichiers dans un dossier."""
    key = generate_key()
    save_key(key)
    print(f"Clé de chiffrement : {key.decode()}")
    for root, _, files in os.walk(folder_path):
        for file in files:
            encrypt_file(os.path.join(root, file), key)

def decrypt_folder(folder_path, key):
    """Décrypte tous les fichiers dans un dossier avec une clé."""
    fernet = Fernet(key)
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                decrypt_file(os.path.join(root, file), key)
        print("Décryptage terminé.")
    except Exception as e:
        print(f"Erreur lors du décryptage : {e}")

def main():
    print("1. Encrypter un dossier")
    print("2. Décrypter un dossier")
    choice = input("Choisissez une option (1/2) : ")
    folder_path = input("Chemin du dossier : ")
    
    if choice == "1":
        encrypt_folder(folder_path)
    elif choice == "2":
        key = input("Entrez la clé de décryptage : ").encode()
        decrypt_folder(folder_path, key)
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
