import sys
import subprocess


class Client(object):

    def __init__(self):
        self._video_playing = False

    def start_new_video(self, url):
        self._video_playing = True
        sys.stderr.write('starting new video {0}'.format(url))
        cmd = 'youtube-dl -q -o- {0} | mplayer -cache 8192  -'
        subprocess.call(cmd.format(url), shell=True)
        sys.stderr.write('finished playing video')
        self._video_playing = False

    @property
    def video_playing(self):
        return self._video_playing
