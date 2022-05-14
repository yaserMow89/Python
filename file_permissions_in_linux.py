#The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute
# for the owner, group, and others. Each of the three values can be expressed as an octal number summing
# each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string
# using the letters r, w, and x or - when the permission is not granted.
 #For example:
 #640 is read/write for the owner, read for the group, and no permissions for the others; converted to
# a string, it would be: "rw-r-----"
 #755 is read/write/execute for the owner, and read/execute for group and others; converted to a string,
# it would be: "rwxr-xr-x"

def convert_single_val(val):
    result = ""
    if int(val[0]) == 0:
        result += "---"
    elif int(val[0]) == 1:
        result += "--x"
    elif int(val[0]) == 2:
        result += "-w-"
    elif int(val[0]) == 3:
        result += "-wx"
    elif int(val[0]) == 4:
        result += "r--"
    elif int(val[0]) == 5:
        result += "r-x"
    elif int(val[0]) == 6:
        result += "rw-"
    elif int(val[0]) == 7:
        result += "rwx"
    else:
        return False
    return result
def octal_to_string(octal):
    result= ""
    octal = str(octal)
    count = 0
    while count <=2:
        result += str(convert_single_val(octal[count]))
        count += 1
        if result == False:
            return "Invalid input"
            break
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
