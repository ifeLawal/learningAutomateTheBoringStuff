import sys
catNames = []
try:
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) 
                + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name] # list concatenation
except KeyboardInterrupt:
    sys.exit()

print('The cat names are:')
for name in catNames:
    print(' ' + name)