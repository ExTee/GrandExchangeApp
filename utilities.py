'''
	@author: XT
	utilities.py contains utility functions used for most tasks.
'''

import json
import pickle
import getPrices
import pandas as pd
import urllib.request, json
import urllib

ID_DICTIONARY = 'ID_DICTIONARY'

def update():
	getPrices.download_all()

def save_obj(obj, name ):
	with open('obj/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

'''
	Loads the ID dictionary as a dictionary
	@return: dict
'''
def load_IDS():
	return load_obj("ID_DICTIONARY")


'''
	Loads summary.json, and generate a dictionary of name to ID as a pkl file.
	@return: Nothing. saves file as ID_DICTIONARY.pkl
'''
def generate_IDS():
	f = open('summary.json')
	data = json.load(f)

	d = {}
	for id in data:
		name = data[id]['name']
		d[name] = id

	print(d)

	save_obj(d,ID_DICTIONARY)

'''
	Loads LIVE prices as a dictionary
'''
def getItemPrice(item_name):
	#Load ID dictionary
	d = load_IDS()

	#Match name queried to price
	id = d[item_name]

	#Generate query
	query = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i=' + id

	#JSON is loaded as dictionary
	with urllib.request.urlopen(query) as url:
		data = json.loads(url.read().decode())

	#returns dictionary corresponding to object
	return data

'''
	Loads summary.json into a pandas dataframe
'''
def load_dataframe(filename = 'summary.json'):
	#Loads all prices into a dictionary
	data = getPrices.get_all()

	sell_average, buy_average, sp, overall_average, members, ids, name = [],[],[],[],[],[],[]

	for id in data:
		sell_average.append(data[id]["sell_average"])
		buy_average.append(data[id]["buy_average"])
		sp.append(data[id]["sp"])
		overall_average.append(data[id]["overall_average"])
		members.append(data[id]["members"])
		ids.append(data[id]["id"])
		name.append(data[id]["name"])

	d = {
			'id':ids,
			'name':name,
			'sell_average':sell_average,
			'buy_average':buy_average, 
			'sp':sp,
			'overall_average':overall_average,
			'members':members,	
		}


	dataframe = pd.DataFrame(data = d)
	return dataframe


'''
	Retrieves price of item_name from the dataframe df
	@return a dataframe
'''
def getPrice(item_name, df):
	return df.loc[df['name'] == item_name]


'''
	Calculates profit
	@p_in  : 	list of prices of input
	@p_out : 	list of prices of output
	@return:	profit for one item	
'''
def calculateProfit(p_in, p_out):
	total_in = 0
	total_out = 0

	BUY = []
	SELL = []

	for data in p_in:
		total_in += data.buy_average.item()	
		BUY.append((data.name.item(),data.buy_average.item()))
		print("BUY  - {} : {}".format(data.name.item(), data.buy_average.item()))

	for data in p_out:
		total_out += data.sell_average.item()
		SELL.append((data.name.item(),data.sell_average.item()))
		print("SELL - {} : {}".format(data.name.item(), data.sell_average.item()))

	profit = total_out - total_in


	return profit, BUY, SELL


def main():
	print("Running Main")



if __name__ == '__main__':
	main()




