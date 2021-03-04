from addons.handler import Handler as BaseHandler


class Handler(BaseHandler):

    def __init__(self):
        super(Handler, self).__init__()

    # 视频列表
    def video_list(self, request_url, request_content, response_content):
        print(self.parse_params(request_url))
        print(self.parse_query(request_content))
        print(response_content)

