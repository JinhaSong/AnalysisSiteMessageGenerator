import requests
import json


class AnalysisSiteRequestGenerator :
    def __init__(self):
        self.__url = None
        self.__json_data = None
        self.__json_file = None

    def set_request_attr(self, url, image, modules=None):
        self.__url = url
        self.__json_file = {'image': image}
        if modules is not None :
            self.__json_data = {'modules':modules}
        else :
            self.__json_data = {}

    def get_request_attr(self):
        return self.__url, self.__json_data, self.__json_file

    def send_request_message(self):
        try :
            request = requests.post(url=self.__url, data=self.__json_data, files=self.__json_file)
            response = json.loads(request.content)
        except :
            response = {}

        return response

