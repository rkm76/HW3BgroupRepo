import random
import pandas as pd
from matplotlib import pyplot as plt

def create_new_architecture():
	architecture = {}
	architecture['D1'] = get_D1_choice()
	architecture['D2'] = get_D2_choice()
	architecture['D3'] = random.choice(D3_choices)
	architecture['D4'] = random.choice(D4_choices)
	architecture['D5'] = random.choice(D5_choices)
	architecture['D6'] = get_D3_choice()
	architecture['D7'] = random.choice(D7_choices)
	result = architecture_already_generated(architecture)
	if result:
		print(architecture)
	return architecture


def architecture_already_generated(architecture):
	for old_arch in architectures:
		all_decisions_same = True
		for decision in architecture:
			if old_arch[decision] != architecture[decision]:
				all_decisions_same = False
				break

		if all_decisions_same:
			return True

	return False

def get_D1_choice():
	choice = 000000
	choices = [0, 1, 2, 3, 4, 5]
	random.shuffle(choices)
	for c in choices[:4]:
		choice += 10 ** c
	return choice


def get_D2_choice():
	choice = 000
	flip_first = random.random()
	if flip_first > 0.5:
		choice += 1
	flip_second = random.random()
	if flip_second > 0.5:
		choice += 10
	flip_third = random.random()
	if flip_third > 0.5:
		choice += 100
	return choice


def get_D3_choice():
	choice = 000
	flip_first = random.random()
	if flip_first > 0.5:
		choice += 1
	flip_second = random.random()
	if flip_second > 0.5:
		choice += 10
	flip_third = random.random()
	if flip_third > 0.5:
		choice += 100
	return choice


def plot_distribution():
	fig, axs = plt.subplots(7)
	fig.suptitle('Decision Frequencies')
	plot_number = 0
	width = 500
	for d in occurrences:
		print(occurrences[d].values())
		# plt.title(d)
		# plt.xlabel("Decision")
		# plt.ylabel("Occurrences")
		axs[plot_number].bar(occurrences[d].keys(), occurrences[d].values(), width=width)
		width = 0.8
		plot_number += 1
	plt.show()


D1_choices = [] # 6-digit binary num, 4 digits are 1, 2 digits are 0
D2_choices = [] # 3-digit binary num, any
D3_choices = [1, 2, 3, 4] 
D4_choices = [1, 2]
D5_choices = [1, 2, 3]
D6_choices = [] # 3-digit binary num, any
D7_choices = [1, 2]

N = 100

# create architectures:
architectures = []
for n in range(N):
	architecture = create_new_architecture()
	architectures.append(architecture)
	
# analyze the randomness:
occurrences = {'D1': {}, 'D2': {}, 'D3': {}, 'D4': {}, 'D5': {}, 'D6': {}, 'D7': {}}
for a in architectures:
	for d in a:
		choice = a[d]
		if choice in occurrences[d]:
			occurrences[d][choice] += 1
		else:
			occurrences[d][choice] = 1

output = pd.DataFrame()
for a in architectures:
	output = output.append(a, ignore_index=True)

output.to_csv('architectures.csv')

