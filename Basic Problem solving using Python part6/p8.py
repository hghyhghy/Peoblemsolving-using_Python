# replacing multiple words of a string  in python

# creating a string

s1 = "Subham and Malati Loves Each Other "

print("The original string is ", str(s1))

# creating a variable for words which are to be replaced

repl_word = ["Malati"]

# creating a variable for the word by which we replace

the_word = "Shreyoshi"

# using a for loop to iterate through the words


for xy in repl_word:
    s1 = s1.replace(xy, the_word)

print(f"The replaced version of the string {s1} is ", str(s1))
