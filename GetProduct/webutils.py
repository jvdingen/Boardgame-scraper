from urllib.parse import urlparse

def get_domain(url):
        with_sub_domain = urlparse(url).netloc
        domain = '.'.join(with_sub_domain.split('.')[-2:])
        return domain