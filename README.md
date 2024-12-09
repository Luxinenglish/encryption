# File Encryption and Decryption Utility

This Python project provides a simple tool to encrypt and decrypt files or entire folders using the `cryptography` library. It ensures the security of your data by leveraging symmetric encryption with a generated key.

## Features

- **Generate Encryption Keys**: Create and save secure encryption keys.
- **Encrypt Files**: Encrypt individual files securely.
- **Decrypt Files**: Decrypt previously encrypted files.
- **Encrypt Folders**: Encrypt all files within a folder.
- **Decrypt Folders**: Decrypt all files in a folder using the same key.

## Requirements

- Python 3.6 or higher
- `cryptography` library

Install the `cryptography` library using pip:

<pre><code>pip install cryptography</code></pre>

## Usage

### Running the Script

1. Clone the repository or save the script to your local machine and open it.
   <pre><code>git clone https://github.com/Luxinenglish/encryption.git | cd encryption</code></pre>
2. Run the script in a terminal:
   <pre><code>python index.py</code></pre>

### Options

When running the script, you will be prompted to choose an option:

1. **Encrypt a Folder**: Provide the path to the folder you want to encrypt. The script generates and saves a key in `key.key`. Keep this key safe, as it is required for decryption.
2. **Decrypt a Folder**: Provide the path to the folder you want to decrypt, along with the encryption key.

### Encryption Key Management

- **Generate Key**: Automatically generated when encrypting a folder.
- **Save Key**: Saved in the file `key.key` in the current directory.
- **Load Key**: Automatically loaded from `key.key` or provided manually when decrypting.

### Example

#### Encrypting a Folder

1. Select option `1` in the menu.
2. Enter the folder path.
3. Save the displayed encryption key securely.

#### Decrypting a Folder

1. Select option `2` in the menu.
2. Enter the folder path.
3. Provide the encryption key.

## Code Overview

### Functions

- `generate_key()`: Generates a new encryption key.
- `save_key(key, filename)`: Saves the encryption key to a file.
- `load_key(filename)`: Loads the encryption key from a file.
- `encrypt_file(file_path, key)`: Encrypts a single file.
- `decrypt_file(file_path, key)`: Decrypts a single file.
- `encrypt_folder(folder_path)`: Encrypts all files in a folder.
- `decrypt_folder(folder_path, key)`: Decrypts all files in a folder using the given key.

### Main Function

The `main()` function provides a user-friendly interface to choose between encryption and decryption tasks.

## Notes

- Make sure to keep the encryption key (`key.key`) safe. Losing the key means you cannot decrypt your files.
- Always double-check the folder paths before proceeding to avoid unintentional data loss.

## License

This project is open-source and available under the MIT License. Feel free to modify and use it as per your needs.

---
**Disclaimer**: Use this tool responsibly. The developer is not responsible for any data loss or misuse.
