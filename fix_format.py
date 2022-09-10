
if __name__ == '__main__':
	
	path = "/home/taylorott/Documents/cube_analysis/cube_files/"

	fname = 'order_list_unformatted'

	ext = '.txt'

	out_file = 'order_list_formatted'

	g = open(path+out_file+ext, "w")

	with open(path+fname+ext) as f:
		cards = f.read().split('\n')

		i = 0
		while i < len(cards):
			card = cards[i]
			if card[0]=='\"':
				g.write(card[1:]+'\n')
			i+=1
	g.close()

	# card_dict = {}

	# collection = 'CommonUncommonCollection'
	# lands = 'land_list'

	# no_list = [collection,lands]

	# for cube in no_list:
	#  	with open(path+cube+ext) as f:
	#  		cards = f.read().split('\n')

	#  		for card in cards:
	#  			card_dict[card]=None

	# buy_list = []

	# for cube in cube_list:
	# 	with open(path+cube+ext) as f:
	#  		cards = f.read().split('\n')

	#  		for card in cards:
	#  			if card not in card_dict:
	#  				card_dict[card]=None
	#  				buy_list.append(card)




	# for card in buy_list:
	# 	f.write("1 ")
	# 	f.write(card)
	# 	f.write("\n")
	# f.close()
