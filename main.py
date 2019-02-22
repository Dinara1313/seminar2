from myclass import Mobile_phone
from mybox import MyBox

phone_1 = Mobile_phone()
phone_2 = Mobile_phone("red", "Apple", 64, 1)
phone_3 = Mobile_phone("black", "Samsung", 32, 2)
phone_4 = Mobile_phone("white", "Meizu", 64, 2)

mybox = MyBox()
mybox.add(1)
mybox.add(phone_1)
mybox.add(phone_2)
mybox.add(phone_3)
mybox.add(phone_4)

it = mybox.iterator()
for phone in it:
	phone.read_parameters()
	
mybox.remove(phone_2)

print(mybox.contains(phone_2))
print(mybox.len())

it = mybox.iterator()
for phone in it:
	phone.read_parameters()




