#!usr/bin/env python

import sys
import os
# import json
import re
import wikipedia

def getWiki(activity):
	pattern = re.compile("\\b(of|the|in|for|at|check|find|how|how\'s|is|tell|me|check|out|about|wiki|wikipedia|summarize)\\W", re.I)
	string = re.sub(pattern, "", activity)

	if "summarize" in activity or "summary" in activity:
		result = wikipedia.summary(string[len('summarize'):], sentences = 2)
	elif "wiki" in activity or "wikipedia" in activity:
		result = wikipedia.summary(activity[len('wiki'):])
	else:
		try:
			result = wikipedia.search(string,results=10,suggestion=False)
		except Exception, e:
			result = wikipedia.search(string,results=10,suggestion=True)

	return result