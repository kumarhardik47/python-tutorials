import os

class fruit:
	fruits = ["apple","mango","orange","banana","grapes"]
	prices = [200,60,50,40,90]

	def __init__(self):
		pass

	def get_fruit_price(self,fruit):
		return prices[ fruits.index(fruit) if fruits.index(fruit)]

	def get_fruit_name_list(self):
		return fruits

	def get_fruit_price_list(self):
		return prices


