import json
import requests
import urllib
import urllib.parse


class Telegram:
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    URL = "https://api.telegram.org/bot{}/".format(TOKEN)

    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = Telegram().get_url(url)
        js = json.loads(content)
        return js

    def chunks(self, s, n):
        for start in range(0, len(s), n):
            yield s[start:start+n]

    def send_message(self, text, chat_id):
        if len(text) > 4096:
            for chunk in self.chunks(text, 4095):
                chunk = urllib.parse.quote(chunk)
                url = Telegram.URL + \
                    "sendMessage?text={}&chat_id={}".format(chunk, chat_id)
                Telegram().get_url(url)
        else:
            text = urllib.parse.quote(text)
            url = Telegram.URL + \
                "sendMessage?text={}&chat_id={}".format(text, chat_id)
            Telegram().get_url(url)

    def get_updates(self, offset=None):
        url = Telegram.URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        js = Telegram().get_json_from_url(url)
        return js

    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)

    def get_chat_id_and_text(self, updates, x):
        last_update = x
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        text = updates["result"][last_update]["message"]["chat"]["text"]
        try:
            username = updates["result"][last_update]["message"]["chat"]["username"]
        except:
            username = ""
        return (text, chat_id, username)

    def get_last_chat_id_and_text(self, updates):
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        try:
            username = updates["result"][last_update]["message"]["chat"]["username"]
        except:
            username = ""
        return (text, chat_id, username)
