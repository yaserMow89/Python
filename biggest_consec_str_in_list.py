# The following code is going to take a list of values and return the biggest consequent string that can
# be taken out from the list by a specific number of elements in that list
# for Example when you give str_lst = ["zone", "abigail", "theta", "form", "libe", "za"] with 1
# it is going to return the biggest element in the list
# But if you ask for two elements, it is going to return biggest element+second biggest element

def longest_consec(strarr, k):
    if (len(strarr) == 0) or (k > len(strarr)) or (k <= 0):
        return ""
    total_combnd = (len(strarr) - k) + 1
    combined_list = []
    for d in range(total_combnd):
        temp_str = ''
        m = d
        for p in range(k):
            temp_str += strarr[m]
            m += 1
        combined_list.append(temp_str)
    long_str = combined_list[0]

    for z in range(1,len(combined_list)):
        if len(long_str) < len(combined_list[z]):
            long_str = combined_list[z]

    return long_str


str_lst = ["zone", "abigail", "theta", "form", "libe", "za"]
print(longest_consec(str_lst, 1))
