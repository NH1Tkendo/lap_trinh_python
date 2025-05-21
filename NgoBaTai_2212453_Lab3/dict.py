# #Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# a = dict()
# for i in range(len(keys)):
#     a[keys[i]] = values[i]
# print(a)

# res_dict = dict(zip(keys, values))
# print(res_dict)
#----------------------------------------------------------------------------------
#Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1, **dict2}
# print(dict3)
#----------------------------------------------------------------------------------
#Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])
#----------------------------------------------------------------------------------
#Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res = dict.fromkeys(employees, defaults)
# print(res)
#----------------------------------------------------------------------------------
#Create a dictionary by extracting the keys from a given dictionaryCreate a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# res = dict()
# for k in keys:
#     res.update({k: sample_dict[k]})

# newDict = {k: sample_dict[k] for k in keys}
# print(res)
#------------------------------------------------------------------------------
#Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# Keys to remove
# keys = ["name", "salary"]
# res = {f: sample_dict[f] for f in sample_dict.keys() - keys}
# print(res)
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)
#------------------------------------------------------------------------------
#Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')
#------------------------------------------------------------------------------
#Rename key of a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
#------------------------------------------------------------------------------
#Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict, key = sample_dict.get))
#------------------------------------------------------------------------------
#Change value of a key in a nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)


#1. In value khác biệt trong dict
# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}

# res = list({ele for val in test_dict.values() for ele in val})
# print(res)

#2. Python program to find the sum of all items in a dictionary
# a = {'a': 3,
#      'b': 7,
#      'c': 10}

# def returnSum(dict):
#     return sum(dict.values())

# def tinhTong():
#     tong = 0
#     for i in a.values():
#         tong+= i
#     return tong

# print(tinhTong())

#3. Remove key 
# test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
# removed_value = test_dict.pop('Mani')#pop
# print(removed_value)
# new_dict = {key: val for key, val in test_dict.items() if key != 'Mani'}#dict comprehension
#del test_dict['Mani']#del

#4. Merging or Concatenating two Dictionaries in Python
#dùng update
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}

# d1.update(d2)#dùng phương thức update
# d3 = d1 | d2 #dùng toán tử |
# print(d1)

#5. sắp xếp dùng itemgetter() và lambda
# from operator import itemgetter
# data_list = [{"name": "Nandini", "age": 20},
#              {"name": "Manjeet", "age": 20},
#              {"name": "Nikhil", "age": 19}]
# print(sorted(data_list, key = itemgetter('age')))
# print(sorted(data_list, key= lambda i: i['age']))

#6. Convert key-values list to flat dictionary = dùng hàm dict()

#7. Insertion at the beginning in OrderedDict
# from collections import OrderedDict

# iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# iniordered_dict.update({'manjeet' : '3'})
# iniordered_dict.move_to_end('manjeet', last=False)