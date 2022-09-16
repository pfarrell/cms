import sys
import frontmatter
from common.models import MarkdownPost


if __name__ == "__main__":
    filepath = sys.argv[1]
    title = sys.argv[2]

    post = MarkdownPost(title=title, content=None)
    with open(filepath, "w") as file:
        file.write(frontmatter.dumps(post))
