with open("wikiest.txt", "r") as read_file:
	raw_data = read_file.readlines()
for line in raw_data:
	print('# text = %s' % line)
	start = 0
	a = 1
	space_index = line.find(" ")
	while space_index != -1:
		print(str(a)+"	"+line[start:space_index]+'\t_'*8)
		start = space_index+1
		space_index = line.find(" ", space_index+1)
		a=a+1

