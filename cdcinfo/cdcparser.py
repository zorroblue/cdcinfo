import sys
import requests
from bs4 import BeautifulSoup
from News import News

base_url = 'http://10.3.100.27/notice/' #The CDC notice page

def get_page_text():
	"""Get the entire page source of the CDC notice page"""
	"""Give me soup,give me freedom"""
	r = requests.get(base_url);
	if r.status_code is not 200:
		print "Looks like something is wrong.Please check your internet connection!"
		sys.exit()
	data = r.text;
	soup = BeautifulSoup(data,'lxml')
	return soup

def main():

	#soup = get_page_text()
	#############
	#FOR TESTING PURPOSES, use file for storing local copy of soup
	#############
	
	#parse command line argument
	arg=None
	if(len(sys.argv)>1):
		arg=sys.argv[1]
		print arg
	f=open('soup.txt')
	soup=BeautifulSoup(str(f.read()),'lxml')
	rows = soup.find("table").findAll('tr')
	newsList=[]
	for row in rows[1:]:
		rowList=row.findAll('td')
		news=News(rowList[1].string,rowList[2].string,rowList[3].string,rowList[4].string)
		newsList.append(news)




if __name__=='__main__':
	main()
