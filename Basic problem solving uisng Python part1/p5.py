

# python program to sort word in an alphabet order 

mystr="Hello this is an apple , you should buy this "

words=[word.lower() for word in mystr.split()]

# sorting the words

words.sort()

print("The sorted words are ")

for word in words:

       print(word)