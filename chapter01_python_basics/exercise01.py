# This program says hello and asks for my name

print('Hello world!')

myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') #ask for their age
myAge = input()
print('You will be %s in a year' % (str(int(myAge) +1)))