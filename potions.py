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


def Potion_SaradominBrew():
	#Buy
	b1 = utilities.getPrice('Saradomin brew(3)', df)

	#sell
	s1 = utilities.getPrice('Saradomin brew(3)', df)
	s1 = utilities.getPrice('Saradomin brew(4)', df)

'''
	Calculates profit
	@override : replaces the function in utilities

	@potion 	: string potion name
	@return		: max possible profit

	Function takes in a potion WITHOUT DOSE AMOUNT.
		-if potion has a 3-dose:
			-returns maximum profit for combining
		-if potion is 4-dose:
			-returns profit directly
'''
def calculateProfit(potion):








	input1 = p_in.buy_average.item()

	#Want to scaled output and find maximum


	for data in p_out:
		name = data.name.item()
		sell_price = data.sell_average()

		#Scale 4 dose potion to 3 dose equivalent IFF the input is a 3 dose potion
		if name.contains('(4)') and p_in.name.contains('(3)'):
			sell_price *= 0.75






	for data in p_in:
		total_in += data.buy_average.item()	
		BUY.append((data.name.item(),data.buy_average.item()))
		print("BUY  - {} : {}".format(data.name.item(), data.buy_average.item()))

	for data in p_out:
		total_out += data.sell_average.item()
		SELL.append((data.name.item(),data.buy_average.item()))
		print("SELL - {} : {}".format(data.name.item(), data.buy_average.item()))

	profit = total_out - total_in


	return profit, BUY, SELL

if __name__ == '__main__':
	main()