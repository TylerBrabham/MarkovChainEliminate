# Tyler Brabham
# CS C281A Spring 2014
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

def eliminate(query_node,evidence_node,initial_dist,transition,query_val,evidence_val):
	# Initialize. place p(x_i | x_pi_i) on active list
	ordering = range(2,evidence_node+1)
	ordering.reverse()

	#put in initial factors
	active_list = []
	for state in range(2):
		factor = ((1,state),None,initial_dist[state])
		active_list.append(factor)

	#put in transition factors
	for i in range(2, evidence_node+1):
		for state in range(2):
			for prev_state in range(2):
				factor = ((i,state), (i-1,prev_state), transition[(prev_state,state)])
				active_list.append(factor)

	#Evidence. Last node only, just a single number
	if evidence_node == 1:
		delta = ((evidence_node, 1),None,1.0)
		active_list.append(delta)
		delta = ((evidence_node, 0),None,0.0)
		active_list.append(delta)
	else:
		delta = ((evidence_node, 1),None,1.0)
		active_list.append(delta)
		delta = ((evidence_node, 0),None,0.0)
		active_list.append(delta)

	#Update
	numerator_list = []
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
					#multiply all the terms together
					if elm[0][1]==k and (elm[1]==None or elm[1][1]==j):
						temp_prod *= elm[2]

				temp_sum += temp_prod

			factors[j][2] = temp_sum

		#place new factor on active list.
		active_list.extend(factors) 

	#normalize
	denominator = 0.0
	numerator = 0.0
	for j in range(2):
		temp_prod = 1.0

		for elm in active_list:
			if elm[0][1]==j:
				temp_prod *= elm[2]

		denominator += temp_prod
		if j==query_val:
			numerator += temp_prod

	return numerator/denominator

transition = {(0,0):.6, (0,1):.4, (1,0):.2, (1,1):.8}
initial = {0:.5, 1:.5}

print eliminate(1,4,initial,transition,0,1)