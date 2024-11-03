from cryptography.fernet import Fernet

def load_key():
    """Load the previously generated key."""
    try:
        with open("encryption_key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Файл с ключом шифрования не найден.")
        return None

if __name__ == "__main__":
    encryption_key = load_key()
    if encryption_key:
        print(f"Encryption Key: {encryption_key.decode()}")
    else:
        print("Не удалось загрузить ключ API.")