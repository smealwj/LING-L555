import sys
temp = open('wiki.conllu')
tags={}
words={}
tagfreq = {}
countlist =[]
for line in temp.readlines(): 
	   
	line = line.strip('\n')
   
	if '\t' not in line:
        	continue

	row = line.split('\t')
	word = row[1]
	tag = row[4]
	form = row[10]
	countlist.append((word,tag))

for (word,tag) in countlist:
	if tag not in tags:
		tags[tag] = 0
	tags[tag] = tags[tag] + 1
	if word not in words :
		words[word] = {}
	if tag not in words[word]:
		words[word][tag] = 0
	words[word][tag] = words[word][tag] + 1
	
total = sum(tags.values())
print('P'+'\t'*4, 'COUNT'+'\t'*4, 'TAG'+'\t'*4, 'FORM')

for k,v in tags.items():
	print(round((v/total),2),"\t"*4,v,"\t"*4,k,"\t"*4,"_")	

for k,v in words.items():
	for x,y in words[k].items():
		print(round((y/sum(words[k].values())),2),"\t"*4,y,"\t"*4,x,"\t"*4,k)


