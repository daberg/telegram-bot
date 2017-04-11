import http.client
import json
import time


class AbstractClient:


    def __init__(self, token):

        self.TOKEN = token

        self.API_URL = "api.telegram.org"

        self.LP_TIMEOUT = 3600

        self.QUERY_BASE = "/bot" + self.TOKEN
        self.LONG_POLL = self.QUERY_BASE + "/getUpdates?timeout=" + str(self.LP_TIMEOUT)
        self.SEND_MESSAGE = self.QUERY_BASE + "/sendMessage"

        self.connection = http.client.HTTPSConnection(self.API_URL)

    
    def _get_updates(offset=None):

        req_url = self.LONG_POLL
        
        if offset is not None:
            req_url = req_url + "&offset=" + str(offset)

        self.connection.request("GET", req_url)
        response = connection.getresponse()

        raw_content = response.read()

        content = raw_content.decode("utf8")

        json_content = json.loads(content)

        if "result" in json_content:
            return json_content["result"]

        else:
            return None


    def send_message(text, chat_id):
        pass


    def start_polling():

        while True:

            max_update_id = -1

            if max_update_id < 0:
                updates = _get_updates()

            else:
                updates = _get_updates(max_update_id)

                if updates is not None:
                    max_update_id = -1

            for update in updates:

                handle(update['message'])

                update_id = update['update_id'] 
                if update_id > max_update:
                    max_update_id = update_id


    def handle_message(message):
        pass


