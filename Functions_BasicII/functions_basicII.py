# Countdown
def countdown(num):
    nums_list = []
    for val in range(num,-1,-1)
        nums_list.append(val)
        return nums_list

    print(countdown(12))

#Print&Return

def print_and_return(nums_list):
    print(nums_list[0])
    return nums_list[1]

print(print_and_return([1,2]))

#First Plus Length
def plus_length(list):
    return list[0] + len(list)
sum = plus_length([1,2,3,4,5])
print("sum is:", sum)

#Values Greater Than Second
def values_greater_than_second(orig_list):
    new_list = []
    
    second_val = orig_list[1]
    
    for idx in range(len(orig_list)):
        if orig_list[idx] > second_val:
            new_list.append(orig_list[idx])
    
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))

#This Length, That Value
def length_and_value(size, value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list

print(length_and_value(4,7))