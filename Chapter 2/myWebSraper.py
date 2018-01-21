from lxml import html
import cssselect
import requests
from pprint import pprint as pp

resp = requests.get('http://kjamistan.com')
resp
pp(resp.content)

# want to import string into fom string function

page = html.fromstring(resp.content)#feed content string into fromstring funciton whicht akes tring and returns html element and save to variable


# check the methods of the html element
posts = page.cssselect('article.post') #select elements using their css tags, here selecting all the posts
posts

#TESTING#
posts = cssselect.Selector('article.post')
parser = cssselect.parser
posts = parser.parse('article.post')
print(posts)
from lxml.etree import fromstring
document = fromstring('''
   <div id="outer">
     <div id="inner" class="content body">text</div>
   </div>
 ''')
 [e.get('id') for e in document.xpath(expression)]


posts
