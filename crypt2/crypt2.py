import math
import random
def count_character_frequencies(text):
    # Создаем пустой словарь для хранения частот
    frequencies = {}

    # Проходим по каждому символу в тексте
    for char in text:
        # Если символ уже есть в словаре, увеличиваем его частоту на 1
        if char in frequencies:
            frequencies[char] += 1
        # Если символа нет в словаре, добавляем его с частотой 1
        else:
            frequencies[char] = 1

    return frequencies



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
    

def entropy(dictionary,total_freq):
    sum=0
    for char, freq in dictionary.items():
        sum=sum+(freq/total_freq) * math.log2(freq/total_freq)
    sum=sum*-1
    return sum

def count_character_frequencies_generate_text(text):
    # Создаем пустой словарь для хранения частот
    frequencies = {}
    words=text.split()
    # Проходим по каждому символу в тексте
    for word in words:
        # Если символ уже есть в словаре, увеличиваем его частоту на 1
        if word in frequencies:
            frequencies[word] += 1
        # Если символа нет в словаре, добавляем его с частотой 1
        else:
            frequencies[word] = 1

    return frequencies


def generate_file_with_all_characters(filename):
    # Открываем файл для записи
    with open(filename, 'w') as file:
        # Создаем байтовый объект с символами от 0 до 255
        for i in range(random.randint(1,512)):
            file.write(str(random.randint(0, 33)))
            file.write(' ')

def log_entropy(filename):
    text = read_text_from_file(filename)
    frequencies_gen = count_character_frequencies_generate_text(text)
    total_freq=0
    for word, freq in frequencies_gen.items():
        total_freq=total_freq+freq
        #print(f"'{word}': {freq}")
    print("Всего разных символов (алфавит): ", len(frequencies_gen))
    print("Всего символов: ", total_freq)
    ent=entropy(frequencies_gen, total_freq)
    print("Энтропия: ", ent)
    print("log2(размер алфавита): ", math.log2(len(frequencies_gen)))



filename = 'text.txt'
text = read_text_from_file(filename)
#text = "Привет, мир!"
frequencies = count_character_frequencies(text)

# Выводим частоты символов
del frequencies[' ']
total_freq=0
for char, freq in frequencies.items():
    total_freq=total_freq+freq
    print(f"'{char}': {freq}")



print("Всего разных символов(алфавит): ", len(frequencies))
print("Всего символов: ", total_freq)
ent=entropy(frequencies, total_freq)
print("Энтропия: ", ent)

#filename = '33_alph.txt'

#generate_file_with_all_characters(filename)

#print("Файл {filename} успешно создан.")

print("считаем генерацию, файл где везде 0")
filename = 'zeroes.txt'
log_entropy(filename)
print("считаем генерацию, файл где 0 и 1")
filename = 'zeroes_ones.txt'
log_entropy(filename)
print("считаем генерацию, файл где от 0 до 33")
filename = '33_alph.txt'
log_entropy(filename)
print("считаем генерацию, файл где от 0 до 255")
filename = 'all_characters.txt'
log_entropy(filename)
#text = read_text_from_file(filename)
#frequencies_gen = count_character_frequencies_generate_text(text)
#total_freq=0
#for word, freq in frequencies_gen.items():
#    total_freq=total_freq+freq
#    print(f"'{word}': {freq}")


