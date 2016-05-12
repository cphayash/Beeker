#!usr/bin/env python

import sys
import os
# import json
import re
import wikipedia
from respond import respond
import string

def getWiki(activity):
	# print "activity:",activity
	# punctuation = re.compile("\\b(\'|\?|\.|\,")
	punctuation_set = set(string.punctuation)

	for ch in string.punctuation:
		if ch in ["#","+","(",")","&","$","@"]:
			pass
		else:
			activity = activity.replace(ch,"")

	pattern = re.compile("\\b(of|are|what|whats|a|an|wrote|did|was|is|the|in|for|at|check|find|how|hows|is|tell|me|check|out|about|wiki|wikipedia|summarize|give|who|whos|whose|define|\?)\\W", re.I)
	new_string = re.sub(pattern, "", activity)
	# new_string = new_string.replace(punctuation,"")
	# pattern_list = ["of","are","what","whats","a","an","wrote","did","was","is","the","in","for","at","check","find","how","hows","is","tell","me","check","out","about","wiki","wikipedia","summarize","give","who","whos","whose","?"]
	# for ch in pattern_list:
	# 	if ch in new_string:
	# 		new_string = new_string.replace(ch,"")
	# 	else:
	# 		pass


	# print "new_string:",new_string


	if "summarize" in activity or "summary" in activity:
		# print new_string
		result = wikipedia.summary(new_string, sentences = 2)
	elif "wiki" in activity or "wikipedia" in activity:
		# print new_string
		result = wikipedia.summary(new_string)
	else:
		try:
			# print "entered wiki try"
			# result = wikipedia.search(new_string,results=10,suggestion=False)
			result = wikipedia.summary(new_string, sentences = 3)
		except Exception, e:
			try:
				# print "entered wiki except try"
				# result = wikipedia.search(new_string,results=10,suggestion=True)
				result = wikipedia.summary(new_string, sentences = 3)
			except Exception, e:
				# print "entered wiki except except"
				result = "I'm afraid I can't find any information about this."

	# return result
	respond(result)