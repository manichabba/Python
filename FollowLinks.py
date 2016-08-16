"""The program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position from the top and follow that link, 
repeat the process a number of times, and report the last name you find."""

import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
pos = int (raw_input("Enter position:"))
count = int(raw_input("Enter count:"))

for i in range(count):
	tags = BeautifulSoup(urllib.urlopen(url).read())('a')
	url = tags[pos-1].get('href', None)
	y = re.findall('by_([^.]*)', url)
	print "Retrieved " + str(i+1) + ":" + url
print "The last name is " + y[0]