from caesarcipher import CaesarCipher
import random



def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            pos = ord(char) - ord('A')
            pos = (pos + shift) % 26
            result += chr(pos + ord('A'))
        elif char.islower():
            pos = ord(char) - ord('a')
            pos = (pos + shift) % 26
            result += chr(pos + ord('a'))
        else:
            result += char
    
    return result




def caesar_decipher(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            pos = ord(char) - ord('A')
            pos = (pos - shift) % 26
            result += chr(pos + ord('A'))
        elif char.islower():
            pos = ord(char) - ord('a')
            pos = (pos - shift) % 26
            result += chr(pos + ord('a'))
        else:

            result += char
    
    return result



source='I want to encode this string'
print("before caesar")
print(source)
print("enter key")
key=random.randint(0,25)
print("key: ", key)
print("encrypt")
cipher = caesar_cipher('I want to encode this string',key)
string=cipher
print(cipher)
print("decrypt")
cipher = caesar_decipher(string, key)
print(cipher)


break_key=0
print("breaking key using cipher text and open text")
print("open text: ", source, "cipher text: ", string)
while(break_key<26):
    cipher=caesar_decipher(source, break_key)
    if(cipher==string):
        break
    break_key+=1

print("key is: ",break_key)

print("breaking using only cipher\n cipher text: ", string)
break_key=0
while(break_key<26):
    cipher=caesar_decipher(string, break_key)
    print("cipher text: ", string, "decoded: ", cipher, "key: ", break_key)
    break_key+=1

flag=0
print("breaking using cipher and dictionary\n cipher text: ", string)
d=dict(who='I', what='string')
print("dictionary: ",d)
words = string.split()
print(words)
number_words=len(words)
print("breaking using cipher and dictionary\n cipher text: ", string)
break_key=0
while(break_key<26):
    cipher=caesar_decipher(string, break_key)
    new_text=cipher
    print("cipher text: ", string, "decoded: ", new_text, "key: ", break_key)
    words = new_text.split()
    for i in range(number_words):
        if(words[i]==d["what"]):
            flag=1
            break
    if(flag==1):
        break
    break_key+=1

print("key: ", break_key)