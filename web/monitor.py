
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


def build_response(json_data):
    emoList = [] 
    for item in json_data['scores']:
        emoList.append(max_attribute(item))
    hash_map = {}
    for word in emoList:
        if word in hash_map:
            hash_map[word] = hash_map[word] + 1
        else:
            hash_map[word] = 1
    return hash_map
