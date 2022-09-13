import sys
from common.post import Post


if(__name__ == '__main__'):
    post = Post(title=sys.argv[2], file_name=sys.argv[1])
    template = f"""id: {post.id} 
title: {post.title}
date: {post.date}
published: {post.published}
lines: []
tags: []
summary_text:
summary_image:
file_name: {post.file_name}
content:
"""
    with open(post.file_name, "w") as file:
        file.write(template)



