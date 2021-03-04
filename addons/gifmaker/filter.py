import mitmproxy.http

from addons.filter import Filter as BaseFilter
from addons.gifmaker.handler import Handler


class Filter(BaseFilter):
    _domains = [
        'apis2.ksapisrv.com',
        'ksapisrv.com',
        'gifshow.com',
        'kwaizt.com',
        'yximgs.com',
        'gifmaker.com',
        'kuaishouzt.com'
    ]

    def __init__(self):
        super(Filter, self).__init__()

    def response(self, flow: mitmproxy.http.HTTPFlow):

        if not self.filter_domain(flow.request.host):
            return None

        request_url, request_content, response_content = self._get_request_data(flow)

        # 用户信息
        if self.is_user_info(request_url):
            return Handler().user_info(request_url, request_content, response_content)

        return None

    # 用户信息
    def is_user_info(self, url: str):
        return self.verify_url([
            'rest/n/user/profile/v2',
            'rest/n/user/profile/adBusiness'
        ], url)
