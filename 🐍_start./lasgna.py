EXPECTED_BAKE_TIME = 40; 
def bake_time_remaining(baked_time):
	"""this function takes minutes the lasagna has been baking as the argument and Calculates the remaining time but subtraction from the excepted lasagna baking time for the book"""
	remaining_time = (EXPECTED_BAKE_TIME - baked_time);
	return remaining_time;
def preparation_time_in_minutes(layers_number):
	"""This function takes number of layers of the lasagna as the argument and the calculates the total preparation time of the lasagna."""
	each_layer = 2;
	making_time = (each_layer * layers_number);
	return making_time;
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
	"""This function takes number of layers & elapsed baking time as arguments to calculate the total cooking time """
	total_cooking_minutes = (preparation_time_in_minutes(number_of_layers) + elapsed_bake_time);
	return total_cooking_minutes;
	
	