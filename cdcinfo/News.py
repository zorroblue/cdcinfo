from datetime import datetime
"""Represents a single news bulletin"""

class News(object):

	subject=""
	company=""
	notice=""
	date=None

	def convert_date(self,datestring):
		date = datetime.strptime(str(datestring),'%d-%m-%Y %H:%M')

	def __init__(self,subject,company,notice,datestring):
		self.subject = subject
		self.company = company
		self.notice = notice
		self.convert_date(datestring)

	

		