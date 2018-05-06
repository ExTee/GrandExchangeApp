'''
	@author: XT
	fletching.py contains functions for calculating fletching profits
'''

import utilities

df = utilities.load_dataframe()


'''
Onyx bolts:
	- 1 Runite bolts
	- 1 Onyx bolt tips
'''
def OnyxBolts():

	#Buy
	rb = utilities.getPrice('Runite bolts', df)
	obt = utilities.getPrice('Onyx bolt tips', df)

	#Sell
	ob = utilities.getPrice('Onyx bolts', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([rb,obt],[ob])
	print("Profit: {}\n".format(profit))

def DiamondBolts():

	#Buy
	rb = utilities.getPrice('Diamond bolts', df)
	obt = utilities.getPrice('Diamond bolt tips', df)

	#Sell
	ob = utilities.getPrice('Diamond bolts', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([rb,obt],[ob])
	print("Profit: {}\n".format(profit))

def RubyBolts():

	#Buy
	rb = utilities.getPrice('Ruby bolts', df)
	obt = utilities.getPrice('Ruby bolt tips', df)

	#Sell
	ob = utilities.getPrice('Ruby bolts', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([rb,obt],[ob])
	print("Profit: {}\n".format(profit))


def main():
	#Always start by updating with newest summary.json
	utilities.update()

	#Check fletching info
	OnyxBolts()
	DiamondBolts()
	RubyBolts()


if __name__ == '__main__':
	main()