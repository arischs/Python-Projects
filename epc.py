#A program created for fun by Arisch

print('Welcome to Electric Power Calculation Tool')
#declares variables
P=0
V=0
I=0
R=0

running= True
#defines various functions for calculation of value of Electric Power
def Power_V_I(V, I):
	P = V * I
	print('\nThe value of Electric Power is {} Watt' .format(P))

def Power_I_R(I, R):
	P = (I*I)*R
	print('\nThe value of Electric Power is {} Watt' .format(P))
	
def Power_V_R(V, R):
	P = (V * V)/R
	print('\nThe value of Electric Power is {} Watt' .format(P))
while running:
	print('\nYou can calculate value of Electric Power just by feeding in any of these values: \n')
	print('''	1. Voltage and Current
	2. Current and Resistance
	3. Voltage and Resistance
	4. Exit Electric Power Calculation Tool''')
#asks user to select the desired method
	selection=int(input('\nMake your selection (Type in the number preceeding your selection) : '))

#puts the selected formula to work
	if selection==1:
		V = float(input('\nEnter the value of Voltage : '))
		I = float(input('Enter the value of Current : '))
		Power_V_I(V, I)
	elif selection==2:
		I = float(input('\nEnter the value of Current : '))
		R = float(input('Enter the value of Resistance : '))
		Power_I_R(I, R)
	elif selection==3:
		V = float(input('\nEnter the value of Voltage : '))
		R = float(input('Enter the value of Resistance : '))
		Power_V_R(V, R)
	elif selection==4:
		exit('Hope we were of some help to you :D')
	else:
		print('\n-------Please make a proper selection-------')