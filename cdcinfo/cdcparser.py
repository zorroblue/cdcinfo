import sys
import requests
from bs4 import BeautifulSoup
from News import News
import datetime
import traceback


base_url = 'http://10.3.100.27/notice/' #The CDC notice page
colors=["0;31;31","0;30;43","1;30;47","0;37;46"]

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

def print_all_results(newsList):
	i=0
	for news in newsList:
		print '\x1b[%sm %s \x1b[0m' %(colors[1],news)
		i=i+1

def main():

	soup = get_page_text()
	arg=None
	
	if(len(sys.argv)>1):
		arg=sys.argv[1]
        rows = soup.find("table").findAll('tr', {'class' : 'notice-rows'})
	newsList=[]
	
   	for row in rows[1:]:
		rowList=row.findAll('td')
		#print rowList,"\n", len(rowList),"\n"
                news=News(rowList[0].string,rowList[1].string,rowList[2].string,rowList[3].find("div",class_="noticeHeading").get("data-notif"),rowList[4].string)
		newsList.append(news)
	
	if arg == '--all' or arg == None:
		print_all_results(newsList)		

	elif arg=='--new':
		try:
			f=open('config.txt','r')
		except:
			print_all_results(newsList)
			f=open('config.txt','w')
			f.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M'))
			sys.exit()
		data=f.read()
		if(data is None or len(data)==0):
			print_all_results(newsList)
			f=open('config.txt','w')
			f.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M'))
			sys.exit()
		#get the last date saved from the file
		last_date=None
		try:
			last_date = datetime.datetime.strptime(data.strip(),'%d-%m-%Y %H:%M')
		except:
			print "Looks like something is wrong!!! Is your config file damaged?"
			traceback.print_exc()
			sys.exit()
		
		if last_date is None:
			print_all_results(newsList)
			f.close()
			f=open('config.txt','w')
			f.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M'))
			sys.exit()
		else:
		 	i=0
			for news in newsList:
				if(news.date >= last_date):
					print '\x1b[%sm %s \x1b[0m' %(colors[1],news)
					i=i+1
				else:
					break
			f.close()
			f=open('config.txt','w')
			f.write(datetime.datetime.now().strftime('%d-%m-%Y %H:%M'))

	else:
		print "The usage is cdcinfo --all  [ for printing all notifications ]\n cdcinfo --new  [ for printing the ones you didn't see yet ]"

if __name__=='__main__':
	main()
