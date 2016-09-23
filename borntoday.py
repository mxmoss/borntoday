# Description:1
# Extract a list of who was born or died on a specific date of the year
# Output as HTML for inclusion in a web page
#
# Initial version: 12/11/2015
from bs4 import BeautifulSoup

import datetime
import urllib.request		# this for python 3 and later
import requests

#get today's date
today = datetime.date.today()
myDate = today.strftime('%B_%d')

# Wikipedia has a page for each day of the year eg: https://en.wikipedia.org/wiki/December_11
myURL = "http://en.wikipedia.org/wiki/"+myDate
print(myURL)
page = urllib.request.urlopen(myURL)

#parse
soup = BeautifulSoup(page, "html.parser")

# Extract all list items <ul>
uSections = soup.find_all('ul')
words = ['math', 'scientist', 'programm']

print('<html><head><title>Events for {0}</title></head><body>'.format(today))

'''
# print out sections
# skip first <ul> entry
for uSection in uSections[1:]:
  print('{0}'.format(uSection))
'''


for iEvents in uSections[1:4]:
  print('{0}'.format(iEvents.find_all('li')))
  
'''
# print out items that match
for iEvents in uSections[1:4]:
  print('hey!{0}<br/>'.format(iEvents))
  for stopword in words:
    print(stopword)
    if stopword in iEvents: #words in li:
      print('ho!')
      print('{0}'.format(iEvents))
'''

print('</body></html>')
