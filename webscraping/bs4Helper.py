## idea: this file should include very basic functions which are called by reference from a list
## the user supplies levels of depth(int) and command list.  Listand integer compared by length
## used to call each function in order.  Level of depth executed top down, so user supplies
## first action first, etc.


import bs4

class HtmlHelper:
    
    mysoup = ""
    
    def __init__(htmlstring):
        print("HtmlHelper initialized")
        set_soup(hmtmlstring)
        
    def set_soup(self, htmlstring):
        self.mysoup = bs4.BeautifulSoup(htmlstring)
    
    def get_links_and_linktext_from_html(self):
        thisdict = {}
        for item in self.mysoup:
            if link.has_attr('href'):
                thisdict[link.text] = link['href']
        return thisdict
    
    def get_links_from_html(self):
        for link in self.mysoup:
            if link.has_attr('href'):
                thislist.append(link['href'])
        self.mysoup = thislist
        return self.mysoup
    
    def get_elems_from_html(findel):
        self.mysoup = self.mysoup.findAll(findel)
        return self.mysoup

     ## Get class items from html
    def get_classes_from_html(self, findclass):
        self.mysoup = soup.findAll(True,{'class':findclass})
        return self.mysoup
        
        
     ## Get ID from html
    def get_ids_from_html(self, findid):
        self.mysoup = soup.findAll(True,{'id':findid})
        return self.mysoup


    ## this will error control, pass arguments to function switch
    
    def html_search_several(listexecute, listfind, thishtml=""):
        if thishtml != "":
            set_soup(thishtml)
        if len(listexecute) != len(listfind):
            return "err"
        else:
            return function_switch(listexecute, listfind)
    
    
     ## Function switch

    def function_switch(self, listexecute, listfind):
        ## each time around, html represents another level of depth
        ## end result is item, list of items, or dict
        ## NOTE: dict must control for dupllicates
        ## NOTENOTENOTE:  MUST MAKE SOUP CLASSLEVEL, FIRST TURN TO Soup Then Run through
      burner = ""
      i=0
      for i < len(listexecute):
        if listFind[i] == "class":
            burner = get_classes_from_html(listfind[i])

        if listFind[i] == "id":
            burner = get_ids_from_html(listfind[i])

        if listFind[i] == "elem":
            burner = get_elems_from_html(listfind[i])

        if listFind[i] == "link":  ## defined as 'a' and 'href'.  Commonly used so allowing this high level method
            burner = get_links_from_html()

        i += 1
      return self.mysoup                                        
                                                       
      
 
 
 
