def eggs(someParameter):
    someParameter.append('Hello')
    print('list id func is:',end='')
    id(someParameter)

def bacon(someParameter):
    someParameter = 'hello'
    print('list string func is:',end='')
    id(someParameter)

spam = [1,2,3]
print('List id is: ',end='')
id(spam)
eggs(spam)
print(spam)
print('list id is:',end='')
id(spam)
bacon(spam)
print(spam)