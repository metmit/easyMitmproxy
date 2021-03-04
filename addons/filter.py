import mitmproxy.http

from utils.helper import Helper


class Filter(object):
    _domains = []

    def __init__(self):
        pass

    '''def request(self, flow: mitmproxy.http.HTTPFlow):
        # 这里配置二级代理的ip地址和端口
        if flow.live:
            proxy = ("12.33.44.55", 8888)
            flow.live.change_upstream_proxy_server(proxy)
    '''

    def filter_domain(self, host: str):
        """过滤域名
        """
        return Helper.list_in_str_or(self._domains, host)

    @staticmethod
    def verify_url(lists, url):
        """根据URL判断是否为当前请求
        """
        return Helper.list_in_str_or(lists, url)

    @staticmethod
    def verify_url_and(lists, url):
        """Url必须同时满足列表中的所有条件
        """
        return Helper.list_in_str_and(lists, url)

    @staticmethod
    def _get_request_data(flow: mitmproxy.http.HTTPFlow):
        # 请求地址
        request_url = flow.request.url

        # 请求内容
        try:
            request_content = flow.request.get_text()
        except Exception as e:
            request_content = ''

        # 响应内容
        try:
            response_content = flow.response.get_text()
        except Exception as e:
            response_content = ''

        return request_url, request_content, response_content
