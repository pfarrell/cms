import os
import sys
import frontmatter
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_markdown import MarkdownExtension


def load_post(filepath):
    file = frontmatter.load(filepath)
    return file


def get_posts(rootdir):
    posts = []
    for filename in [f for f in os.listdir(rootdir) if f.endswith(".yml")]:
        f = os.path.join(rootdir, filename)
        if os.path.isfile(f):
            post = load_post(f)
            posts.append(post)

    return posts


def render_site(rootdir):
    env = Environment(
        loader=FileSystemLoader("cms/templates"),
        autoescape=select_autoescape(),
        extensions=["jinja2_markdown.MarkdownExtension"],
    )
    template = env.get_template("post.html")

    # discover posts
    posts = get_posts("site")

    # convert posts to html
    for post in posts:
        with open(f"{rootdir}/{post['date']}-{post['kebab']}.html", "w") as file:
            rendered = template.render(content=post.content, devmode="true", **post)
            file.write(rendered)

    # build home page


if __name__ == "__main__":
    rootdir = sys.argv[1]
    render_site(rootdir)
