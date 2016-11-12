import requests


class OnlineDictionary(object):
	"""Finds the definition of a word by consuming
	the https://developer.oxforddictionaries.com/ 
	public api
	"""

	app_id = "bf8c3e30"
	app_key = "65bbf7c019b6d1d43fcb1a19b04f9381"
	language = "en/"
	prefix_url = "https://od-api.oxforddictionaries.com/api/v1/entries/"
	suffix_url = "/definitions"

	def __init__(self):
		pass	
		
	def welcome(self):
		"""Introduction message"""

		print("--------------------------------------------------------------------------------")
		return "\t \t Welcome to the Online Oxford Dictionary"

	def search_word(self):
		"""Returns the English definition of a word"""

		print("--------------------------------------------------------------------------------")
		# Prompt the user for input
		self.word = input("Enter an English word to search for its meaning: ").lower()
		print("--------------------------------------------------------------------------------")
		print("")
		# Join the entire url
		self.url = self.prefix_url + self.language + self.word + self.suffix_url
		# Make a get request
		self.my_request = requests.get(self.url, headers = {"app_id": self.app_id, "app_key": self.app_key})
		# Convert our response to json format
		self.my_response = self.my_request.json()		

		return self.my_response

word = OnlineDictionary()
print(word.welcome())
print(word.search_word())
