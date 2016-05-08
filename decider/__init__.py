import Queue
import time
import sqlite3

import youtube
import semaphore


class Sqlite3Wrapper(object):
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._cursor = self._conn.cursor()

    def get_rows(self, table_name, column_name, greater_than_value):
        query = 'SELECT * FROM {0} WHERE {1} > {2} ORDER BY id'.format(table_name,
                                                                       column_name,
                                                                       greater_than_value)
        return self._cursor.execute(query)

    def close(self):
        self._conn.close()


class Song(object):

    def __init__(self, title, link, votes):
        self._title = title
        self._link = link
        self._votes = votes

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    @property
    def votes(self):
        return self._votes

    def __cmp__(self, other):
        return cmp(self.votes, other.votes)


class Decider(object):

    def __init__(self, youtube_client, db_client):
        self._songs_playing = semaphore.Semaphore(1)
        self._youtube = youtube_client
        self._db = db_client
        self._priority_queue = Queue.PriorityQueue()
        self._priority_queue.put(Song('Shia',
                                      'https://www.youtube.com/watch?v=o0u4M6vppCI',
                                      1000))
        self._last_id = 0

    def _populate_queue(self):
        rows = self._db.get_rows('songs', 'id', self._last_id)
        if rows is not None:
            for row in rows:
                self._last_id = row[0]
                self._priority_queue.put(Song(row[1], row[2], row[3]))

    def run(self):
        while True:
            try:
                self._populate_queue()
                if self._songs_playing.acquire():
                    try:
                        next_song = self._priority_queue.get(block=False)
                        if next_song is not None:
                            print next_song.title
                            self._youtube.start_new_video(next_song.link)
                    except Queue.Empty:
                        print 'No songs, playing Shia'
                elif self._youtube.video_playing is not True:
                    self._songs_playing.release()
                time.sleep(5)
            except (KeyboardInterrupt, SystemExit):
                self._db.close()
                raise

if __name__ == '__main__':
    youtube_client = youtube.Client()
    sql_client = Sqlite3Wrapper('/tmp/music_voter.db')
    d = Decider(youtube_client, db_client=sql_client)
    try:
        d.run()
    except (KeyboardInterrupt, SystemExit):
        print 'Exited the Decider'
