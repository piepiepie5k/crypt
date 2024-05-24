import random
def generate_file(filename):
    # Открываем файл для записи
    with open(filename, 'w') as file:
        # Создаем байтовый объект с символами от 0 до 255
        for i in range(64):
            file.write(str(random.randint(0, 9)))



def read_text_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return ""
    except IOError:
        print(f"Ошибка при чтении файла {filename}.")
        return ""


def vernam_encrypt(plaintext, key):
    # Преобразуем текст и ключ в байтовые строки
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')

    # Применяем операцию XOR к каждому байту текста и ключа
    encrypted_bytes = bytes(p ^ k for p, k in zip(plaintext_bytes, key_bytes))

    # Возвращаем зашифрованный текст в виде строки
    return encrypted_bytes.hex()  # Представляем байты в виде строки шестнадцатеричных символов

def vernam_decrypt(ciphertext, key):
    # Преобразуем ключ в байтовую строку
    key_bytes = key.encode('utf-8')

    # Преобразуем зашифрованный текст из шестнадцатеричной строки обратно в байты
    encrypted_bytes = bytes.fromhex(ciphertext)

    # Применяем операцию XOR к каждому байту зашифрованного текста и ключа
    decrypted_bytes = bytes(p ^ k for p, k in zip(encrypted_bytes, key_bytes))

    # Возвращаем дешифрованный текст в виде строки
    return decrypted_bytes.decode('utf-8','ignore')

def generate(filename,text):
    # Открываем файл для записи
    with open(filename, 'w') as file:
            file.write(text)




filename='text.txt'
text=read_text_from_file(filename)
#text_bin=''.join(format(ord(i), '08b') for i in text)
filename='key.txt'
key=read_text_from_file(filename)
res = vernam_encrypt(text, key)
print(res)
filename='output.txt'
generate(filename, res)
res=vernam_decrypt(res, key)
print(res)
#key_bin=''.join(format(ord(i), '08b') for i in key)
#print(text)
#print(text_bin)
#print(key)
#print(key_bin)
#print(bin(text_bin)^bin(key_bin))
#filename='key.txt'
#generate_file(filename)



