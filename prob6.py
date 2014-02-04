# Tyler Brabham
# CSC281A Spring 2014
# HW1 Prob6

'''
Function eliminate uses eliminate algorithm from text on arbitrary
chains of length n, using elimination order starting from n and
ending at 1.

Algorithm can compute P(X_1 = a | X_n = b), where n is the length
pf the chain. 

It is assumed that each X_i can take only the values 0 and 1.

Input to function is a matrix of transition probabilities, a value
for a and a value for b.
'''

def eliminate(last_node,evidence,transition):
	# Initialize. place p(x_i | x_pi_i) on active list
	ordering = range(1,last_node+1)
	ordering.reverse()

	active_list = []
	for i in ordering:
		if i==1:
			factor = ((i,0),None,.5)
			active_list.append(factor)
			factor = ((i,1),None,.5)
			active_list.append(factor)
		else:
			factor = ((i,0),(i-1,0),.6)
			active_list.append(factor)
			factor = ((i,1),(i-1,0),.4)
			active_list.append(factor)
			factor = ((i,0),(i-1,1),.2)
			active_list.append(factor)
			factor = ((i,1),(i-1,1),.8)
			active_list.append(factor)
	print active_list
	#Evidence. Last node only, just a single number
	if evidence == 1:
		delta = ((last_node, 1),None,1)
		active_list.append(delta)
		delta = ((last_node, 0),None,0)
		active_list.append(delta)
	else:
		delta = ((last_node, 1),None,0)
		active_list.append(delta)
		delta = ((last_node, 0),None,1)
		active_list.append(delta)

	#Update
	for i in ordering:
		# find all potentitals with i in them
		i_list = []
		new_active = []
		for elm in active_list:
			if i == elm[0][0] or (elm[1]!=None and i==elm[1][0]):
				i_list.append(elm)
			else:
				new_active.append(elm)
		active_list = new_active

		#multiply them all together, sum over the value of x_i (0 or 1)
		factors = [[(i-1,0),None,0], [(i-1,1),None,0]]
		for j in [0,1]:
			temp_sum = 0
			for k in [0,1]:
				temp_prod = 1.0
				for elm in i_list:
					if elm[1]==None:
						if elm[0][1]==k:
							temp_prod *= elm[2]
						else:
							pass
					else:
						if elm[0][1]==k and elm[1][1]==j:
							temp_prod *= elm[2]
						else:
							pass
				temp_sum += temp_prod
			factors[j][2] = temp_sum
			print temp_sum

		#place new factor on active list.
		active_list.extend(factors)

		print active_list
	
	#normalize

eliminate(4,1,None)