
def get_cubes(cube_list):
	path = "/home/taylorott/Documents/cube_analysis/cube_files/"
	ext = '.txt'

	card_dict_list = []
	card_list_list = []

	count = 0
	for cube in cube_list:
		card_dict_list.append({})
		card_list_list.append([])

		with open(path+cube+ext) as f:
	 		cards = f.read().split('\n')
	 		for card in cards:
 				card_dict_list[count][card]=None
 				card_list_list[count].append(card)

		count+=1

	return card_dict_list,card_list_list

def build_freq_table(card_list_list):
	freq_table = {}
	key_list = []

	for i in range(len(card_list_list)):
		for card in card_list_list[i]:
			if card in freq_table:
				freq_table[card]+=1
			else:
				freq_table[card]=1
				key_list.append(card)

	return freq_table,key_list

def filter_threshold_owned(freq_table,key_list,threshold,my_collection):
	list_out = []
	for card in key_list:
		if freq_table[card]>=threshold and card in my_collection:
			list_out.append(card)

	return list_out

def write_to_file(list_in,fname):
	path = "/home/taylorott/Documents/cube_analysis/cube_files/"
	ext = '.txt'

	f = open(path+out_file+ext, "w")

	for card in list_in:
		# f.write("1 ")
		f.write(card)
		f.write("\n")
	f.close()

if __name__ == '__main__':
	
	
	cube_list = [
				 'AmazsPeasantCube',
				 'EvergreenCube',
				 'JankDiverPeasantCube',
				 'ThePeasantCube2022',
				 'TheSpootyPeasantcube',
				 'BigDiscardEnergy',
				 'Peasantish',
				 'RareBGone',
				 'WadesPeasantCube',
				 'DomsPeasantCube',
				 'KitchenfinksCube',
				 'Peasantville',
				 ]

	owned_list = [
 				  'CommonUncommonCollection',
 				  # 'recently_purchased',
 				  'OrionsPeasantCube'
 				  ]

	
	# card_dict_list,card_list_list = get_cubes(cube_list)

	owned_dict_list,owned_list_list = get_cubes(owned_list)

	list_out = []

	for card in owned_list_list[1]:
		if card not in owned_dict_list[0]:
			list_out.append(card)


	# freq_table,key_list = build_freq_table(card_list_list)
	# my_collection,dummy = build_freq_table(owned_list_list)

	# list_out = filter_threshold_owned(freq_table,key_list,4,my_collection)

	# print(len(list_out))

	# out_file = 'missing_cards_shipping'
	out_file = 'missing_cards_cube'

	write_to_file(list_out,out_file)
	



		 				