def my_map(my_func,myiteration):
    result = []

    for item in myiteration:
        newitem = my_func(item)
        result.append(newitem)
    return(result)

choice1 = list(input("Give me a List of num to Cube (no spaces):"))
nums  = choice1

cubed = my_map(lambda x: int(x)**3, nums)

print(cubed)
input()