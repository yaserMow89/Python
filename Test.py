
# test_dict = {}

# text = "thIs is a bookaIIIsaIIssat"

# for char in text:
#     if char.isalpha():
#         if char.lower() in test_dict:
#             test_dict[char.lower()] += 1
#         else:
#             test_dict[char.lower()] = 1


# text = "this is a book"
# print (text[:2])

# for key, value in test_dict.items():
#     print ("val is {} and key is {}".format(value,key))

# new_dict = {'l': '9.06', 'o': '6.37', 'j': '10.7', 'u': '2.01', 'm': '5.70', 
# 'y': '7.71', 'e': '4.02', 'p': '5.03', 'd': '9.06', 'v': '4.02', 'q': '2.68',}

# print(new_dict.items())



nums = [2,7,11,15]
target = 17
index_list = []
for x in nums:
    for y in nums:
        if x+y == target:
            index_list.append(nums.index(x))
            # index_list.append(nums.index(y))
            
print(index_list)