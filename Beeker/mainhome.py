#!/usr/bin/env python

import sys
import os
import json
import wolframalpha
import wap
import urllib2
import greetings
from ask import ask
from process_response import process

def home(activity):
	if process(activity):
		pass
	else:
		print '\n'
		ask(activity)