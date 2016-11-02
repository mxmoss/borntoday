# Description:1
# Extract a list of who was born or died on a specific date of the year
# Output as HTML for inclusion in a web page
#
# Initial version: 12/11/2015
from bs4 import BeautifulSoup

import datetime
import urllib.request		# this for python 3 and later
import requests

def BornDied():
  #get today's date
  today = datetime.date.today()
  myDate = today.strftime('%B_%d')

  # Wikipedia has a page for each day of the year eg: https://en.wikipedia.org/wiki/December_11
  myURL = "http://en.wikipedia.org/wiki/"+myDate
  page = urllib.request.urlopen(myURL)

  #parse
  soup = BeautifulSoup(page, "html.parser")

  # Extract all list items <ul>
  uSections = soup.find_all('ul')
  words = ['mathe', 'scientist', 'programm', 'comput']

  # extract all 4 sections
  sItems = []
  for iEvents in uSections[1:4]:
    snippet = iEvents.find_all('li')
    sItems = sItems + snippet
    
  #spew them out, but only if they contain keywords
  print('<html><head><base href="http://en.wikipedia.org/."> <title>Events for {0}</title></head><body>'.format(today))
  print(myURL)
  for sItem in sItems:
    for stopword in words:
      if stopword in sItem.get_text():
  print('</body></html>')

BornDied()