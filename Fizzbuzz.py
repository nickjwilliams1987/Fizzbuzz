#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Title:     Fizzbuzz Python
# Author:    Nick Williams
# Written    31st October 2020
# Overview   Standard programming challenge creating the Fizzbuzz game. Count up from 1 but instead of saying 3, or any number
#            divisble by 3 then say "Fizz" instead, and where the number is divisible by 5 say "Buzz" instead. If the number
#            is divisible by both then say Fizzbuzz.
#            Users can define their own Fizz & Buzz values, and any number of them, and the start and stop numbers to count.


#Define your Fizz's and Buzz's in this list
fizzbuzz_array=[['Fizz',3],['Buzz',5]]

#Define what number you want to start the output at
output_start = 1

#Define what number you want to end the output on
output_end = 200

#Define what steps you want to count up in
output_step = 1


def fizzbuzz(array, start, end, step):
    
    #Check inputs
    if type(array).__name__ != 'list':
        print('Please enter a list for the Fizzbuzz array. The type entered is ' + type(array).__name__ + '.')
        return
        
    if type(start).__name__ != 'int':
        print('Please enter an integer for the start number. The type entered is ' + type(start).__name__ + '.')
        return
    
    if type(end).__name__ != 'int':
        print('Please enter an integer for the end number. The type entered is ' + type(end).__name__ + '.')
        return
    
    if type(step).__name__ != 'int':
        print('Please enter an integer for the step number. The type entered is ' + type(step).__name__ + '.')
        return
    
    #Get the range of numbers to count and Fizzbuzz
    nums = range(start, end+1, step)
    
    #Loop through the range
    for j in nums:
        
        #By default we want to print the number
        output = str(j)
        found = False
        
        #Loop through the Fizzbuzz array, checking if the current number matches any in the array.
        for i in array:
            if j % i[1] == 0 and found == False:
                output = i[0]
                found = True
            elif j % i[1] == 0 and found == True:
                output += i[0]
            
        print(output)
        

#Start the fizzbuzz!
fizzbuzz(fizzbuzz_array, output_start, output_end, output_step)


# In[ ]:




