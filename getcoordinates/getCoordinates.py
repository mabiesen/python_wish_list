import googlemaps
import time


#Should be able to receive address or list of addresses; control for time allowances between calls



class GetCoordinates:

    __myclient = ""

    def __init__(self, mykey):
        self.myclient = googlemaps.Client(key=mykey)

    def getCoordinatesList(self, mylist):
        ## example input '1600 Amphitheatre Parkway, Mountain View, CA'
        returnlist = []
        sendstring = ", ".join(mylist)
        geocodeOutput = self.myclient.geocode(sendstring)
        for k in geocodeOutput[0]['geometry']['location']:
            returnlist.append(geocodeOutput[0]['geometry']['location'][k])
        return returnlist

    def getManyCoordinatesList(self, listoflists):
        returnlist = []
        for mylist in listoflists:
            returnlist.append(self.getTheseCoordinates(mylist))
            time.sleep(0.2)
        return returnlist
