import pickle

with open("profile.pickle", 'rb') as profile_file:
	print(pickle.load(profile_file))

with open("study.txt", "w", encoding='utf8') as study_file:
	study_file.write("I am studying Python hard.")
	
with open("study.txt", "r", encoding="utf8") as study_file:
	print(study_file.read())

with open('study_pickle.pickle', 'wb') as ILP:
	data = "no pain no gain"
	pickle.dump(data, ILP)
with open('study_pickle.pickle', 'rb') as ILP:
	print(pickle.load(ILP))
