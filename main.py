#@robocyber
import urllib2
from bs4 import BeautifulSoup
page = "https://wordsmith.org/words/today.html"
see= urllib2.urlopen(page)
soup = BeautifulSoup(see,features='html.parser')

print """
 ( \/\/ )(  _  )(_  _)(  _ \ 
  )    (  )(_)(   )(   )(_) )
 (__/\__)(_____) (__) (____/ 
 
       """


print "WORD OF THE DAY IS "
print soup.h3.text

links = soup.find_all('div',attrs ={'style':'margin-left: 20px;'})
print "Meaning:"+ links[1].text


