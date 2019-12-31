from sklearn import tree

#properties of people and their classifications data set

#X contains height and weight in inches
X = []

#Y contains the gender associated with the height and weight
Y = []

data_set = {'male':[[66, 110], [99, 130], [123, 150], [54, 99], [153, 250]], 
			'female':[[52, 100], [62, 150], [56, 170], [90, 130]]}

def get_key_by_value(val):
	for key, values in data_set.items():
		for value in values:
			if(val == value):
				return key

for key, values in data_set.items():
	 for value in values:
	 	X.append(value)
	 	Y.append(get_key_by_value(value))

print(X)

print(Y)

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[160, 300], [45, 400]])

print(prediction)