#!/usr/bin/env python
try:
	import requests
except ImportError:
    print("\nA package called requests is required to run this script.")
    print("Install it by : sudo apt-get install python-requests\n")
    quit()
	
try:
	from bs4 import BeautifulSoup
except ImportError:
    print("\nA package called Beautiful Soup is required to run this script.")
    print("Install it by : sudo apt-get install python-bs4\n")
    quit()

import os
ch='y'
while ch=='y':

	os.system('clear')

	keyword = raw_input('\nEnter a word :')		#Takes input
	url = "http://www.dictionaryapi.com/api/v1/references/learners/xml/"+keyword+"?key=f46c56a3-000f-4057-bd99-90dc09fa4156" #sanyam.jain@iiitb.org API key for learners

	print("\nConnecting to the internet...")								#Fetches the XML Document
	r = requests.get(url)
	while r.status_code is not 200:
		r = requests.get(url)
	print("Connected.")

	soup = BeautifulSoup(r.text,"xml")
	if soup.select("dt")==[] :
		print("\nThe word you have entered is not in the dictionary.\n")
	else:
			
		label = soup.fl.string							#Finds the label
			
		examples=[]										#Fetches 3 examples usage of the words
		for link in soup.find_all('vi'):	
			examples.append(link.text)
			link.decompose()
			if len(examples)==3:
				break

		for tag in soup.dt.findAll(True):				#Deletes other tags
			tag.decompose()

		meaning=soup.dt.text							#Finds the meaning of the word
		print("")
		print("Label\t:"+label)
		print("Meaning "+meaning.strip())
		for example in examples[0:3]:
			print("Example :" +example)
		print("\n")
	ch = raw_input("You you want to search more ? y/n\n")		#Takes input
print("\nBye.")
print('  _________\n /         \\\n |  /\\ /\\  |\n |    -    |\n |  \\___/  |\n \\_________/');
print("")
