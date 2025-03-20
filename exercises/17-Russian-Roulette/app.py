import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
	# ✅ ↓ your code here ↓ ✅
	bullet = spin_chamber()
	for i in range(0,5):
		if i == bullet:
			return "DIED"
		else:
			print("Still alive") 
	return "END"	


print(fire_gun())
