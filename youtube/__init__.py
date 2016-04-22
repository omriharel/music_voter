import time
import sys
import subprocess

url = 'https://www.youtube.com/watch?v=CevxZvSJLk8'
class Client(object):

    def start_new_video(self, semaphore, url):
        sys.stderr.write('starting new video {0}'.format(url))
        if semaphore.acquire():
            cmd = 'youtube-dl -q -o- {0} | mplayer -cache 8192  -'
            subprocess.call(cmd.format(url), shell=True)
            sys.stderr.write('finished playing video')
            semaphore.release()
        else:
            sys.stderr.write('Adding to queue')
