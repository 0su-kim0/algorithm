str = input()

def swap(str):
    return str.swapcase()

print(swap(str))

'''
#방법2

def swap2(str):
    result=''
    for char in str:
        if char.isupper():
            result+=char.lower()
        else:
            result+=char.upper()
    return result

'''

#알게된 것
#char.isupper()
#char.lower()
#char.upper()
#char.swapcase()
