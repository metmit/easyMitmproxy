import urllib.parse


class Helper:

    @staticmethod
    def parse_params(url: str):
        """从Url中取出query参数
        """
        return Helper.parse_query(urllib.parse.urlsplit(url).query)

    @staticmethod
    def parse_query(query: str):
        """格式化query参数为字典
        """
        return dict(urllib.parse.parse_qsl(query))

    @staticmethod
    def list_in_str_or(lists, string):
        """列表的 任一元素 包含在字符串中
        """
        for val in lists:
            if val in string:
                return True
        return False

    @staticmethod
    def list_in_str_and(lists, url):
        """列表的 所有元素 都必须包含在字符串中
        """
        res = False
        for val in lists:
            if val in url:
                res = True
            else:
                return False
        return res
