class Semaphore(object):

    def __init__(self, max):
        self._resources = 0
        self._max_resources = max

    def acquire(self):
        if self._resources < self._max_resources:
            self._resources += 1
            return True
        else:
            return False

    def release(self):
        self._resources -= 1
