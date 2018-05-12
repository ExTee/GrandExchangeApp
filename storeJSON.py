'''
	@author: XT
	StoreJSON.py downloads summary.json from osbuddy and saves it with a timestamp
	Goes hand-in-hand with storeJSON.bat for scheduler
'''
import urllib.request, json
import urllib
from datetime import datetime
import pandas as pd
from utilities import load_dataframe

def getTime():
	return datetime.now().strftime('%Y-%m-%d %H-%M-%S')

def main():
	CURTIME = getTime()

	#construct path for storage
	PATH =  'D:/GrandExchangeJSON/' + CURTIME +'.pkl'

	#Load json into dataframe
	df = pd.read_json("https://rsbuddy.com/exchange/summary.json").T

	#Add time information
	df['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	#save as csv
	df.to_pickle(PATH)

	print('Saved DataFrame for {}'.format(PATH))
	


if __name__ == '__main__':
	main()