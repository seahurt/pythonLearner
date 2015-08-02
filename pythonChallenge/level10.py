#http://www.pythonchallenge.com/pc/return/bull.html


# a sequence: a = [1, 11, 21, 1211, 111221, 

# find the rule and calculate len(a[30])


#the rule is called : 
# 1
#one 1 :11
#two 1: 21
#one 2,one 1 : 1211
#one 1,one 2, two 1: 111221

# so describe the last line to obtain the new number


#a=[1,11,21,1211,111221



############# No 0

def find_same_successive_num(num):
	target=num[0]
	for x in range(0,len(num)):
		if num[x]==target:
			continue
		else:
			return x
	return len(num)




#########  No1
def cut_the_num(num):

	container=[]
	if len(num)==1:
		container.append(num)
		return container
	while(True):
		count=find_same_successive_num(num)
		if count==0:break
		if count==len(num):
			container.append(num)
			break
		container.append(count*num[0])
		num=num[count:]

	#print 'container is ',
	#print container
	return container


################### No2
def describe_the_num(container):
	ins_list=[]
	for x in container:
		ins_list.append(str(len(x)))

		ins_list.append(x[0])
	#print len(ins_list)
	new_num=''.join(ins_list)
	return int(new_num)








def find_next_num(num):
	num=str(num)
	container=cut_the_num(num)
	#print container
	next_num=describe_the_num(container)
	#print next_num
	return next_num


a=[1]
while(len(a)<31):
	new=find_next_num(a[-1])
	a.append(new)

print len(str(a[30]))


#5808

