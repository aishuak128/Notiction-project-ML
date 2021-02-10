import json


with open('new_train_examples.json') as f:
	data = json.load(f)

# print(type(data['bass_synthetic_068-049-025']))
# print(data['bass_synthetic_068-049-025'])

# keyboard_acoustic sifted through json
new_dict = dict()

for i in data:
	if 	'keyboard_acoustic_003' in i: continue
	if	'keyboard_acoustic_011' in i: continue
	if	'keyboard_acoustic_015' in i: continue
	if	'keyboard_acoustic_017'	in i: continue
	if	'keyboard_acoustic_018' in i: continue
	if	'keyboard_acoustic_020' in i: 
		# print(i + " suka")
		continue
	else:
		print(i)
		# print(data[i])
		# del i
		new_dict[i] = data[i]


print(len(new_dict))

# save to the file 

with open('new_train_examples2.json', 'w') as f:
	json.dump(new_dict, f, indent=4)
	

	# for name in data:
	# 	if 'keyboard_acoustic' in name:	
			# json.dump(name, f, indent=4)
			# print(f)

