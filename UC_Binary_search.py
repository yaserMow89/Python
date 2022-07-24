


def binary_search(input_array, value):
    if value in input_array:
        mid_index = int(len(input_array))
        indext_found = False
        while indext_found:
            if value == input_array[mid_index]:
                return mid_index
            elif value > input_array[mid_index]:
                first_index = mid_index+1
                last_index = len(input_array)
                mid_index = int(last_index - first_index)/2
                continue
            elif value < input_array[mid_index]:
                first_index = 0
                last_index = mid_index -1
                mid_index = int(last_index - first_index)/2
                continue
            return -1
test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
test_val2 = 15

# print (int(len(test_list)/2))
# print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))

