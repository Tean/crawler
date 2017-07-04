from com.xcoupe.crawler.util import HtmlUtil


def get_def_url():
    return "http://dbd.jd.com"


def ana_page(url):
    html = HtmlUtil.get_html(url)
    print(html)

ana_page(get_def_url())