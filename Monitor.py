# Hello World program in Python
    
print "Hello World!\n"
import json
import requests

response = requests.get()
json_data = json.loads(response.text)

def max_attribute(item):
    list = item['happiness'],item['angry'],item['sadness'],item['neutral']
    val = max(list)
    emotion=''
    for i in range(list):
        if list[i]==val:
            if i == 0:
                emotion='happiness'
            elif i == 1:
                emotion='angry'
            elif i==2:
                emotion='sadness'
            else:
                emotion = 'neutral'
    return emotion
    
def reactionClass():
    
    emoList = []
    for item in json_data['scores']:
        emoList.append(max_attribute(item))
    hash_map = {}
	for word in emoList:
		if word in hash_map:
            hash_map[word] = hash_map[word] + 1
        else:
            hash_map[word] = 1
	length = len(emoList)
	for key, value in sorted(hash_map.iteritems(), key=lambda (k,v): (v,k)):
		value/length
		if key=='happiness'
			if value >= 0.8 
				star = 5
			elif value >= 0.7
				star = 4
			elif value >= 0.5
				star = 3
			elif val >=0.2
				star = 2
			else:
				star = 1
	with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in hash_map.items():
       writer.writerow([key, value])
	return star
	
        

            


