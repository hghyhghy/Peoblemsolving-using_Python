

# python program to print the N no of largest  elements from a list 


list=[1000,1002,9,4550,123,0]

n=4

# sorting the elements

list.sort()

print(f"The N no of largest element form the list {list } is " , list[-n:])