import urllib2
import re
from bs4 import BeautifulSoup

baseball = "http://www.baseballmonkey.com/article-common-baseball-terms-defined"
page = urllib2.urlopen(baseball)
soup = BeautifulSoup(page, "lxml")
baseball_words = []

all_strong=soup.find_all("strong")
for strong in all_strong:
    s=strong.get_text()
    s=re.sub('[!@#$:]', '', s)
    baseball_words.append(s)
    print s

print baseball_words
print len(baseball_words)
