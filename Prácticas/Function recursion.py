def length(list):
    if list == []:
        return 0
    return 1 + length(list[1:])

def reverse(list):
    if len(list) == 0:
        return []
    body = list[:-1]
    return [list[-1]] + reverse(body) 

def map(function, list):
    if len(list) == 0:
        return []
    head = list[0]
    tail = list[1:]
    print(f'L={list} H={head} T={tail}')
    return [function(head)] + map(function, tail)

def double(number):
    return 2 * number

def concat(str1, str2):
    return str1 + str2

def foldl(list, start, function):
    if len(list) == 0:
        return start
    head = list[0]
    tail = list[1:]
    return foldl(tail, function(start, str(head)), function)


lista = [1, 2, 3, 4, 5, 6]
print(length(lista))
print(reverse(lista))
print(map(double, lista))
print(foldl(lista, '', concat))