import sys
import subprocess


class Client(object):

    def __init__(self):
        self._video_playing = False

    def start_new_video(self, url):
        self._video_playing = True
        sys.stderr.write('Starting new video: {0}\n'.format(url))
        cmd = 'youtube-dl -q -o- {0} | mplayer -cache 8192  -'
        subprocess.call(cmd.format(url), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sys.stderr.write('Finished playing video.\n')
        self._video_playing = False

    @property
    def video_playing(self):
        return self._video_playing
