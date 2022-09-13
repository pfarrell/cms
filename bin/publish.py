from jinja2 import Environment, PackageLoader, select_autoescape


def render_site():
    env = Environment(loader=PackageLoader("cms"), autoescape=select_autoescape())

    template = env.get_template('template.html')

    html_template_string = template.render(name = "Pat")

    print(html_template_string)


if(__name__ == '__main__'):
    render_site()
