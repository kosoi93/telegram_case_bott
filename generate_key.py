from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()

# Сохранение ключа в файл
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

print("Ключ шифрования сгенерирован и сохранён в файл 'encryption_key.key'.")
