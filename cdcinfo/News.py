from datetime import datetime
import sys
"""Represents a single news bulletin"""


class News(object):

	sno=""
	subject=""
	company=""
	notice=""
	date=""
		

	def __init__(self,sno,subject,company,notice,datestring):
		self.sno=sno
		self.subject = subject
		self.company = company
		self.notice = notice
		try:
			self.date = datetime.strptime(str(datestring),'%d-%m-%Y %H:%M')
		except:
			print "Looks like something is wrong!! Is your config file damaged?"
			sys.exit()

	def __str__(self):

		matter=str(unicode(self.notice).encode('ascii','ignore'))
		string = "#######################\nDATE: "+str(self.date)+"\n"+str(self.sno)+str(self.subject)+" ---- "+str(self.company)+"\n\n" +matter+"\n#######################\n"
	
		return string

		