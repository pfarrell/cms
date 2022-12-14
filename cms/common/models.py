import time
import frontmatter

from datetime import date


class MarkdownPost(frontmatter.Post):
    def __init__(self, kebab, title, content, id=None, dt=None):
        super().__init__(
            content=content, kebab=kebab, title=title, 
            date=dt, projectLink=None, summary="Write a summary", image="update me", headerImage=None
        )

        if self.get("id") is None:
            self.metadata["id"] = int(time.time())
        if self.get("date") is None:
            self.metadata["date"] = str(date.today())

    def __lt__(self, other):
        return self["date"] < other["date"]
