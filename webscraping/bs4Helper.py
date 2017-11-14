## idea: this file should include very basic functions which are called by reference from a list
## the user supplies levels of depth and command as two lists.  Lists are compared by length
## used to call each function in order.  Level of depth executed top down, so user supplies
## first action first, etc.


import bs4


def get_links_and_linktext_from_html(stringhtml):
    thisdict = {}
    for link in bs4.BeautifulSoup(stringhtml, parseOnlyThese=bs4.SoupStrainer('a')):
        if link.has_attr('href'):
            thisdict[link.text] = link['href']
    return thisdict

def get_links_from_html(stringhtml):
    thislist = []
    for link in bs4.BeautifulSoup(stringhtml, parseOnlyThese=bs4.SoupStrainer('a')):
        if link.has_attr('href'):
            thislist.append(link['href'])
    return thislist
    
 ## Get class items from html
 
 
 ## Get ID from html
 
 
 ## Get elements from html
 
 
 
 ## Function switch
 
def functionSwitch(listFind, listLevel):

  for i in listlevel:
    case(listFindt[i]):
      
 
 
 
