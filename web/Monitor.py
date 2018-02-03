import json
import requests

response = requests.get()
json_data = json.loads(response.text)


def max_attribute(item):
	list = item['happiness'], item['angry'], item['sadness'], item['neutral']
	val = max(list)
	emotion = ''
	for i in range(list):
		if list[i] == val:
			if i == 0:
				emotion = 'happiness'
			elif i == 1:
				emotion = 'angry'
			elif i == 2:
				emotion = 'sadness'
			else:
				emotion = 'neutral'
	return emotion


def reactionClass():
	emoList = []
	for item in json_data['scores']:
		emoList.append(max_attribute(item))
	hash_map = {}
	for word in emoList:
		hash_map[word] = hash_map[word] + 1 if word in hash_map else 1

	star = 1
	for key, value in hash_map.items()
		value/length
	neutral = hash_map.get("neutral");
		if key == 'happiness': 
			if value >= 0.8 or neutral > 0.7:
				star = 5
			elif value >= 0.7 or neutral > 0.5:
				star = 4
			elif value >= 0.5 or neutral > 0.4:
				star = 3
			elif value >= 0.2 or neutral > 0.3:
				star = 2

	# with open('dict.csv', 'wb') as csv_file:
	# 	writer = csv_file.writer(csv_file)
	# for key, value in hash_map.items():
	# 	writer.writerow([key, value])
	return star
