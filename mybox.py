from myclass import Mobile_phone
from myboxiterator import MyBoxIterator

class MyBox:
	def __init__(self):
		self.box = list()
	
	def len(self):
		return len(self.box)
	
	def add(self, obj):
		if type(obj) is Mobile_phone:
			if obj in self.box:
				print("This object is already contained in box")
			else:
				self.box.append(obj)
		else:
			print("This object is not a suitable type")
			
	def remove(self, obj):
		if obj in self.box:
			self.box.remove(obj)
		else:
			print("This object is not contained in box")
			
	def contains(self, obj):
		if obj in self.box:
			return True
		return False
		
	def iterator(self):
		return MyBoxIterator(self.box)
			
	
		
					
		
