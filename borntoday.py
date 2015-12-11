# Description:
# Extract a list of who was born or died on a specific date of the year
# Output as HTML for inclusion in a web page
#
# Initial version: 12/11/2015
from bs4 import BeautifulSoup

import datetime
import urllib.request		# this for python 3 and later
import requests

# Wikipedia has a page for each day of the year eg: https://en.wikipedia.org/wiki/December_11
myURL = "en.wikipedia.org/wiki/"

#get today's date
today = datetime.date.today()
myDate = today.strftime('%B_%d')
page = urllib.request.urlopen("http://"+myURL+myDate)

#parse
soup = BeautifulSoup(page, "html.parser")

# Extract all list items <li>
rows = soup.find_all('li' )

#output
print('<html><head><title>Events for {0}</title></head><body><ul>'.format(today))
for row in rows:
  print('<li>{0}</li>'.format(row.text))
print('</ul></body></html>')
