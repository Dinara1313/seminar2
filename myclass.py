class Mobile_phone:
	def __init__(self, color = "black", manufacturer = "Apple", memory = 16, number_of_sim_cards = 1):
		self.color = color
		self.manufacturer = manufacturer
		self.memory = memory
		self.number_of_sim_cards = number_of_sim_cards
		
	def change_parameters(self, color, manufacturer, memory, number_of_sim_cards):
		self.color = color
		self.manufacturer = manufacturer
		self.memory = memory
		self.number_of_sim_cards = number_of_sim_cards
		
	def read_parameters(self):
		print("Color:", self.color,\
			  "Manufacturer:", self.manufacturer,\
			  "Memory:", self.memory,\
			  "Number of sim-cards:", self.number_of_sim_cards)
			  
			   
				
		
