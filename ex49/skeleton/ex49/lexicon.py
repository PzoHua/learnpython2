#_*_coding=utf-8_*_

# 需要测试的ex48下的lexicon.py文件
# 需要测试 direction verbs stop noun number error

def scan(sentence):

    result = []
    words = sentence.split()
    
    for word in words:
    
        if word in ['north', 'south', 'east', 'west']:
            result.append(('direction', word))

        elif word in ['go', 'kill', 'eat', 'stop', 'open']:
            result.append(('verb', word))

        elif word in ['the', 'in', 'of', 'from', 'at']:
            result.append(('stop', word))

        elif word in ['bear', 'princess', 'door', 'cabinet']:
            result.append(('noun', word))
            
        elif convert_number(word):
            result.append(('number', convert_number(word)))
            
        else:
            result.append(('error', word))
            
    return result

def convert_number(s):

	try:
		return int(s)
	except ValueError:
		return None
