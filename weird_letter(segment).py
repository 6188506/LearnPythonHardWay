 #=> after a string splited,transfer one of lists.

for i in range(1,len(w_list)+1):
	if i%2 != 0:
		w_list[i-1] = w_list[i-1].upper()
		
 