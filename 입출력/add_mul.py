def add_mul(choice, *args):
    if choice == 'add': # 매겨변수 choice에 'add'를 입력받았을떄.
        result = 0
        for i in args:
            result = result + i 
    
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i 
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print (result)