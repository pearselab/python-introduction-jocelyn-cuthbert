###1### Write loop that prints out the numbers from 20 to 10
for i in range (10,20,1):
    print (i)
#Gave me nothing yet.....I think that because I am starting at 20, and adding positive one
    for i in range (10,20,-1):
    print (i)
#This worked correctly!  Yay!


    
###2### Write a list comprehension that returns the numbers form 20 to 10
results = []
for each in range (5, 10, 1):
    result append(each*2)
quicker_result = [each *2 for each in range(5,10)]

results = []
for each in range (20, 10, -1):
    result append(each)
#SyntaxError: multiple statements found while compiling a single statement
#for both.  Hmmmmmm.  Probably need something in the brackets. Or a :
#but wait.....multiple statements.  In the handout it is probably instead just
#telling us how to tell it to give us a result.  So instead I will try
for each in range (5, 10, 1):
    result append(each*2)
quicker_result = [each *2 for each in range(5,10)]
#aha.  Now I am just getting invalid syntax.  Bam.  It doesn't like append. 
for each in range (5, 10, 1):
    quicker_result = [each *2 for each in range(5,10)]
#= no error, but I didn;t have it print so I didn't get anything.
for each in range (5, 10, 1):
	quicker_result = [each *2 for each in range(5,10)]
	print (quicker_result)
#Now it printed it but did it 5 times.  probably because of my 5,10 in the quicker result
#take 5, I'll try to do it more correctly
for each in range (20, 10, -1):
	quicker_result = [each *1 for each in range(20)]
	print (quicker_result)	
#Ok.  Now I got all numbers from 0-20 10 times.  the way I am telling it to do the range must be wrong
for each in range (20, 10, -1):
	quicker_result = [each *1 for each in range(20)]
	print (quicker_result)	
#oh my gosh.  Didn't get the fact that the list comprehension is just the end line haha.
#I've been doing a loop and a list for no reason. Cool.  Lets try this again :)

I_can_List_things = [print each for each in range (10, 20, 1)]
                     
###3### Write a loop that prints out only the numbers from 20 to 10 that are even.
for i in range(20, 10, -2):
    print(i)
#This works but doesn't give me ten.  So I think that I need to go smaller than ten....
for i in range(20, 9, -2):
    print(i)
#Bam.  Even numbers.

#4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even

#5. Write a function that calculates whether a number is a prime number
    
