#! /usr/bin/python

import webbrowser
from respond import respond
import sys


# Define googleMaps
#
# This function will open a web browser (or a new tab if
# it's already open) and plot the coordinates on Google
# Maps.
def googleMaps(latitude,longitude, speak):
	if checkCoordinates(latitude, longitude):
		northSouth = "North"
		eastWest = "East"
		latitude = float(latitude)
		longitude = float(longitude)
		shortLat = "{:.2f}".format(abs(latitude))
		shortLon = "{:.2f}".format(abs(longitude))
		longLat = "{:.6f}".format(latitude)
		longLon = "{:.6f}".format(longitude)
		deg = unichr(176)

		zoom = "4"
		# URL = "https://www.google.com/maps/search/{},{}".format(str(latitude), str(longitude))
		# URL = "https://maps.google.com/?q=10,10&ll=10,10&z=3"
		# URL = "https://maps.google.com/?q=38.6531004,-90.243462&ll=38.6531004,-90.243462&z=3"
		URL = "https://maps.google.com/?q={},{}&ll={},{}&z={}".format(str(longLat), str(longLon), str(longLat), str(longLon), zoom)
		# print URL
		# webbrowser.open_new("https://www.google.com/maps/search/" + str(latitude) + "," + str(longitude))
		webbrowser.open_new(URL)
		# webbrowser.open_new("https://www.google.com/maps/place/"+str(latitude)[0:1]+"%C2%B0"+str(latitude)[2:3]+"'48.9%22S+55%C2%B053'09.0%22W/@-35.1469167,-55.8858333,11z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
		try:
			# print "In Try"
			if latitude < 0:
				northSouth = "South"
			if longitude < 0:
				eastWest = "West"
			if speak:
				# respond("You can see the current location here, on Google Maps.")
				# respond("Mapping latitude {}, longitude {}".format(shortLat, shortLon))
				respond(u"Mapping {}\xb0 {}, {}\xb0 {}".format(shortLat, northSouth, shortLon, eastWest))
		except:
			pass



def checkCoordinates(latitude, longitude):
	if abs(latitude) > 90.0 or abs(longitude) > 180.0:
		respond("You entered: {}, {}.\nThese are invalid coordinates".format(latitude, longitude))
		return False

	return True

def testMap():
	try:
		coordinates = sys.argv[1:3]
		# print coordinates
		googleMaps(coordinates[0], coordinates[1], True)
	except:
		raise Exception("Invalid coordinates.  You must provide 2 numbers.")
		sys.exit(1)



# if __name__ == "testMap":
if __name__ == "__main__":
	# print "Mapping {}, {}".format(sys.argv[1], sys.argv[2])
	# respond("Mapping latitude {}, longitude {}".format(sys.argv[1], sys.argv[2]))
	testMap()