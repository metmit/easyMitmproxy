
import mitmproxy.http

from addons.filter import Filter as BaseFilter
from addons.aweme.handler import Handler


class Filter(BaseFilter):
    _domains = [
        'snssdk.com',
        'amemv.com',
        'aweme.com',
        'iesdouyin.com',
        'douyin.com',
    ]

    def __init__(self):
        super(Filter, self).__init__()

    def response(self, flow: mitmproxy.http.HTTPFlow):

        if not self.filter_domain(flow.request.host):
            return None

        request_url, request_content, response_content = self._get_request_data(flow)

        # 视频列表
        if self.is_video_list(request_url):
            return Handler().video_list(request_url, request_content, response_content)

        return None

    # 用户视频列表
    def is_video_list(self, url: str):
        return self.verify_url([
            'aweme/v1/aweme/post/?',
            'aweme/v2/aweme/post/?'
        ], url)
