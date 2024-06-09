# chapter 3 grokking algos

# iterative version that uses while loop to search through pile
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile: # is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

# recursive version that searches through each box
def look_for_key_recusive(box):
    for item in box:
        if item.is_a_box():
            look_for_key_recusive(item)
        elif item.is_a_key():
            print("found the key!")

# never ending function 
def countdown(i):
    print(i)
    countdown(i - 1)

# adding base case to never ending function

def countdownbasecase(i):
    print(i)
    if i <= 0:
        return
    else:
        countdownbasecase(i - 1)

# call stack example, greet calls greet2 and bye
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

# 3.1 Call stack example 
# Greet2 calls Greet with name = maggie

# stack with factorial 
# factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
# 5! = 5 * 4!

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    
# 3.2 recursive function w/o base case? 
# infinite recursion, stack overflow error

def infinite():
    return infinite()

# recusion is when a function calls itself
# every recursive function has two cases: base case and the recursive case
# a stack has two operations: push and pop
# all function calls go onto the call stack
# the call stack can get very large, which takes up a lot of memory