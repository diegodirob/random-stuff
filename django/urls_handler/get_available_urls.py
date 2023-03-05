# Not mine but usefull

from django.conf import settings
from django.urls import URLPattern, URLResolver


def get_available_urls():
    urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])

    def retrieve_urls(lis, acc=None):
        if acc is None:
            acc = []
        if not lis:
            return
        l = lis[0]
        if isinstance(l, URLPattern):
            yield acc + [str(l.pattern)]
        elif isinstance(l, URLResolver):
            yield from retrieve_urls(l.url_patterns, acc + [str(l.pattern)])
        yield from retrieve_urls(lis[1:], acc)

    urls = map(lambda row: ''.join(row), retrieve_urls(urlconf.urlpatterns))

    urls = filter(lambda row:
                  not row.startswith('__debug__') and
                  not row.startswith('admin') and
                  not row.startswith('api') and
                  not row.startswith('^') and
                  not row.endswith('<pk>'), urls
                  )

    urls = map(lambda row: '/' + row, urls)

    return list(urls)

