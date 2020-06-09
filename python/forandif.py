colors = ['red' , 'blue', 'green']
print ("Using list : {}".format(colors))
for color in colors:
	if color == 'blue':
		print ("{} : my fav".format(color))
	else:
		print (color)

list_of_points = [(9,1),(8,2),(7,3)]
print ("Using list of tuples (has to be the same data type) : {}".format(list_of_points))
for x,y in list_of_points:
	print (f"x: {x} , y: {y} , x+y:{x+y}")

ages={'amit':42, 'sejal':40, 'avyaan': 9, 'shourya':7}
print (f"Using dictionary ages : {ages}")

print ("Using for key11 in ages:")
for key11 in ages:
	print (key11)

print ("Using for key in ages.keys():")
for key in ages.keys():
	print (key)

print ("For below items is a reserved keyword that was used for referencing the dictionary variable")
print ("You cannot do something like 'or name, age in ages:' . It has to be 'for name, age in ages.items():'")
for name, age in ages.items():
	print (f"{name}.{age}")

