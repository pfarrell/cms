import os
import sys
import frontmatter
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_markdown import MarkdownExtension
from rfeed import *
from datetime import datetime

def load_post(filepath):
    file = frontmatter.load(filepath)
    return file

def create_rss_item(post):
    link = f"https://patf.net/{post['date']}-{post['kebab']}.html"
    return Item(
            title = post['title'],
            link = link,
            description = post['summary'],
            author="mr.patfarrell@gmail.com (Patrick Farrell)",
            guid=Guid(link),
            pubDate = datetime.strptime(post['date'], '%Y-%m-%d')
            )


def get_posts(rootdir):
    posts = []
    feedItems = []

    for filename in [f for f in os.listdir(rootdir) if f.endswith(".yml")]:
        f = os.path.join(rootdir, filename)
        if os.path.isfile(f):
            post = load_post(f)
            posts.append(post)
            item = create_rss_item(post)
            feedItems.append(item)

    return posts, feedItems


def render_site(rootdir, sources):
    env = Environment(
        loader=FileSystemLoader("cms/templates"),
        autoescape=select_autoescape(),
        extensions=["jinja2_markdown.MarkdownExtension"],
    )
    template = env.get_template("post.html")

    # discover posts
    posts = []
    feedItems = []
    for source in sources:
        items = get_posts(source)
        posts.extend(items[0])
        feedItems.extend(items[1])


    # convert posts to html
    for post in posts:
        rendered = template.render(content=post.content, **post)
        with open(f"{rootdir}/{post['date']}-{post['kebab']}.html", "w") as file:
            file.write(rendered)

    # sort posts
    posts.sort(key=lambda x: x["date"], reverse=True)

    # build home page
    template = env.get_template("index.html")
    rendered = template.render(posts=posts)
    with open(f"{rootdir}/index.html", "w") as file:
        file.write(rendered)

    # publish rss feed
    feedItems.sort(key=lambda x: x.pubDate, reverse=True)
    feed = Feed(
            title="The Farrellel Postulate",
            link = "https://patf.net/rss.xml",
            description="",
            language="en-US",
            lastBuildDate = datetime.now(),
            items = feedItems)
    with open(f"{rootdir}/rss.xml", "w") as file:
        file.write(feed.rss())

if __name__ == "__main__":
    rootdir = sys.argv[1]
    mode = sys.argv[2]
    if(mode == 'dev'):
        render_site(rootdir, ['drafts', 'site'])
    else:
        render_site(rootdir, ['site'])

