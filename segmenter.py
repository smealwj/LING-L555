import sys
with open("wikiest.txt", "r") as read_file:
	raw_data = read_file.read()
re_data = raw_data.replace(".", ".\n")
with open("segmenter.txt", "w") as save_for_gh:
	save_for_gh.write(re_data)
print(re_data)
