## idea: this file should include very basic functions which are called by reference from a list
## the user supplies levels of depth(int) and command list.  Listand integer compared by length
## used to call each function in order.  Level of depth executed top down, so user supplies
## first action first, etc.


import bs4

class HtmlHelper:
    
    def __init__():
        print("HtmlHelper initialized")
    
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
    
    def get_elems_from_html(stringhtml, findel):
        elemlist = []
        for myelem in bs4.BeautifulSoup(stringhtml, parseOnlyThese=bs4.SoupStrainer(findel)):
            elemlist.append(myelem)
        return elemlist

     ## Get class items from html


     ## Get ID from html



    ## this will error control, pass arguments to function switch
    
    def html_search_several(listexecute, listfind, thishtml):
        if len(listexecute) != len(listfind):
            return "error"
        else:
            return function_switch(listexecute, listfind, thishtml)
    
    
     ## Function switch

    def function_switch(listexecute, listfind, thishtml):
        ## each time around, html represents another level of depth
        ## end result is item, list of items, or dict
        ## NOTE: dict must control for dupllicates
      i=0
      for i < len(listexecute):
        if listFind[i] == "class":

        if listFind[i] == "id":

        if listFind[i] == "elems":
            thishtml = get_elems_from_html(thishtml, listfind[i])

        if listFind[i] == "link":  ## defined as 'a' and 'href'.  Commonly used so allowing this high level method
            thishtml = get_links_from_html(thishtml, listfind[i])
            
        if listFind[i] == "linkandtext":
            thishtml = get_links_and_linktext_from_hml(thishtml, listfind[i])

        i += 1
      return thishtml                                        
                                                       
      
 
 
 
