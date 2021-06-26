def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False

list_1 = [1,2,3,4,5,6]
list_2 = [2,4,6,8,3,4]

print('First list:', is_consecutive(list_1))
print('\nSecond list:', is_consecutive(list_2))