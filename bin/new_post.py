import sys
import yaml
from common.models import Post


if(__name__ == '__main__'):
    filepath = sys.argv[1]
    contentpath = sys.argv[2]
    title = sys.argv[3]

    post = Post(title=title, content=contentpath)

    stream = open(filepath, "w")
    yaml.dump(post.__dict__, stream)


                
