if __name__ == '__main__':
    s = input()
    
    result = False
    for i in s:
        if i.isalnum():
            result = True
            break
    print (result)
    result = False
    
    for i in s:
        if i.isalpha():
            result = True
            break
    print (result)
    result = False
    
    for i in s:
        if i.isdigit():
            result = True
            break
    print (result)
    result = False
    
    for i in s:
        if i.islower():
            result = True
            break
    print (result)
    result = False
    
    for i in s:
        if i.isupper():
            result = True
            break
    print (result)
    result = False
