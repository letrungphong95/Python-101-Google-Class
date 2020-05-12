#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

"""
[TODO]
Bài wordcount.py này QA bị các lỗi cơ bản như sau ha: 
(1) Chưa sử dụng hết được lợi ích khi define 1 function 
(2) Chưa biết cách chạy 1 script(chạy từ lệnh bên ngoài bằng cửa sổ terminal) khi truyền 1 argument 
từ bên ngoài vào 
Cụ thể mắc lỗi ở đâu thì cùng đi xuống dưới ha, rồi Phong sẽ trình bày bài giải ở dưới
"""

"""
[TODO] Lỗi thứ (1): Lỗi này là chưa dùng hết công dụng của 1 function. Mục dích define 1 function 
là để có thể thực hiện 1 task nào đó, và trả về 1 kết quả mong muốn. Tất cả các process, variables trong function
sẽ chỉ tồn tại trong function, sau khi thực hiện xong function thì sẽ bị xóa, chỉ lưu lại kết quả trả về. Và đặc biệt
function có thể được dùng lại nhiều lần, để đỡ mất công viết code thực hiện các task vụ đó.
Cú pháp define 1 function 

```
def do_something(name=None):
  # Do some processing

  return (name + ' is handsome')
```

result1 = do_something('Phong')
result2 = do_something('Quynh Anh')

-> Vì vậy ở đây, cùng 1 việc mở file, QA lại phải define lại 2 lần trong 2 function khác nhau, khá mất công,
Phong sẽ refactor lại code như sau. 
"""

""" QA's code
"""
# def print_words(filename):
#   # Open input file:
#   input_file = open(filename, "r") # TODO: tên biến bị sai, không được động từ, bị khá nhiều ở dưới
#   read_file = input_file.read() # TODO: tương tự tên biến
  
#   # Split on all whitespaces
#   splitted_list = read_file.split()

#   # Lowercase all characters
#   final_list = []
#   for word in splitted_list:
#     final_list.append(word.lower())

#   # Count characters' numbers of appearances
#   dict_count = {}
#   for word in final_list:
#     if word not in dict_count:
#       dict_count[word] = 1
#     else:
#       dict_count[word] += 1
  
#   # # Sort dict
#   sorted_count = sorted(dict_count.keys())
#   for word in sorted_count:
#     print(word + " " + str(dict_count[word]))
  

# # Print top 20 characters:
# def print_top(filename):
#   # Open input file:
#   input_file = open(filename, "r")
  
#   # Split on all whitespace
#   splitted_list = []
#   for line in input_file:
#     splitted_list += line.split()

#   # Lowercase all characters
#   final_list = []
#   for word in splitted_list:
#     final_list.append(word.lower())

#   # Count characters' numbers of appearances
#   dict_count = {}
#   for word in final_list:
#     if word not in dict_count:
#       dict_count[word] = 1
#     else:
#       dict_count[word] += 1
  
#   # Sort dict
#   def get_value(dictionary):
#     return dictionary[1]
#   sorted_count = sorted(dict_count.items(), key = get_value, reverse = True)
  
#   # Print top 20
#   for word in sorted_count[:20]:
#     print(word[0] + " " + str(word[1]))


""" [TODO]
Phong's code 
"""
def read_file(filename=None):
  """ Ở đây Phong sẽ define 1 function read_file và trả về 1 dict các từ có trong file với số lần xuất hiện lun, để đọc txt file và dùng cho cả 2 function con 
  bên dưới, đỡ phải viết lại cái read file
  """
  # Nên đọc file theo cách with open... này để file có thể được close lun, ko gây tràn bộ nhớ
  with open(filename, 'r') as f:
    text_data = f.read()
    all_words = text_data.split()

  # Lowercase all characters
  lower_words = [word.lower() for word in all_words]

  # Count characters' numbers of appearances
  dict_count = {}
  for word in lower_words:
    if word not in dict_count:
      dict_count[word] = 1
    else:
      dict_count[word] += 1
  
  return dict_count

def print_words(filename):
  """ Vì function này chỉ để in data, nên Phong chỉ cần gọi lại function read_file để đọc data, và in hết kết quả ra thôi ngen
  """
  # all_data là cái dict_count trả về, và Phong truyền vào 1 biến là filename như define của function read_file để cho function read_file thực thi
  all_data = read_file(filename)
  # Giờ chỉ việc in thôi 
  sorted_data = sorted(all_data.keys())
  for word in sorted_data:
    print(word + " " + str(all_data[word]))

  # Trả về không gì cả, có dòng này cũng được, không có cũng được, vì function này chỉ để in 
  return 

# Print top 20 characters:
def print_top(filename):
  """ Đây là bài print top, và vì đã define read_file function nên mình không cần đọc lại file và xử lý data cho ra dict_count, chỉ việc 
  gọi để function thực thi và lấy giá trị trả về
  """
  all_data = read_file(filename)
  # Sort dict
  def key_fn(s):
    return s[1]
  sorted_count = sorted(all_data.items(), key = key_fn, reverse = True)
  
  # Print top 20
  for word in sorted_count[:20]:
    print(word[0] + " " + str(word[1]))

  return

""" ==> Do Phong comment nhiều, chớ nhìn nó gọn code và chuyên nghiệp hơn đúng không, mình chia nhỏ để dễ quản lý, debug, và reuse đc nhiều lần function. 
Lần sau chú ý hen !!! 
"""


""" [TODO] Lỗi thứ (2) 
Đây là lỗi Quỳnh Anh không hiểu rõ cách chạy 1 script, ngoài việc `python3 run.py` mình vẫn có thể điều khiển chương trình chạy bên trong bằng cách thêm các
argument, flag từ bên ngoài... eg `python3 run.py --count` hoặc `python3 run.py --topcount`
ở trong main() họ có nói 
`
if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)
`
-> Nghĩa là mình có thể chạy `python3 ./wordcount.py --count` sẽ chạy ra kết quả bài print_words 
Hoặc `python3 ./wordcount.py --topcount` sẽ chạy ra kết quả bài print_top 
Vì vậy mình không cần phải khai báo nó ra như Quỳnh Anh làm ở bên dưới. 
"""  
print_words("alice.txt")  
print_top("alice.txt")


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)
  """ [TODO] Hello Quỳnh Anh
  Ở đây có 1 package là sys.argv, để hiểu cách truyền arguments từ bên ngoài của script, và cái khai báo option bên dưới
  là để lấy cái arguments mà Quỳnh Anh truyền vào.
  + sys.argv[1] sẽ là vị trí đầu tương đương option --count hoặc --topcount
  + sys.argv[2] sẽ là vị trí thứ 2 tương đương filename mà Quỳnh Anh chạy vào, và code dưới nó sẽ xét điều kiện để chạy 2 function
  print_words với print_top cho Quỳnh Anh
  Ví dụ:
  * Nếu chạy `python3 ./wordcount.py --count alice.txt` sẽ in ra kết quả bài print_words 
  * Nếu chạy `python3 ./wordcount.py --topcount alice.txt` sẽ in ra kết quả bài print_top
  Còn nếu không truyền vào gì chỉ chạy `python3 ./wordcount.py` thì như code bên dưới nó sẽ in ra `unknown option...`
  """
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
