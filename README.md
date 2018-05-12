# GrandExchangeApp
Application for calculating profits from RuneScape GrandExchange

## Tools for building daily and monthly averages
invisible.vbs:		Allows Windows to run a .bat file without prompt
storeJSON.bat:		Runs storeJSON.py (This is used in Windows scheduler to run periodically)
storeJSON.py:		Grabs prices from OSBuddy GE summary, transforms into dataframe, saves as .pkl

## Tools for profit calculation
armoursets.py:		Calculates profit for combining armmour into armour sets
fletching.py:		Calculates profit for making bolts
potions.py:		Calculates profit for combining potions

## Helper tools
utilities.py:		Utilities for loading into dataframes, calculating prices, etc.