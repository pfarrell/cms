import time

from datetime import date


class Post():

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.date = kwargs.get('date')
        self.published = kwargs.get('published')
        self.links = kwargs.get('links')
        self.tags = kwargs.get('tags')
        self.file_name = kwargs.get('file_name')
        if(self.id is None):
            self.id = int(time.time())
        if(self.date is None):
            self.date = str(date.today())
        if(self.published is None):
            self.published = False


