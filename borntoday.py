# Description:1
# Extract a list of who was born or died on a specific date of the year
# Output as HTML for inclusion in a web page
#
# 12/11/2015 Initial version
# 01/18/2017 Change logic so it can handle multiple days
from bs4 import BeautifulSoup
from datetime import timedelta, date
import datetime
import urllib.request		# this for python 3 and later
import requests

CONST_WORDS = ['mathe', 'scientist', 'programm', 'comput']

def BornDied(aDate):
  myDate = aDate.strftime('%B_%d')
  # Wikipedia has a page for each day of the year eg: https://en.wikipedia.org/wiki/December_11
  myURL = "http://en.wikipedia.org/wiki/"+myDate
  page = urllib.request.urlopen(myURL)

  #parse
  soup = BeautifulSoup(page, "html.parser")

  # Extract all list items <ul>
  uSections = soup.find_all('ul')

  # extract all 4 sections
  sItems = []
  for iEvents in uSections[14:]:
    snippet = iEvents.find_all('li')
    sItems = sItems + snippet
    
  #spew them out, but only if they contain keywords
  print('<html><head><base href="{0}"> <title>Events for {1}</title></head><body>'.format(myURL, aDate))
  for sItem in sItems:
    for stopword in CONST_WORDS:
      if stopword in sItem.get_text():
        print('{0}'.format(sItem))
        break

#        print('{0}'.format(sItem).encode('ascii','ignore'))
  print('</body></html>')


def Main():
  #from today
  start_date = datetime.date.today()
  #next 30 days
  day_count = 30
  for single_date in (start_date + timedelta(n) for n in range(day_count)):
      BornDied(single_date)
    

Main()
