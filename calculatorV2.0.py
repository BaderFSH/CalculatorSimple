print ("===================>The calculator V2.0<===================")
print ("************************************************************")
while True :
	def  math1():
		square = int(input ('\n'"[~]Enter the Length : "))
		square2 = int(input ("[~]Enter the weigth : "))
		print (">>[",square * square2,"]<<")
		print ("############################################################")
	
	def math2():
		pi = (3.14) 
		R = int(input ('\n'"[~]Enter the R radias : "))
		print (">>[",pi * (R * R ),"]<<")
		print ("############################################################")
	
	def math3():
		R = int(input('\n'"[~]Enter R the Circel : "))
		pi2 = (3.14 * 3.14)
		print (">>[",R * pi2,"]<<")
		print ("############################################################")
	
	def math4():
		R = int(input('\n'"[~]Enter the Length of the side 1 :"))
		R2 = int(input("[~]Enter the Length of the side 2 :"))
		R3 = int(input("[~]Enter the Length of the side 3 :"))
		R4 = int(input("[~]Enter the Length of the side 4 :"))
		print (">>[",R + R2 + R3 + R4,"]<<")
		print ("############################################################")
		
	def math5():
		x1 = int(input ('\n'"[~]Enter the point[x1] : "))
		x1 = x1 * x1
		y1 = int(input ("[~]Enter the point[y1] : "))
		y1 = y1 * y1
		x2 = int(input("[~]Enter the point[x2] : "))
		x2 = x2 * x2
		y2 = int(input("[~]Enter the point[y2] : "))
		y2 = y2 * y2
		print (">>[",((x2 - x1))+ ((y2-y1)),"]<<")
		print ("[!]{Please Take the result and take the root to get the final result} \n")
		print ("############################################################")
		
	print ("[1] Square space ?")
	print ("[2] Circle area ?")
	print ("[3] circumference of a circle ?")
	print ("[4] The perimeter of the square or rectangle ? ")
	print ("[5] Length of a straight piece ? ")
	print ("############################################################")
	math = input ('\n'"What do you want? :  ")
	
	if math is '1' :
		print (math1())
	elif math is '2' :
		print (math2())
	elif math is '3' :
		print (math3())
	elif math is '4' :
		print (math4())
	elif math is '5' :
		print (math5())
	else :
		print ("Error : the namber is not found")