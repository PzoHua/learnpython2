
class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
				"I don't want o get sued",
				"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the familly",
				"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sker_boi = Song(["Sorry,well tough luck taht just boy!"])

sker_boi.sing_me_a_song()
