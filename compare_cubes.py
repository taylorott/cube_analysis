
if __name__ == '__main__':
	
	path = "/home/taylorott/Documents/cube_analysis/cube_files/"

	cube_list = ['AmazsPeasantCube',
				 'EvergreenCube',
				 'JankDiverPeasantCube',
				 'ThePeasantCube2022',
				 'TheSpootyPeasantcube']

	ext = '.txt'

	card_dict = {}

	collection = 'CommonUncommonCollection'
	lands = 'land_list'

	no_list = [collection,lands]

	for cube in no_list:
	 	with open(path+cube+ext) as f:
	 		cards = f.read().split('\n')

	 		for card in cards:
	 			card_dict[card]=None

	buy_list = []

	for cube in cube_list:
		with open(path+cube+ext) as f:
	 		cards = f.read().split('\n')

	 		for card in cards:
	 			if card not in card_dict:
	 				card_dict[card]=None
	 				buy_list.append(card)


	out_file = 'purchase_list'

	f = open(path+out_file+ext, "w")

	for card in buy_list:
		f.write("1 ")
		f.write(card)
		f.write("\n")
	f.close()
