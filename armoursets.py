'''
	@author: Andrei Z
	armorsets.py contains prices for combining armor pieces into sets
'''

import utilities

df = utilities.load_dataframe()


'''
Dharok:
	- 1 Dharok's Greataxe
	- 1 Dharok's Platebody
	- 1 Dharok's Platelegs
	- 1 Dharok's Helm
Torag:
	- 1 Torag's Hammers
	- 1 Torag's Platebody
	- 1 Torag's Platelegs
	- 1 Torag's Helm
Verac:
	- 1 Verac's Flail
	- 1 Verac's Brassard
	- 1 Verac's Plateskirt
	- 1 Verac's Helm
Guthan:
	- 1 Guthan's Warspear
	- 1 Guthan's Platebody
	- 1 Guthan's Chainskirt
	- 1 Guthan's Helm
Karil:
	- 1 Karil's Crossbow
	- 1 Karil's Leathertop
	- 1 Karil's Leatherskirt
	- 1 Karil's Coif
Ahrim:
	- 1 Ahrim's Staff
	- 1 Ahrim's Robetop
	- 1 Ahrim's Robeskirt
	- 1 Ahrim's Hood
'''
def Dharok():

	#Buy
	wep = utilities.getPrice('Dharok\'s greataxe', df)
	body = utilities.getPrice('Dharok\'s platebody', df)
	leg = utilities.getPrice('Dharok\'s platelegs', df)
	helm = utilities.getPrice('Dharok\'s helm', df)

	#Sell
	fullset = utilities.getPrice('Dharok\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))

def Karil():

	#Buy
	wep = utilities.getPrice('Karil\'s crossbow', df)
	body = utilities.getPrice('Karil\'s leathertop', df)
	leg = utilities.getPrice('Karil\'s leatherskirt', df)
	helm = utilities.getPrice('Karil\'s coif', df)

	#Sell
	fullset = utilities.getPrice('Karil\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))

def Ahrim():

	#Buy
	wep = utilities.getPrice('Ahrim\'s staff', df)
	body = utilities.getPrice('Ahrim\'s robetop', df)
	leg = utilities.getPrice('Ahrim\'s robeskirt', df)
	helm = utilities.getPrice('Ahrim\'s hood', df)

	#Sell
	fullset = utilities.getPrice('Ahrim\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))
def Guthan():

	#Buy
	wep = utilities.getPrice('Guthan\'s warspear', df)
	body = utilities.getPrice('Guthan\'s platebody', df)
	leg = utilities.getPrice('Guthan\'s chainskirt', df)
	helm = utilities.getPrice('Guthan\'s helm', df)

	#Sell
	fullset = utilities.getPrice('Guthan\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))
def Torag():

	#Buy
	wep = utilities.getPrice('Torag\'s hammers', df)
	body = utilities.getPrice('Torag\'s platebody', df)
	leg = utilities.getPrice('Torag\'s platelegs', df)
	helm = utilities.getPrice('Torag\'s helm', df)

	#Sell
	fullset = utilities.getPrice('Torag\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))
def Verac():

	#Buy
	wep = utilities.getPrice('Verac\'s flail', df)
	body = utilities.getPrice('Verac\'s brassard', df)
	leg = utilities.getPrice('Verac\'s plateskirt', df)
	helm = utilities.getPrice('Verac\'s helm', df)

	#Sell
	fullset = utilities.getPrice('Verac\'s armour set', df)

	#Profit
	profit, BUY, SELL = utilities.calculateProfit([wep,body,leg,helm],[fullset])
	print("Profit: {}\n".format(profit))



def main():
	#Always start by updating with newest summary.json
	utilities.update()

	#Check fletching info
	Dharok()
	Verac()
	Guthan()
	Torag()
	Karil()
	Ahrim()


if __name__ == '__main__':
	main()