import time
import frontmatter

from datetime import date


class MarkdownPost(frontmatter.Post):
    def __init__(self, title, content, id=None, dt=None):
        super().__init__(content=content, title=title, date=dt, published=False)

        if self.get("id") is None:
            self.metadata["id"] = int(time.time())
        if self.get("date") is None:
            self.metadata["date"] = str(date.today())
