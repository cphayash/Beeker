import urllib2
import json
from pprint import pprint
from respond import respond
import webbrowser
from mapIt import googleMaps


def locateISS():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())

	latitude = obj['iss_position']['latitude']
	longitude = obj['iss_position']['longitude']

	# print obj['timestamp']
	# print latitude, longitude


	if latitude > 0:
		ns_location = "North"
		latitude_string = "{0: .5f}".format(latitude) + " " + ns_location
	else:
		ns_location = "South"
		latitude_string = "{0: .5f}".format(abs(latitude)) + " " + ns_location
	if longitude > 0:
		ew_location = "East"
		longitude_string = "{0: .5f}".format(longitude) + " " + ew_location
	else:
		ew_location = "West"
		longitude_string = "{0: .5f}".format(abs(longitude)) + " " + ew_location

	if longitude <= 20 and longitude > -69:
		ocean = "Atlantic Ocean"
	elif longitude <= -69 or longitude > 115:
		ocean = "Pacific Ocean"
	elif longitude > 20 and longitude <= 115:
		ocean = "Indian Ocean"

	if latitude < -55:
		ocean = "Southern"
		hemisphere = ""
	elif latitude > -55 and latitude < 0:
		hemisphere = "South"
	elif latitude > 0:
		hemisphere = "North"
	else:
		hemisphere = ""

	if longitude > -5.6 and longitude < 36.214049 and latitude > 30.269624 and latitude < 45.791372:
		ocean = "Mediteranean Sea"
		hemisphere = ""


	# factual = urllib2.Request('http://api.v3.factual.com/places/geocode?geo={"$point":[34.06021,-118.41828]}')
	# fact_response = urllib2.urlopen(factual)

	# new_fact = json.loads(fact_response.read())

	# fact_key = "lA0hhDs2bTeWHeUEl2tkps4ZZDEvYIzGslrag0Kl"

	# print type(new_fact)

	# print new_fact

	# pprint(new_fact)

	# print "factual data:",fact_response.__dict__.keys()

	# print factual.data

	openstreet = urllib2.Request("http://nominatim.openstreetmap.org/reverse?format=json&lat=" + str(latitude) + "&lon=" + str(longitude) + "&zoom=18&addressdetails=1")
	open_res = urllib2.urlopen(openstreet)

	jres = json.loads(open_res.read())

	print "JRES:",jres
	# print jres['error']

	# responses = []
	failure = False

	for item in jres:
		# print item
		if item == u"error":
			failure = True
			print "Failure is True"

	if failure == True:
		# respond("Sorry, I'm unable to find an address.")
		# respond("However, I can tell you that the current geographical coordinates for the International Space Station are latitude " + "%.5f" % latitude + " and longitude " + "%.5f" % longitude)
		respond("The current geographical coordinates for the International Space Station are latitude " + latitude_string + " and longitude " + longitude_string + ", over the " + hemisphere + " " + ocean)
		# arcGIS = urllib2.Request("http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?location=" + str(latitude) + "%2C+" + str(longitude) + "&distance=200&outSR=&f=pjson")
		# arcResponse = urllib2.urlopen(arcGIS)

		# jres = json.loads(arcResponse.read())
		
		# mapISS(latitude,longitude)
	else:
		print "Address:",jres['display_name']

		try:
			respond("The international space station is currently located over " + jres['display_name'])
		except:
			respond("I'm having trouble pronouncing this location name.")
	respond("Would you like to see the location on a map?")
	answer = raw_input("")

	for term in ["yes","yeah","sure","why not"]:
		if term in answer.lower():
			# mapISS(latitude,longitude)
			googleMaps(latitude, longitude, True)
			break

	# latitude = "%.3f" % latitude
	# print type(latitude)
	# print latitude

def mapISS(latitude,longitude):
	webbrowser.open_new("https://www.google.com/maps/search/" + str(latitude) + "," + str(longitude))
	# webbrowser.open_new("https://www.google.com/maps/place/"+str(latitude)[0:1]+"%C2%B0"+str(latitude)[2:3]+"'48.9%22S+55%C2%B053'09.0%22W/@-35.1469167,-55.8858333,11z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
	respond("You can see the current location here, on Google Maps.")