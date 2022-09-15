import time
import yaml

from datetime import date


class Post(object):
    def __init__(self, title, content, id=None, dt=None, links=[], tags=[]):
        self.id = id
        self.title = title
        self.content = content
        self.date = dt
        self.links = links
        self.tags = tags
        self.published = False

        if self.id is None:
            self.id = int(time.time())
        if self.date is None:
            self.date = str(date.today())

    def yaml(self):
        return yaml.dump(self.__dict__)

    @staticmethod
    def load(data):
        vals = yaml.safe_load(data)
        return Post(
            title=vals.get("title"),
            content=vals.get("content"),
            id=vals.get("id"),
            dt=vals.get("date"),
            links=vals.get("links"),
            tags=vals.get("tags"),
        )
