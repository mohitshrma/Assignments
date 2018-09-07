
# coding: utf-8

# In[ ]:


#Q.1 Write a Python program to replace last value of tuples in a list

#Solution

    n = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print([t[:-1] + (100,) for t in n])

    #end
    
    
# Q.2 You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

[input: 'This is mE 123'
output: 'tHIS IS Me 123']

    #Solution

    string = "This is mE 123"
    print (string.swapcase())

    #end


# Q.3 The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

    [Input: 
    ABCDCDC
    CDC]

    Output:
    2

    #Solution

    a = "ABCDCDC"
    b = "CDC"

    cnt = 0
    for i in range(0, len(a) - len(b)+1):
    if a[i:i+len(b)] == b:
        cnt += 1

    print (cnt)

    #end


#Q.4 Write a class in which its one method accepts a string from console and another method to print the characters that have even indexes

    #Solution

    import re

    string = "H1e2l3l4o5w6o7r8l9d"
    string = re.sub('[^a-zA-Z]', '', string)
    print (string)

    #end 
    
    
    

