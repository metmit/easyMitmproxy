import mitmproxy.http

from addons.filter import Filter as BaseFilter

from addons.red.handler import Handler


class Filter(BaseFilter):
    __domains = [
        'xiaohongshu.com',
        'hongshu.com'
    ]

    def __init__(self):
        super(Filter, self).__init__()

    def response(self, flow: mitmproxy.http.HTTPFlow):

        if not self.filter_domain(flow.request.host):
            return None

        request_url, request_content, response_content = self._get_request_data(flow)

        # feed
        if self.is_feed(request_url):
            return Handler().feed(request_url, request_content, response_content)

    # feed 流
    def is_feed(self, url: str):
        return self.verify_url([
            'api/sns/v6/homefeed',
            '/homefeed'
        ], url)
