
#! Easy Exercises (I started on these before the labs were posted so I just made up lists)

# ? 1. Sum the Numbers

# nums = [1, 2, 3]
# sum = 1 + 2 + 3
# print(sum)

# ? 2. Largest Number

# nums = [3, 2, 5, 4, 1]
# nums.sort()
# new_num = nums[-1:]
# print(new_num)

# ? 3. Smallest Number

# nums = [3, 2, 5, 4, 1]
# nums.sort()
# new_num = nums[:1]
# print(new_num)

# ? 4. Even Numbers

# nums = [3, 2, 5, 4, 1]
# nums.sort()
# index = 0
# while index < len(nums):
#     print(f"{nums[index + 1]}")
#     index += 2

# ? 5. Positive Numbers

# nums = [-5, 10, 3, -2, 8, 1]

# for i in nums:
#     if i > 0:
#         print(i)

# ? 6. Positive Numbers II

# nums = [-5, 10, 3, -2, 8, 1]
# j = []
# index = 0
# while index < len(nums):
#     for i in nums:
#         if i > 0:
#             j.append(i)
#             index += 1 
# print(j)

# ? 7. Multiply a List

# list = [1, 2, 3, 4, 5]
# char = 2
# index = 0
# j = []

# while index < len(list):
#     for i in list:
#         k = i * char
#         j.append(k)
#         index += 1 
# print(j)

# ? 8. Reverse a String

# str = "Hello World"
# index = 0
# reverse = ""

# while index < len(str):
#     reverse = str[index] + reverse
#     index += 1

#! Medium Exercises

#? 1. Multiply Vectors

# mult1 = [2, 4, 5]
# mult2 = [2, 3, 6]
# res = [] # should come out to [4, 12, 30]

# for i in range(0, len(mult1)):
#     res.append(mult1[i] * mult2[i])
# print(str(res))

#? 2. Matrix Addition

# result should be 6 5 3 4

# add1 = [1, 3, 2, 4]

# add2 = [5, 2, 1, 0] 

# ans = [] # result should be [6, 5, 3, 4]

# for i in range(0, len(add1)):
#     ans.append(add1[i] + add2[i])
# print(ans)

#? 3. Matrix Addition II
# * I wasn't exactly sure this is what the question was asking. Think it was wanting us to use the extend function.

# add1 = [1, 3, 2, 4]

# add2 = [5, 2, 1, 0] 

# ans = [] # result should be [6, 5, 3, 4]

# for i in range(0, len(add1)):
#     ans.append(add1[i] + add2[i])
# print(ans)

# ans.extend([7, 10, 1, 8])
# print(ans)

#? 4. De-dup

# orig_list = [7, 4, 2, 9, 1, 6, 4, 5, 4, 8, 4, 8]
# next_list = []

# print(f'Original list: {orig_list}')

# for i in orig_list:
#     if i not in next_list:
#         next_list.append(i)

# print(f'Revised list: {next_list}')

#? 5. Leetspeak

# orig_str = 'the quick brown fox jumped over the lazy dog'
# leet_list = []

# print(f'Original list: {orig_str}')

# index = 0 

# while index < len(orig_str):
#     comp = orig_str[index]
#     for i in comp:
#         if i == 'a':
#             i = '4'
#             leet_list.append(i)
#         elif i == 'e':
#             i = '3'
#             leet_list.append(i)
#         elif i == 'g':
#             i = '6'
#             leet_list.append(i)
#         elif i == 'i':
#             i = '1'
#             leet_list.append(i)
#         elif i == 'o':
#             i = '0'
#             leet_list.append(i)
#         elif i == 's':
#             i = '5'
#             leet_list.append(i)
#         elif i == 't':
#             i = '7'       
#             leet_list.append(i)
#         else:
#             leet_list.append(i)
#     index += 1

# leet_str = ''.join(leet_list)
# print(f'Leet String: {leet_str}')

#? 6. Long-long Vowels

# word = "Good"

# word_list = list(word)

# i = 1

# while i < len(word_list):
#     if word_list[i] == word_list[i - 1] and (word_list[i] == 'o' or word_list[i] == 'e'):
#         for x in range(3):
#             word_list.insert(i, word_list[i])
#         i+=4
#     else:
#         i+=1

# word = "".join(word_list)
# print(word)

#? 7. Caesar Cipher

# coded_str = "lbh zhfg hayrnea jung lbh unir yrnearq"
# decoded_str = ""

# for i in coded_str:
#     # print(ord(i) - 96 + 13)
#     if(ord(i) + 13 - 96) % 26 == 0:
#         decoded_str+=chr(96 + ord(i) + 13)
#     elif(ord(i) + 13 - 96 < 0):
#         decoded_str += " "
#     else:
#         mod = (ord(i) + 13 - 96) % 26
#         decoded_str+=chr(mod + 96)
# print(decoded_str)

