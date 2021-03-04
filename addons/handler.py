
from utils.helper import Helper


class Handler(object):

    def __init__(self):
        pass

    @staticmethod
    def parse_params(url: str):
        return Helper.parse_params(url)

    @staticmethod
    def parse_query(query: str):
        return Helper.parse_query(query)
