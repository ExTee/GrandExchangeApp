'''
	@author: XT
	potions.py contains methods to calculate profit for:
		- BUY 3-dose -- CONVERT -> SELL 4-dose
		- BUY 3-dose ------------> SELL 3-dose
		- BUY 4-dose ------------> SELL 4-dose
'''

import utilities
import re

df = utilities.load_dataframe()



def SuperAttack():
	calculateLiveProfit('Super attack(3)')

def SuperDefence():
	calculateLiveProfit('Super defence(3)')

def SuperStrength():
	calculateLiveProfit('Super strength(3)')

def SuperCombat():
	calculateLiveProfit('Super combat potion(3)')

def Ranging():
	calculateLiveProfit('Ranging potion(3)')

def Magic():
	calculateLiveProfit('Magic potion(3)')

def Antifire():
	calculateLiveProfit('Antifire potion(3)')

def AntifireExtended():
	calculateLiveProfit('Extended antifire(3)')

def SuperAntifire():
	calculateLiveProfit('Super antifire potion(3)')

def SuperAntifireExtended():
	calculateLiveProfit('Extended super antifire(3)')

def Prayer():
	calculateLiveProfit('Prayer potion(3)')

def SuperRestore():
	calculateLiveProfit('Super restore(3)')

def SaradominBrew():
	calculateLiveProfit('Saradomin brew(3)')

def Stamina():
	calculateLiveProfit('Stamina potion(3)')

def SuperEnergy():
	calculateLiveProfit('Super energy(3)')

def SanfewSerum():
	calculateLiveProfit('Sanfew serum(3)')

def Antidote1():
	calculateLiveProfit('Antidote+(3)')

def Antidote2():
	calculateLiveProfit('Antidote++(3)')

def Antivenom1():
	calculateLiveProfit('Anti-venom+(3)')



'''
	Calculates profit using Summary.json (Prices are not live)
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

	profit = 0
	BUY,SELL = [],[]

	_potionIN	= utilities.getPrice(potion, df)
	_potionOUT3	= utilities.getPrice(potion, df)
	_potionOUT4	= utilities.getPrice(re.sub('3','4',potion), df)

	BUY.append(_potionIN)

	p_potionIN = _potionIN.buy_average.item()


	#Want to scale output and find maximum
	p_potionOUT3 = _potionOUT3.sell_average.item()
	p_potionOUT4 = _potionOUT4.sell_average.item() * 0.75

	#print(p_potionIN, p_potionOUT3 , p_potionOUT4)

	if p_potionOUT3 > p_potionOUT4:
		#If 3 dose sells more than 4 dose, return 3 dose
		profit = p_potionOUT3 - p_potionIN
		SELL.append (_potionOUT3)
	else:
		profit = p_potionOUT4 - p_potionIN
		SELL.append (_potionOUT4)	
	

	for data in BUY:
		print("BUY  - {} : {}".format(data.name.item(), data.buy_average.item()))

	for data in SELL:
		print("SELL - {} : {}".format(data.name.item(), data.sell_average.item()))
	
	print('PROFIT: {}'.format(profit))

	return profit, BUY, SELL

'''
	Calculates profits using live prices. More expensive.
'''
def calculateLiveProfit(potion):

	profit = 0
	BUY,SELL = [],[]

	_potionIN	= utilities.getItemPrice(potion)
	_potionIN['name'] = potion
	_potionOUT3	= _potionIN
	_potionOUT4	= utilities.getItemPrice(re.sub('3','4',potion))
	_potionOUT4['name'] = re.sub('3','4',potion)

	BUY.append(_potionIN)

	p_potionIN = _potionIN['selling']


	#Want to scale output and find maximum
	p_potionOUT3 = _potionOUT3['buying']
	p_potionOUT4 = _potionOUT4['buying'] * 0.75

	#print(p_potionIN, p_potionOUT3 , p_potionOUT4)

	if p_potionOUT3 > p_potionOUT4:
		#If 3 dose sells more than 4 dose, return 3 dose
		profit = p_potionOUT3 - p_potionIN
		SELL.append (_potionOUT3)
	else:
		profit = p_potionOUT4 - p_potionIN
		SELL.append (_potionOUT4)	
	

	for data in BUY:
		print("BUY  - {} : {}".format(data['name'], data['selling']))

	for data in SELL:
		print("SELL - {} : {}".format(data['name'], data['buying']))
	
	print('PROFIT: {}\n'.format(profit))

	return profit, BUY, SELL

def main():
	#Update prices
	#utilities.update()

	#Check potion info
	SuperAttack()

	SuperDefence()

	SuperStrength()

	SuperCombat()

	Ranging()

	Magic()

	Antifire()

	AntifireExtended()

	SuperAntifire()

	SuperAntifireExtended()

	Prayer()

	SuperRestore()

	SaradominBrew()

	Stamina()

	SuperEnergy()

	SanfewSerum()

	Antidote1()

	Antidote2()

	Antivenom1()


if __name__ == '__main__':
	main()