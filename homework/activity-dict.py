# Activité 3.1
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
print(mes_fruits) # {'poire': 3, 'pomme': 4, 'orange': 2}

# Activité 3.2
d = {"voiture": 25, "vélo": 55, "train": 20}
tr = d["vélo"]
print(tr) # 55

# Activité 3.3
tab = []
d = {"voiture": 25, "vélo": 55, "train": 20}
for t in d.values():
	if t < 40:
		tab.append(t)
print(tab) # [25, 20]

# Activité 3.4
tab = []
d = {"voiture": 25, "vélo": 55, "train": 20}
for v, t in d.items():
	if t < 40:
		tab.append(v)
print(tab) # ['voiture', 'train']

# Activité 3.5
tab = [{'nom': 'toto', 'num': 2}, {'nom': 'titi', 'num': 5}, {'nom': 'tata', 'num': 4}]
tab_nom = []

for t in tab:
	if t['num'] > 3:
		tab_nom.append(t['nom'])
print(tab_nom) # ['titi', 'tata']

# Activité 3.6
tab = [{'nom': 'Titi', 'note':12}, {'nom': 'Tutu', 'note':11}, {'nom': 'Toto', 'note':17}]

def plusHaute(tab):
	nom = ""
	max_note = 0
	for t in tab:
		if t['note'] > max_note:
			max_note = t['note']
			nom = t["nom"]
	return nom

print(plusHaute(tab)) # Toto

# Activité 3.7
tab = [{'nom': 'Titi', 'num':987675643}, {'nom': 'Tutu', 'num':424224}, {'nom': 'Toto', 'num':343235365}]

def numTel(n, tab_tel):
	for t in tab_tel:
		if n == t["nom"]:
			return t["num"]
	return -1

print(numTel("Tutu", tab)) # 424224
print(numTel("Tulu", tab)) # -1

# Activité 3.8
tab = [{'nom': 'Titi', 'note': 12}, {"nom": 'Tutu', "note":11}, {'nom': 'Toto', 'note':17}]

def sum(list):
	answer = 0
	for entry in list:
		answer += entry
	return answer

def moyenne(tab):
	notes = []
	for t in tab:
		notes.append(t["note"])
	moyenne = sum(notes) / len(notes)
	return moyenne

print(moyenne(tab)) # 13.333333333333334
