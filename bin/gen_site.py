import os
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_markdown import MarkdownExtension
from common.models import Post


def file_to_post(filepath):
    stream = open(filepath, 'r')
    file = Post.load(stream)
    return file

def load_content(filepath):
    with open(filepath) as file:
        return file.read()

def get_posts(rootdir):
    posts = []
    for filename in [f for f in os.listdir(rootdir) if f.endswith('.yml')]:
        f = os.path.join(rootdir, filename)
        if os.path.isfile(f):
            post=(file_to_post(f))
            post.content = load_content(post.content)
            posts.append(post)

    return posts


def render_site():
    env = Environment(
            loader=FileSystemLoader("cms/templates"), 
            autoescape=select_autoescape(),
            extensions=['jinja2_markdown.MarkdownExtension'],
    )
    template = env.get_template("post.html")

    # discover posts
    posts = get_posts("site")
    
    # convert posts to html
    for post in posts:
        print(template.render(post.__dict__))

    # build home page


if(__name__ == '__main__'):
    render_site()
    
