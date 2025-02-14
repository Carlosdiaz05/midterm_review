# To indicate the type of an expression, we can use the function type
# can also search for idle app and check here
#eg 2 +3
print(type(2+3)) #it gives int
#eg 5 or 6
print(type(5 or 6))
#eg print(2*2)
print(type(print(2*2))) #NonType
#eg "abc".find
print(type("abc".find))
# eg "bubu"*(4/2)
#print(type("bubu"*(4/2))) error

# Indicate the result of the following
#eg 2+3
print(2+3)
# eg 2 != 3
print(2 != 3)
# eg [] or "" or 0/10 or 7/2 or 9
print([] or "" or 0/10 or 7/2)
# eg [1,2,3].append("John")
print([1,2,3].append("John"))

#Assume the operations are executed in order. What will each print display
# we can simply print these and that's it

# a = 2
# b = 3
# c = "abc"
# print(a,b,c)
# print (a,b,c, sep=",")
# a += 2
# a == 5
# print(a)
# print()

# Question
# Write a function that takes the name of a text file as a parameter.
# #Print out the 3-letter words that start with b
#solution
#go to chatgpt and prompt: Write me a text file of 20 lines that contain an abnormal number of 3 letter words that start with B or b. Also use abnormal frequency of punctuation.
# with what chat gave us, create a new text file and copy paste it in it.
punctuation = ",.1?';\"" #punctuation we want to get rid of. Def is to create new function
def find_words(filename):
    """
    Prints 3 letter words starting with b from a file
    :param filename: the name of the file
    :return: None (nothing)
    """
    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
                    print(word)

find_words("midterm_practice.txt") #i'm calling the function here

# Question
# Write a function that takes an integer as parameter and returns a list of all the divisors of that number
    # ex 47 –> [1,47], 28 -> [1,2,4,7,14,28]
# Solution




#Question
# Write a function that forces the user to enter a multiple of 6 number. Use try, except to catch invalid inputs. Return that number
