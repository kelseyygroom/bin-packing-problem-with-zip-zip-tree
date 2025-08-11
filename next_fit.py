# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
	# don't need to use a bst to implement this; can iterate over items for O(n) runtime

	f = 0

	for index, item in enumerate(items):
		if (free_space == []):					# to handle first case where no bins exist
			free_space.append(round(1-item, 2))
			assignment[index] = f						
		elif free_space[f] >= item:
			# check if current bin fits the item
			free_space[f] = round(free_space[f] - item, 2)
			assignment[index] = f
		else:
			free_space.append(round(1-item, 2))
			f += 1
			assignment[index] = f
	return free_space
			
