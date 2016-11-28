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

I_can_List_things = [each for each in range (10, 20, 1)]
I_can_List_things
#Got it!  Got all my little numbers.  Except 20.  soooo
I_can_List_things = [each for each in range (10, 21, 1)]
#Bam.  Done.
#Interesting note.....I_can_List_things = [each in range (10, 21, 1)] gives me [True]




###3### Write a loop that prints out only the numbers from 20 to 10 that are even.
for i in range(20, 10, -2):
    print(i)
#This works but doesn't give me ten.  So I think that I need to go smaller than ten....
for i in range(20, 9, -2):
    print(i)
#Bam.  Even numbers.

    

###4### Write a list comprehension that prints out only the numbers from 20 to 10 that are even
I_can_list_even_things = [each for each in range (10, 21, 2)]
I_can_list_even_things
#It'sss alive!



###5### Write a function that calculates whether a number is a prime number
#hmmmm. my R code was
#is_prime <- function (num) {
#  if (num == 2) {
#    TRUE
#  } else if (any(num%%2:(num-1)==0)) { # see example function of a "any
#    FALSE
#  } else {
#      TRUE
#    }
#  }

#is_prime(7)

#Your R code was:
#is.prime <- function(x){
#    if(x==1)
#        return(FALSE)
#    for(each in (x-1):2)
#        if((x %% each) == 0)
#            return(FALSE)
#    return(TRUE)
#}

#so would be sort of similar, different syntax.  Possible to call functions as we did
#In R, but objects also have methods associated with it. Call by name language,
#saves resources  by not copying information from an argument into a new variable.


def optimus_PRIME (x):
    if x == 1:
        return "get outta hur"
    for each in (x-1),2:
        if x %% each ==0
            return "nooooo"
    return "true"

#invalid syntax at the %%.  not super shocked.  Change it to one % and its invalid syntaxo n the whole line.
#oh yeah.  : out the wazzoo
#Fixed it. 

def optimus_PRIME (x):
    if x < 1:
        return "get outta hur"
    for each in (x-1),2:
        if x % each ==0:
            return "nooooo"
    return "so PRIME"



####6###  Write a function that laods a text file, loops over the lines in it and
#prints out the fifth character on the fifth line of that file.

with open ("textytextertext.txt") as f:
    for l in handle:
        print(row[5])


####7###   Write a loop that prints out the numbers from 1-20, printing Good:NUMBER if it is divisible
 # by 5 and "Job:NUMBER" if its prime and nothing otherwise
 
for i in range (1, 20, 1):
    if i % 5 == 0:
        print "good", i
    elif optimus_PRIME(i) == "so PRIME":
        print "prime", i
#Error missing paranthesis in call to "print"
#also realized I don't need 1-20, by 1.  I just need range of 20 I think
for i in range (20):
    if i % 5 == 0:
        print ("good", i)
    elif optimus_PRIME(i) == "so PRIME":
        print ("prime", i)
# Traceback (most recent call last):
#  File "<pyshell#27>", line 4, in <module>
#    elif optimus_PRIME(i) == "so PRIME":
#  File "<pyshell#22>", line 5, in optimus_PRIME
#    if x % each ==0:
#ZeroDivisionError: integer division or modulo by zero



####8####  Biologist is modeling population growth using a Gompertz curve, which is defined as
#y(t) =a.e^-b.e^-c.x where:
#y=population size
#t is time
#a and b are parameters
#and e is exponential function
#Write a function that calculates population size for any values in its parameters

# R code = gompertz <- function(a, b, c, t) a * exp(-b * exp(-c * t))
def GOMGOM(a, b, c, t):
    a * exp(-b * exp(-c * t))
#NameError: name 'exp' is not defined

import math
from math import exp
#no errors but nothing printed.  If nothing is stored notihng can print soooo
def GOMGOM(a, b, c, t):
    GOM = a * exp(-b * exp(-c * t))
    return GOM
#YAY!!

####9####  Write a function that draws boxes of specified width and width with stars
#IN R
#box <- function(height, width){
#    .row <- function(x)
#        cat(rep("*",x),"\n", sep="")
#    
#    if(height < 3)
#        stop("Can't make a box of this height")
#    if(width < 1)
#        stop("Can't make a box of this width")
#    spacer <- height - 2
#    
#    .row(width)
#    for(i in seq_len(spacer))
#        cat("*", rep(" ",width-2), "*\n", sep="")
#    .row(width)
#}
#box(5, 7)

def BOXES_YO ("height", "width"):
    def rowz(x):
        cat(rep("*",x),"\n", sep="")

    if(height <3):
        stop("Can't H")
    if(width <3):
        stop("Can't W")
    spacer = height-2

    rowz(width)
    for (i in seq_len(spacer)):
        cat("*", rep(" ", width-2), "*\n", sep="")
    rowz(width)
#SyntaxError: invalid syntax
def BOXES_YO ("height", "width"):
    

####10####  Implement a point class that holds x and y information for a point in space (don't plot) 
#IN R
#new.point <- function(x, y){
#    if(!is.numeric(x) | !is.numeric(y))
#        stop("Can only create a point with numerical position data")
#
#    output <- list(x=x, y=y)
#    class(output) <- "point"
#    return(output)
#}
#new.point(3, 10)


####11#### Write a distance method that calculates the distance between two points in space. 
#IN R
#dist.points <- function(one, two){
#    if(!inherits(one, "point") | !inherits(two, "point"))
#        stop("Can only calculate distance between points")
#
#    return(sqrt((one$x-two$x)^2 + (one$y-two$y)^2))
#}
#dist.points(new.point(3,5), new.point(7,4))

####12####  Implement a line class that takes two point objects and makes a line between (don't plot)
#IN R
#new.line <- function(start, end){
#    if(!inherits(start, "point") | !inherits(end, "point"))
#        stop("Can only construct a line from points")
#
#    output <- list(start=start, end=end)
#    class(output) <- "line"
#    return(output)
#}
#new.line(new.point(3,5), new.point(7,4))

