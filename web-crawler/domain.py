from urllib.parse import urlparse


def get_domain_name(url):
    try:
        result = get_sub_domain(url).split('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''


def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
