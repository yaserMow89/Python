def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) -1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1

        elif item > midpoint_value:
            begin_index == midpoint + 1    
    
    return -1 


test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
test_val2 = 15

# print (int(len(test_list)/2))
# print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))