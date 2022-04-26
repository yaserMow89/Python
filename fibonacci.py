The Following code is going to calculate the fibonaci series


iters = (int(input("How many Iterations would you like for your FIBONACCI? "))) - 3
val_1 = 0
val_2 = 1
val_3 = 0
list = [val_1, val_2]
count = 0

while count <= iters:
    val_3 = val_1 + val_2
    list.append(val_3)
    val_1 = val_2
    val_2 = val_3
    count += 1
    
    
print(list)
