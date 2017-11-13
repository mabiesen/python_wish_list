import mapsInterface
import pprint

x = mapsInterface.GetCoordinates('mykey')

pprint.pprint(x.getCoordinatesList(["9025 Anchor Road","Highland","Indiana"]))
