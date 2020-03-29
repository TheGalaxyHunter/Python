import json
import requests
import time
import urllib.parse
from sympy import *

# from dbhelper import DBHelper
#
# db = DBHelper()

TOKEN = "1022850309:AAFAnnPB6xBqVjqneoXM4DOknARaUw0dKVQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def handle_updates(updates):
    for update in updates["result"]:
        text = str(update["message"]["text"])
        chat = update["message"]["chat"]["id"]
        text = text.lower()
        # items = db.get_items(chat)  ##

        # if name == []:
        #     send_message("What's your name, Human?", chat)
        #
        #     send_message("Hello, " + str(name[0]) + '.', chat)

        # if text == "/done":
        #     keyboard = build_keyboard(items)
        #     send_message("Select an item to delete", chat, keyboard)
        if text == "/start":
            send_message("Welcome to your Personal Assistant.", chat)
            send_message("How can I help you Sir?", chat)
        elif text.startswith("/"):
            continue
        # elif text in items:
        #     db.delete_item(text, chat)  ##
        #     items = db.get_items(chat)  ##
        #     keyboard = build_keyboard(items)
        #     send_message("Select an item to delete", chat, keyboard)
        else:
            process_text(text, chat)
            # db.add_item(text, chat)  ##
            # items = db.get_items(chat)  ##
            # message = "\n".join(items)
            # send_message(message, chat)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def process_text(input, chat):
    try:
        # if 'search' in input or 'play' in input:
        #     # a basic web crawler using selenium
        #     search_web(input)
        #     return
        if "who are you" in input or "define yourself" in input:
            msg = "I am your personal Assistant. I am here to make your life easier. You can command " \
                  "me to perform various tasks such as calculating sums or opening applications etcetra"
            send_message(msg, chat)
            return

        elif "who made you" in input or "created you" in input:
            msg = "I have been created by Ankit Das."
            send_message(msg, chat)
            return

        elif "geeksforgeeks" in input:  # just
            msg = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            send_message(msg, chat)
            return

        elif "calculate" in input.lower():
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            str_expr = ''.join(query)
            expr = sympify(str_expr)
            msg = "The answer is " + str(expr)
            send_message(msg, chat)
            return

        elif "integrate" in input.lower():
            indx = input.lower().split().index('integrate')
            query = input.split()[indx + 1:]
            str_expr = ''.join(query)
            str_expr = "integrate("+str_expr+", x)"
            expr = sympify(str_expr)
            msg = "The answer is " + str(expr)
            send_message(msg, chat)

        elif "differentiate" in input.lower():
            indx = input.lower().split().index('differentiate')
            query = input.split()[indx + 1:]
            str_expr = ''.join(query)
            str_expr = "diff("+str_expr+", x)"
            expr = sympify(str_expr)
            msg = "The answer is " + str(expr)
            send_message(msg, chat)

        # elif 'open' in input:
        #
        #     # another function to open
        #     # different application availaible
        #     open_application(input.lower())
        #     return

        else:

            msg = "I can search the web for you, Do you want to continue?"
            send_message(msg, chat)
            # main()
            # if 'yes' in input or 'yeah' in input:
            #     # search_web(input)
            #     return
            # else:
            #     return
            return

    except:
        msg = "I don't understand, I can search the web for you, Do you want to continue?"
        send_message(msg, chat)
        # main()
        # if 'yes' in input or 'yeah' in input:
        #     # search_web(input)


def main():
    # db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)

        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


name = []

if __name__ == '__main__':
    main()


# def get_yes_no(updates):
#     for update in updates["result"]:
#         text = update["message"]["text"]
#         return text
