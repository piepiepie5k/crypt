from caesarcipher import CaesarCipher
import random
source='I want to encode this string'
print("before caesar")
print(source)
print("enter key")
key=random.randint(0,25)
print("key: ", key)
print("encrypt")
cipher = CaesarCipher('I want to encode this string', offset=key)
string=cipher.encoded
print(cipher.encoded)
print("decrypt")
cipher = CaesarCipher(string, offset=key)
print(cipher.decoded)


break_key=0
print("breaking key using cipher text and open text")
print("open text: ", source, "cipher text: ", cipher.encoded)
while(break_key<26):
    cipher=CaesarCipher(source, offset=break_key)
    if(cipher.encoded==string):
        break
    break_key+=1

print("key is: ",break_key)

print("breaking using only cipher\n cipher text: ", string)
break_key=0
while(break_key<26):
    cipher=CaesarCipher(string, offset=break_key)
    print("cipher text: ", string, "decoded: ", cipher.encoded, "key: ", break_key)
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
    cipher=CaesarCipher(string, offset=break_key)
    new_text=cipher.encoded
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