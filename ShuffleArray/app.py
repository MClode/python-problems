from random import randint


class ShuffleArray:

	def get_random(self, floor, ceiling):
		return randint(floor, ceiling)
	
	def run(self, array):
		new_array = array[:]
		
		i = 0
		while i < len(new_array):
			key_to_pop = self.get_random(0, len(array)-1)
			popped = array.pop(key_to_pop)
			
			new_array[i] = popped
			
			i += 1
			
		return new_array
		
