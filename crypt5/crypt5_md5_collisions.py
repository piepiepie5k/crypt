import math

rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

constants = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
            16*[lambda b, c, d: (d & b) | (~d & c)] + \
            16*[lambda b, c, d: b ^ c ^ d] + \
            16*[lambda b, c, d: c ^ (b | ~d)]

index_functions = 16*[lambda i: i] + \
                  16*[lambda i: (5*i + 1)%16] + \
                  16*[lambda i: (3*i + 5)%16] + \
                  16*[lambda i: (7*i)%16]

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

def md5(message):

    message = bytearray(message) #copy our input into a mutable buffer
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message)%64 != 56:
        message.append(0)
    message += orig_len_in_bits.to_bytes(8, byteorder='little')

    hash_pieces = init_values[:]

    for chunk_ofst in range(0, len(message), 64):
        a, b, c, d = hash_pieces
        chunk = message[chunk_ofst:chunk_ofst+64]
        for i in range(64):
            f = functions[i](b, c, d)
            g = index_functions[i](i)
            to_rotate = a + f + constants[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
            new_b = (b + left_rotate(to_rotate, rotate_amounts[i])) & 0xFFFFFFFF
            a, b, c, d = d, new_b, b, c
        for i, val in enumerate([a, b, c, d]):
            hash_pieces[i] += val
            hash_pieces[i] &= 0xFFFFFFFF
    
    return sum(x<<(32*i) for i, x in enumerate(hash_pieces))
        
def md5_to_hex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

def check_partial_collision(message1, message2):
    hash1 = md5_to_hex(md5(message1))
    hash2 = md5_to_hex(md5(message2))
    result1 = bytes.fromhex(hash1)
    #for byte in result1:
    #    print(byte)
    result2=bytes.fromhex(hash2)
    #for byte in result2:
    #    print(byte)
    
    print(len(result1))
    print(len(result2))
    counter=0
    for i in range(16):
        if(result1[i]==result2[i]):
            counter+=1
    return counter


if __name__=='__main__':
    message1 = b"Hello"
    message2 = b"owl"  
    message3 = b"Hello"  
    message4 = b"hell"
    print(md5_to_hex(md5(message1)),' <= "',message1.decode('ascii'),'"', sep='')
    print(md5_to_hex(md5(message2)), ' <= "', message2.decode('ascii'), '"', sep='')   
    counter=check_partial_collision(message1, message2)
    if(counter>0):
        print('коллизия message1 message2, байтов:', counter)
    else:
        print('нет коллизии message1 message2')
    counter=check_partial_collision(message1, message3)
    if(counter>0):
        print('коллизия message1 message3, байтов:', counter)
    else:
        print('нет коллизии message1 message3')
    counter=check_partial_collision(message1, message4)
    if(counter>0):
        print('коллизия message1 message4, байтов:', counter)
    else:
        print('нет коллизии message1 message4')
    