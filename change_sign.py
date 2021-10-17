def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

numbers = [2, -2, 14, 0, 9.14, -1.25]

def change_direction(n):
    return -n
apply_to_each(numbers, change_direction)
print(numbers)



