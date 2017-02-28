import urllib2
import re
from bs4 import BeautifulSoup
import random

sport_url = [
    "https://en.wikipedia.org/wiki/Glossary_of_baseball",
    "https://en.wikipedia.org/wiki/Glossary_of_basketball_terms",
    "https://en.wikipedia.org/wiki/Glossary_of_association_football_terms",
    "https://en.wikipedia.org/wiki/Glossary_of_American_football",
    "https://en.wikipedia.org/wiki/Glossary_of_golf",
    "https://en.wikipedia.org/wiki/Glossary_of_rugby_league_terms",
    "https://en.wikipedia.org/wiki/Glossary_of_ice_hockey_terms"
    ]
words = []

for sport in sport_url:
    page = urllib2.urlopen(sport)
    soup = BeautifulSoup(page, "lxml")
    all_dt=soup.find_all("dt")
    for dt in all_dt:
        word=dt.get_text()
        word=re.sub('[!@#$: ]', '', word)
        words.append(word)

new_ipsum = 0
ipsum_string = " "
while new_ipsum < 50:
    new_word = random.choice(words)
    ipsum_string = ipsum_string + " " + new_word
    new_ipsum = new_ipsum+1

print "Sport ipsum " + ipsum_string.lower()
