#Q1) WRITE A PYTHON PROG TO CALCULATE LENGTH OF A STRING
s="Hello"
print(len(s))


#Q2) Sum of elements of a list
l=[1,2,3,4,5]
print(type(l))
sum=0
for x in l:
    sum=sum+x
print("Sum of list :",sum)


# 3. Write a Python program to multiplies all the items in a list. Go to the editor
mul=1
for x in l:
    mul=mul*x
print("Multiplication of all elements of list :",mul)


# 4. Write a Python program to get the largest number from a list. Go to the editor
a=[2,4,1,3]
mx=a[0]
for x in a:
    if mx<x:
        mx=x
print("Largest number is ",mx)


# 5. Write a Python program to get the smallest number from a list. Go to the editor
a=[2,4,1,3]
max=a[0]
for x in a:
    if max>x:
        max=x
print("smallest number is ",max)



# 7. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
def char_frequency(str):
    dict={}
    for x in str:
        keys=dict.keys()
        if x in keys:
            dict[x]=dict[x]+1
        else:
            dict[x]=1
    return dict

s=input("Enter the string whose char freq is to be found: ")
print(char_frequency(s))




# 8. Write a Python program to count the number of strings where the string length is 2 or more and 
# the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
s=['abc','xyz','aba','1221']
count=0
for x in s:
    if len(x)>=2 and x[0]==x[-1]:
        count+=1
print("There are ",count," strings in the list with length > 2 and fist & last elements are same")
        



# 9. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# 10. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
def str_cond(str):
    if len(str)<2:
        print("Empty String")

    else:
        str2=str[0]+str[1]+str[-2]+str[-1]
    return str2

s=input("10) Enter the string :")
print(str_cond(s))


# 11. Write a python program to get a string from a given string where all occurrences of its first char is changed to $, except the first
# sample: 'restart'
# output: resta$t
str=input("11) replacing start letter with $:\n")
x=str[0]
y=str[1:]
res=x+y.replace(x,'$')
print(res)

# 12. Write a python program to get a single string from given two strings,seperated by a space
#  also swap the first two characters of the string
# Sample Strings : 'abc','xyz'
# Expected Result : 'xyc','abz'

str1='abc'
str2='xyz'
res=str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
print(res)

# #13. 13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
str=input("13) Enter the string: ")
if len(str)<3:
    print(str)
elif str.endswith('ing'):
    print(str+'ly')
else:
    print(str+'ing')

# 14. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'
def not_poor_to_good(str):
    if 'not' and 'poor' in str:
        x=str.find('not')
        y=str.find('poor')+4
        if 'bad' in str[y:]:
            str2=str[x:y]
            result=str.replace(str2,'good')
            return result
        

str='The lyrics is not that poor or bad'
print(not_poor_to_good(str))

# 15. Write a Python function that takes a list of words and returns the length of the longest one
def longest_in_list(list):
    longest_item=max(list,key=len)
    longest_len=len(longest_item)
    return longest_item
l=['apple','banana','cherry','orange','kiwi']
print(longest_in_list(l))

# 16. Write a Python program to test whether an input is an integer
x=input()
if x.isnumeric():
    print("Input is an int")
else:
    print("Input is not an int")


# 17. Write a Python program to sort (ascending and descending) a dictionary by value
dict = {'b': 2, 'a': 3, 'c': 1}
keys=dict.keys()
# SOL: To sort a dictionary use the following steps:
# !) Covert the dictionary into a list.
# 2) Sort the list based on the values. Use buuble sort 
# #) Crearte a new dictionary using teh list.

list=list(dict.items())
print("List :",list)
# using buuble sort for sorting
for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j][0]>list[j+1][0]:
            #Swap
            list[j],list[j+1]=list[j+1],list[j]
print("Sorted list:",list)
# create a new dictionary using the list
sorted_dict={key: value for key,value in list}
print(sorted_dict)


# Q18) Write a Python program to sort (ascending and descending) a dictionary by key value
# To sort thge dictionary by keys, do the following:
# 1) Extract the key-value pair of the dictionary in form of tuple
# Sort the tuples
# Create a new dictionary using the tuples

dict = {'a': 3, 'b': 1, 'c': 2}
list=list(dict.items())
print(list)

# Q19) Write a Python program to add key to a dictionary.
my_dict={'a':1,'b':2}
new_key=input("Enter the new key: ")
new_value=input("Enter the new value: ")
my_dict[new_key]=new_value
print("updated dictionay :",my_dict)


# Q20) Write a Python program to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Since dictionaries are immutable, create a new dict.
result={}
# Iterate over the keys in the first dictionary
for i in (dic1,dic2,dic3):
    for j in i:
        result[j]=i[j]

print(result)

# Q 21) Write a Python program to check if a given key already exists in a dictionary.
my_dict = {'a': 3, 'b': 1, 'c': 2}
def is_Present(x):
    if x in my_dict:
        print(x," is presnt")
    else:
        print("Not present")
is_Present(5)
is_Present('c')

# 22. Write a Python program to iterate over dictionaries using for loops
my_dict = {'a': 3, 'b': 1, 'c': 2}
for i in my_dict:
    print(i, my_dict[i])
for i in my_dict:
    print(my_dict.items)


# 23. Write a Python program to remove duplicates from a list.
li = [1, 2, 3, 2, 4, 3, 5, 1]

# Empty list to store unique elements
unique_list = []

# Loop through the original list
for x in li:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)


# 24. Write a Python program to check a list is empty or not.
li = [1, 2, 3, 4, 5]
if len(li)!=0:
    print("List is not empty")
else:
    print("list is empty")

# 25. Write a Python program to clone or copy a list
li = [1, 2, 3, 4, 5]
li2=li.copy()
print(li2)
