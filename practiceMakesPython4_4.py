people_list = []
people = [
          {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
          {'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
         ]
		 
for item in people:
	people_list.append(item['last'],item['first'],item['email'])	

people_list_sorted =sorted(people_list)	
		 
for i in people_list_sorted:
	print(i[0],i[1],i[2])

	
		 