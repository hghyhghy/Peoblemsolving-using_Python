

# checking wheather a string is symmetrical and palidrome at  same time or not 

#  first logic for symmetrical string 

string="sabbas"

half=int(len(string)/2)

firsthalf=string[0:half]

secondhalf=string[half:len(string)]

if firsthalf==secondhalf:

       print(f"The string {string} is symmetrical to each other ")

else:
       print(f"The string {string} is not symmetrical to each other ")


# creating function to check for palindrome 

def ispalindrome(sr):

       sr==sr[::-1]

       return sr

sr="sabbas"

ans=ispalindrome(sr)

if ans:

       print(f"{sr}is palindrome"  )

else:
       print(f"{sr}is not palindrome"  )




