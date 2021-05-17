import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Viết hàm kiểm tra chuỗi palindrome
def is_palindrome(input):
    if input[::-1] == input:
        return True
    return False

print('is palindrome: ' + str(is_palindrome("121")))

# 2. Đọc dữ liệu từ file paper.txt 
def most_frequent_word(words):
    global number_Word 
    number_Word = dict()
    
    for word in words:
        if word in number_Word:
            number_Word[word] += 1
        else:
            number_Word[word] = 1
    return max(number_Word, key= number_Word.get)

f = open("paper.txt", encoding = 'utf-8')
content = f.read().replace('\n', ' ')
words = ''.join(e for e in content if e.isalnum() | (e == ' '))
words = [c for c in words.split(' ') if c !='']

''' 1 '''
print('word is most frequent: ' + most_frequent_word(words))

''' 2 '''
print('set() file: ' + str(set(words)))

''' 3 '''
for item in number_Word:
    print(f"{item}: {number_Word[item]}")

f.close()

# 3. Xử lý matrix
matrix = []
n = int(input("Enter the order of a square matrix: "))
def inputMaxtrix(maxtrix):
    count = 1
    for i in range(n):
        a = []
        for j in range(n):
            a.append(count)
            count += 1
        matrix.append(a)

def outputMaxtrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = " ")
        print()
    print()

def rotateMaxtrix(matrix, degrees):
    temp_matrix = []
    if degrees == 90:     
        for column in range(len(matrix)):
            temp = []
            for row in range(len(matrix)-1,-1,-1):
                temp.append(matrix[row][column])
            temp_matrix.append(temp)
    elif degrees == 180:
        for row in range(len(matrix)-1,-1,-1):
            temp = []
            for column in range(len(matrix)-1,-1,-1):
                temp.append(matrix[row][column])
            temp_matrix.append(temp)
    return temp_matrix

inputMaxtrix(matrix)
print('origin: ')
outputMaxtrix(matrix)
print('rotate 90: ')
outputMaxtrix(rotateMaxtrix(matrix, 90))
print('rotate 180: ')    
outputMaxtrix(rotateMaxtrix(matrix, 180))

# 4.  Xử lý file csv (sử dụng pandas)
f = pd.read_csv('Car_sales.csv')
print("Câu 4a: 20 bản ghi đầu là:")
row20 = f.head(20)
print(row20)

print("Câu 4b: Tính tổng Sales_in_thousands theo Manufacturer: ")
grouped = row20.groupby(by="Manufacturer")
print(grouped['Sales_in_thousands'].agg([np.sum]))

# Cau 4c:
f = pd.read_csv('Car_sales.csv')
choose = f[f["Manufacturer"] == 'Chevrolet']
print(choose)
x = choose[['Model']].values
x_val = []
for i in range(len(x)):
    temp = str(x[i]).strip("[]' ")
    x_val.append(temp)

y_val = []
y = choose[['Sales_in_thousands']].values
for i in range(len(y)):
    temp = float(str(y[i]).strip("[]' "))
    y_val.append(temp)

plt.figure(figsize=(10,5))
plt.bar(x_val, y_val, color="blue")
plt.title("Câu 4c. Đồ thị dạng cột phân bố của hãng 'Chevrolet' theo từng model với thuộc tính 'Sales_in_thousands'")
plt.xlabel('Model')
plt.ylabel('Sales_in_thousands')
plt.show()