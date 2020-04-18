# part 1 do a try block to make sure the list has objects
# part 2 if it does have objects, range print up to the final item
# print and then the final item

def commaCode(listOfItems):
    try:
        # try block in case the list is empty
        lenOfList = len(listOfItems)
        if(lenOfList > 1):
        # check if the len of list is greater than 1 object
            for i in range(lenOfList - 1):
                # print each item in the list with a comma
                print(listOfItems[i],end=', ')
            # print and before the final statement 
            print('and ', end='')
        # print last item if the list is bigger than 1 otherwise just print the only item in the list
        print(listOfItems[lenOfList-1])
    except IndexError:
        print('Nothing in list')

spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = []
spam3 = ['flights']

commaCode(spam3)