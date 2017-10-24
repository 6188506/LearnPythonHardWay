from sys import argv
script, destination_file = argv

print script
print "read file from ex1 to ex41,and write to a argv file"
x = 1
if x <= 41:
	target = open('e:/learnpythonhardway/ex'+str(x)+'.py')
	wenben = target.read()
	open(destination_file,'r+')
	destination_file.write(wenben)
	destination_file("\n")
	target.close()
	x = x + 1

