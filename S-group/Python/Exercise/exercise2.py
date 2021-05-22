import math
import requests
import json

# # 1. Bai Tuong
# class DownloadCovidInfo:
#     __url = ""
#     def __init__(self, url = "https://api.covid19api.com/summary"):
#         self.__url = url

#     def get_all_data(self):
#         try:
#             response = requests.get(self.__url)
#             response.raise_for_status()
#             print(response.status_code)
#         except requests.HTTPError as http_err:
#             print(f'HTTP error occurred: {http_err}')
#         except Exception as err:
#             print(f'Other error occurred: {err}')
#         else:
#             print('Successfull Get Request')
#             # response.content
#             # response.text
#             return response.json()
            
#     def get_data_by_country(self, Country):
#         for country in self.get_all_data()['Countries']:
#             if Country.lower() == country['Country'].lower():
#                 return country

#     def save_to_file(self, file):
#         data = self.get_all_data()
#         with open(''.join([file, '.json']), "w") as f:
#             json.dump(data, f, indent=4)

#     @property
#     def url(self):
#         return self.__url
#     @url.setter
#     def url(self, url):
#         self.__url = url

# a = DownloadCovidInfo()

# print(a.url)
# print(a.get_all_data())
# print(a.get_data_by_country('viet nam'))
# a.save_to_file("CovidData")

# # 2. Tính sum của các phần tử trong mảng
# nums = [1, 2, 3, 4]

# def sum(nums):
#     for i in range(len(nums)):
#         if i != 0:
#             nums[i] += nums[i-1]
#     return nums

# print(sum(nums))

# 3. Super palindrome: 
# def checkPalindrome(num):
#     if str(num)[::-1] == str(num):
#         return True
#     return False


# def superPalindrome(left, right):
#     for i in range(left, right+1):
#         if math.sqrt(i) % 1 == 0:
#             if checkPalindrome(num) and checkPalindrome(int(math.sqrt(i))):
#                 nums.append(i)
#                 print('sss')

# left = int(input('Left : '))
# right = int(input('Right : '))

# nums = []
# superPalindrome(left, right)
# print(nums)

# 4. Dùng class tạo cấu trúc dữ liệu danh sách liên kết đơn với value của mỗi node là giá trị số

class Node():
    def __init__(self, value = None, next = None):
        self.data = value 
        self.next = next 
    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add_node(self, data):
        if self.first == None:
            self.first = Node(data)
            self.last = self.first
        elif self.first == self.last:
            self.last = Node(data)
            self.first.next = self.last
        else:
            current = Node(data)
            self.last.next = current
            self.last = current
        self.size += 1

    def findMiddle(self):
        index = 0
        if self.size % 2 == 0:
            index = int(self.size/2)
        else:
            index = int(self.size/2 + 1)
        middle = self.first
        for i in range(index - 1):
            middle = middle.next
        return middle.data

    def translate(self, units):
        for i in range(units):
            self.last.next = self.first
            self.first = self.last
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            self.last = temp
            temp.next = None

    def __str__(self):
        node = self.first
        out = []
        while(node):
            out.append(str(node.data))
            node = node.next
        out = '->'.join(out)
        return out

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(6)
# print linkedlist
print(ll)
# a. find middle node
print(ll.findMiddle())
# b. translate to right 2 units
ll.translate(2)
print(ll)