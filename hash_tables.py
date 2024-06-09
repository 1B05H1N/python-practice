# ch 5 grokking algos
# hash function is a functions hwere your put in a string and it returns a number
# hash functions are used in hash tables

# Which of these functions are consistent?
# 5.1 f(x) = 1, consistent because it always returns 1
# 5.2 f(x) = rand(), not consistent because it changes
# 5.3 f(x) = next_empty_slot(),  not consistent because it changes
# 5.4 f(x) = len(x), consistent because it always returns the length of x

# voting example 

voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")

check_voter("tom")
# let them vote
check_voter("mike")
# let them vote
check_voter("mike")
# kick them out

# cache example

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# recap 
# hashes are good for modeling relationships between two things
# hash functions are good for filtering out duplicates
# hash functions are good for caching/memoization (store the results of expensive function calls and return the cached result when the same inputs occur again)

# to avoid collisions, you can use a hash table with linked lists at each index
# you need a low load factor, and a good hash function to avoid collisions

# excerises
# which hash function would provide a good distribution?
# a. Return “1” for all input., bad because it maximizes collisions and doesn't use the hash table effectively
# b. Use the length of the string as the index., okay but will have collisions if there are strings of the same length
# c. Use the frst character of the string as the index. So, all strings , starting with a are hashed together, and so on., bad because it maximizes collisions and doesn't use the hash table effectively
# d. Map every letter to a prime number: a = 2, b = 3, c = 5, d = 7, e = 11, and so on. For a string, the hash function is the sum of all the characters modulo the size of the hash., good because it uses a good hash function

# 5.5 a,b = bad, c = good, d = best
# 5.6 a,c = bad, b,d = good
# 5.7 a = poor, b = fair, c = good, d = best

# recap
# hash tables are fast because they use a hash function to store data in an array
# you'll almost never have to implement one yourself, but it's good to understand how they work

# you can make a hash table by combining a hash function with an array
# collisions are bad, your need a good hash function and a low load factor
# hash tables are great for modeling relationships from one item to another
# once you outgrow your hash table, you'll need to resize it
# usually if your load factor is greater than 0.7, it's time to resize
# hash tables are used for caching data (for example, with a web server)
# hash tables are great for catching duplicates