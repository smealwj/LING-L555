
from cyrillicesp import cyrillicesp as c_map

with open("wikiest.txt", "r") as read_file:
	raw_data = read_file.readlines()
for line in raw_data:
	print('# text = %s' % line)
	start = 0
	a = 1
	space_index = line.find(" ")
	while space_index != -1:
		word = line[start:space_index]
		letters = [e for e in word]
#		кир = кир + c_map[l for l in letters]
		кир = 'Кир= ' + ''.join([c_map[l] for l in letters if l in c_map])
		print(str(a)+"  "+line[start:space_index]+'\t_'*8, кир)
		start = space_index+1
		space_index = line.find(" ", space_index+1)
		a=a+1

