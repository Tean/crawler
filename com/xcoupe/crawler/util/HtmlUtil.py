from urllib import request


def get_html(url):
    response = request.urlopen("http://www.baidu.com")
    return response.read().decode()


def get_tag_from_html(html):
    # SGMLParser
    return

