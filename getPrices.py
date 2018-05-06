import urllib.request, json
import urllib

def get_item(itemID):
	with urllib.request.urlopen("https://api.rsbuddy.com/grandExchange?a=guidePrice&i=9044") as url:
		data = json.loads(url.read().decode())
		return data

def get_all():
	with urllib.request.urlopen("https://rsbuddy.com/exchange/summary.json") as url:
		data = json.loads(url.read().decode())
		return data

def download_all():
	urllib.request.urlretrieve ("https://rsbuddy.com/exchange/summary.json", "summary.json")
	print("summary.json downloaded.")

def main():
	#get_all()
	download_all()

if __name__ == '__main__':
	main()