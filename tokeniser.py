with open("wikiest.txt", "r") as read_file:
	raw_data = read_file.read()
start = 0
a = 1
space_index = raw_data.find(" ")
while space_index != -1:
	print(str(a)+" "+raw_data[start:space_index])
	start = space_index+1
	space_index = raw_data.find(" ", space_index+1)
	a=a+1
else:
	print(raw_data[start::1])




