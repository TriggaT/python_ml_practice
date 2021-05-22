array = ["Malcolm", "X"]
array[0] = "Tray"


print(array[0] + " " + array[1])


groceryArray = ["Eggs", "Milk", "Yogurt", "Kombucha", "Chicken", "Lettuce", "Carrots"]
listSlice = groceryArray[3:6] # ":" slices the array non-inclusive of last index
slice_up_to_three = groceryArray[:3] #inclusive w/o "0" or last index 
slice_from_three = groceryArray[3:] 
slice_second_from_end = groceryArray[-2]

print(listSlice)
print(slice_up_to_three)
print(slice_from_three)
print(slice_second_from_end)

#Tuples - set of values nested in parenthesis and hold any number of variables

(x_values, y_values) = ([1,2,3],[-1,-2,-3])

# print(f'PLOT THIS POINT: {x_values[2]}, {y_values[0]}' ) - string interpolation python 3.6+
print("PLOT POINT: %s, %s" % (x_values[2], y_values[0])) #old version of string interpolation

tuple = (x_values, y_values) #allows you to pull out each as array and delve into each array/list

print(tuple[0][1])

