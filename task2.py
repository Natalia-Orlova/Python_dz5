# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from os import path
from itertools import groupby

def rle_encode(text, text_code):
    if path.exists(text) and path.exists(text_code):
        with open(text) as text1, open (text_code, 'a') as text2:
            for i in text1:
                text2.write ("".join([f"{len(list(v))}{char}" for char, v in groupby(i)]))
    else:
        print("Файл с таким именем отсутствует в системе")
               
def rle_decode(file_name):
    if path.exists(file_name):
        with open (file_name) as file:
            count = ''
            res = ''
            for k in file:
                 for j in k.strip():
                    if j.isdigit():
                        count += j
                    else:
                        res += int(count) * j
                        count = ''
            return res
    else:
        print("Файл с таким именем отсутствует в системе")


rle_encode(input("Введите имя файла с текстом: "), \
     input("Введите имя файла для сжатия данных: "))
print(rle_decode(input("Введите имя файла для декодирования: ")))
