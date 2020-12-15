from controller.telegram import Telegram
from repository.todo import todoRepository
import time


class usecaseListenUpdate:
    def listenUpdates(self):
        last_update_id = None
        while True:
            updates = Telegram().get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = Telegram().get_last_update_id(updates) + 1
                text, chat, username = Telegram().get_last_chat_id_and_text(
                    Telegram().get_updates())
                todo = text.split('|')
                title = todo[0]
                note = todo[1]
                text_send = todoRepository(title, note).create()
                Telegram().send_message(text_send, chat)
            time.sleep(0.3)
