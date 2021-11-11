'''                                     Welcome to the food generator
											By:Jai'Mir Darby                                                '''

import random
FastFood = ['McDonalds', 'Wendys', 'Popeyes', 'Subpreme Grill', 'Dairy Queen', 'Burger King', 'Checkers', 'Taco Bell', 'WingStop', 'Buffalo Wild Wings', 'Pizza Hut', 'Papa Johns' ]
Resurants = ['Olive Garden', 'Chilis', 'Longhorns', 'Outback', 'TGI Fridays', 'Red Lobster', 'Texas Roadhouse', 'Samurai', 'Steak n Shake']

input (" Hey, Welcome to the 'What should we eat today' program, to solve all your dumb argguements over what to eat in a relationship. ")
Choice = (input) (" Help us out a bit, which would you prefer?\n Fast/Cheap Food [1}\n Resurant/Expensive Food [2]\n No Prefrence [3]\n ")

if Choice == '1':
	RandomFF = random.choice(FastFood)
	print (' You guys should go to',RandomFF )
elif Choice == '2':
	RandomRes = random.choice(Resurants)
	print (' You guys should go to',RandomRes)  
elif Choice == '3':
	RandomAll = random.choice(FastFood + Resurants)
	print (' You guys should go to',RandomAll)
