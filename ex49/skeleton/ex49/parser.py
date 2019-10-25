#_*_coding=utf-8_*_

class ParserError(Exception):
	pass

class Sentence(object):
	
	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]

# 用 peek函数识别下一个单词类型
def peek(word_list):         # 例子：word_list = [('verb', 'open'), ('stop','the'), ('noun', 'door')]
	if word_list:            #
		word = word_list[0]  # word = ('verb', 'open')
		return word[0]       # word[0] = 'verb'
	else:
		return "错误1"

# 用 match函数匹配单词
def match(word_list, expecting):   # match(word_list, 'verb')
	if word_list:
		word = word_list.pop(0)    # 删除 word_list 中 ('verb', 'open')， 将其传递给 word

		if word[0] == expecting:   # word[0] = 'verb'
			return word            # 返回('verb', 'open')
		else:
			return "错误2"
		
	else:
		return "错误3"

# 用 skip函数筛选符合单词类型的单词，对其执行 match函数
def skip(word_list, word_type):
	while peek(word_list) == word_type: # peek(word_list)返回'verb'
		match(word_list, word_type)     # match 返回 ('verb', 'open')


# 用 parse_verb取出 verb类型的元组
def parse_verb(word_list):
    skip(word_list, 'stop')             # 用 skip函数筛选 stop类型的单词
    
    if peek(word_list) == 'verb':       # 如果下一个单词是 verb类型的单词，则匹配
        return match(word_list, 'verb') # verb，并返回值
    else:
        raise ParserError("Expected a verb next.")

# 用 parse_object函数筛选目标单词(名词和方向词)
def parse_object(word_list):
	skip(word_list, 'stop')    # 在单词列表(word_list)中筛选修饰词(stop)
	next = peek(word_list)     # 取出单词列表(word_list)中的第一个单词
	
	if next == 'noun':         
		return match(word_list, 'noun')       # 匹配名词
	if next == 'direction':
		return match(word_list, 'direction')  # 匹配方向词
	else:
		raise ParserError("Expected a noun or direction next.")

# 用 parse_subject函数得到三个值：subj由 parse_sentence 待定、动词、名词或方向词待定、动词、名词或方向词
def parse_subject(word_list, subj):
	verb = parse_verb(word_list)     # 动词
	obj = parse_object(word_list)    # 名词或方向词
	
	return Sentence(subj, verb, obj) #

# 用 parse_sentence函数获得三个值：
def parse_sentence(word_list):
	skip(word_list, 'stop')  # 跳过动词
	
	start = peek(word_list)  # 获得名词或动词
	
	if start == 'noun':                            # 如果是名词
		subj = match(word_list, 'noun')            # 获得名词的值给subj
		return parse_subject(word_list, subj)      # 调用 parse_subject 得到三个值
	elif start == 'verb':                          # 如果是动词
		# assume the subject is the player then (假设主题是玩家)
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, object, or verb not: %s" %
start)
