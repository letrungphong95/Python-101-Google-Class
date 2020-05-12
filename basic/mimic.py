#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

""" [TODO] Hello Quỳnh Anh, lại là Phong đây. Bài này vẫn có các vấn đề là:
(1) Quỳnh Anh chưa dùng hết công hiệu khi define 1 function trong python 
(2) Chưa hiểu được requirements
(3) Vẫn chạy bằng cách gọi lại function `mimic_dict('small.txt')` chứ chưa chạy script bằng cách truyền các 
tham số từ bên ngoài vào như yêu cầu của bài toán

-> Solution:
(1) Define 1 function đọc file để trả về 1 dict với key là các words có trong text file còn value tương ứng 
là các từ theo sau word đó có trong text file. 
(2) Bài này sẽ có 2 yêu cầu 
+ Yêu cầu 1 là build 1 cái mimic dict, gồm các key là các words có trong text file, và value của mỗi key đó 
là các từ mà theo sau word đó trong đoạn văn của text file 
+ Từ cái mimic dict ở trên, tạo 1 đoạn văn (200 chữ) bất kỳ. Ban đầu sẽ chọn 1 từ bất kỳ, có thể là empty string như ' ' 
sau đó sẽ tra vào mimic dict để random chọn từ đứng sau của từ ban đầu -> sẽ được từ thứ 2, rồi lại random chọn các từ tiếp theo từ 
thứ 2 để được từ thứ 3... tới từ thứ 200 thì dừng. Khi nào mà không có từ đứng sau, thì sẽ reset về empty string ''
"""

""" QA's code 
"""
# def mimic_dict(filename): # TODO Đặt tên function phải là động từ, tên biến phải là danh từ
#   # Open input file
#   input_file = open(filename, "r")
#   read_file = input_file.read()
  
# # Split on all whitespaces
#   splitted_list = read_file.split()

# # Mapping
#   mimic_dict = {} # TODO Không được đặt tên biến trùng với function 
#   for item in range(len(splitted_list)-1):
#     if splitted_list[item] not in mimic_dict.keys():
#       mimic_dict[splitted_list[item]] = [splitted_list[item+1]]
#     else:
#       mimic_dict[splitted_list[item]] += [splitted_list[item+1]]
#   print(mimic_dict)
  
# mimic_dict('small.txt')


# def print_mimic(mimic_dict, word):
#   """Given mimic dict and start word, prints 200 random words."""
#   # +++your code here+++
#   return
#   # I gave up. Couldn't understand what the requirement was

""" [TODO] Phong's code
"""
def mimic_dict(filename):
  """ Function này để đọc file và trả về 1 mimic dict
  """
  with open(filename, 'r') as f:
    all_data = f.read()
    all_words = all_data.split()
  # Mapping 
  mimic_dict_result = {}
  key_word = ''
  for after_word in all_words:
    if key_word in mimic_dict_result:
      mimic_dict_result[key_word].append(after_word) 
    else:
      mimic_dict_result[key_word] = [after_word]
    key_word = after_word
  return mimic_dict_result

def print_mimic(mimic_data, word):
  """ Function này để random 1 cái đoạn 200 từ 
  """
  context = ''
  for i in range(200):
    text = random.choice(mimic_data[word]) 
    text = text if text != None else ''
    context = context + ' ' + text 
    word = text
  print(context)

""" [TODO] Đây cũng là lỗi thứ 3 do Quỳnh Anh chưa biết chạy script truyền từ bên ngoài theo yêu cầu của họ 
`
if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)
`
nên mình sẽ truyền tên file từ bên ngoài vào lun, để chạy bài này thì dùng script này 
`python3 ./mimic.py alice.txt`
"""
# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
