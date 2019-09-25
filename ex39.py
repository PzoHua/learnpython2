#_*_coding=utf-8_*_

class Song(object):                                                   # 定义一个类 （歌曲）
	
	def __init__(self, lyrics):                                         # 歌曲属性歌词 （需要两参数）
		self.lyrics = lyrics  
    
  def sing_me_a_song(self):                                           # 歌曲属性唱歌 （需要一个参数）
		for line in self.lyrics:  
			print line
			
happy_bday = Song(["Happy birthday to you",                           # 将happ_bday和 "Happy......there" 用Song函数连接
				"I don't want to get sued",
				"So I'll stop right there"])
				
bulls_on_parade = Song(["They rally around the family",               # 将 bulls_ong_parade 和 "They......shells" 用Song函数连接
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()                                           # 以happy_bday为参数运行 .sing_me_a_song()方法

bulls_on_parade.sing_me_a_song()                                      # 以bulls_on-parade为参数运行 .sing_me_a_song()方法
