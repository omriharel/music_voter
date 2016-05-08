
## MAC OSX:
	* sudo brew install mplayer
	* sudo curl https://yt-dl.org/downloads/2016.04.19/youtube-dl -o /usr/local/bin/youtube-dl
	* sudo chmod a+rx /usr/local/bin/youtube-dl
	* cd music_voter && sqlite3 /tmp/music_voter.db < schema.sql
	
## Start Server (only allows putting new items to db)
	* python server.py
	
## Start The Decider (fetches from db and decides what to play)
	* python decider/__init__.py
