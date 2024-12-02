import requests
import time
import random

def print_art():
    art = """
██████╗ ███████╗██╗      ██████╗ ██████╗  █████╗ ███╗   ███╗
██╔══██╗██╔════╝██║     ██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██║  ██║█████╗  ██║     ██║  ███╗██████╔╝███████║██╔████╔██║
██║  ██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
██████╔╝███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                             """

    print("\033[32m" + art + "\033[0m")

    print("создатель: KPACHOE_O3EPO")



def send_complaint():
    user_name = input("Ник нейм жертвы: ")
    group_chat = input("ссылка на чат/нарушение: ")
    date_time = input("дата и время нарушения: ")

    complaint_template = """
Subject: Immediate Action Required - User Abuse

Dear Telegram Support,

I am writing to report a user who has insulted me on Telegram. Here are the details:

- Username: {username}
- Group/Chat: {group}
- Date and Time: {date_time}

Please take immediate action to remove this user from the platform. I have attached screenshots of the offensive messages for your review.

Thank you for your prompt attention to this matter.

[+] 1. Snooping account
"""

    complaint_message = complaint_template.format(username=user_name, group=group_chat, date_time=date_time)

    emails = [
    'vadim@gmail.com', 'email2@example.com', 'email3@example.com',
    'dch72gorod@mvd.ru', 'dch_09@vol.mvd.ru', 'deg_uvd@vol.mvd.ru',
    'dchmvd@yfa.mvd.ru', 'dchguvd@yandex.ru', 'dchguvd@per.mvd.ru',
    'strgovd@yfa.mvd.ru', 'krasnoeozero5@gmail.com', 'fcb@gmail.com',
    'vvputin@gmail.com', 'dvd@gmail.com', 'sachatr43@gmail.com',
    'poit678@gmail.com', 'eagiseva41@gmail.com', '89504654534@temp.ru',
    'telegram@gmail.com', 'magomedmagomed58341@gmail.com'
]

    phones = [
    '+79999639466', '+73832327089', '+78002242222', '+74952242222',
    '+74956677264', '+73452799802', '+73452291600', '+73432941421',
    '+73433588177', '+78442930111', '+78442946698', '+3472793902',
    '+3472734760', '+73422467700', '+73473204534', '+73473439161',
    '+79161234567', '+79504654534', '79999939919', '+79524362819'
]

    while True:
        contacts = emails + phones
        random.shuffle(contacts)
        for contact in contacts:
            data = {'message': complaint_message, 'contact': contact}
            response = requests.post('https://telegram.org/support', data=data)
            print(f"\033[31m[+] жалоба отправлена на {contact}\033[0m")
            time.sleep(0.3)  # Delay to prevent spamming

def main():
    print_art()
    while True:
        send_complaint()

if __name__ == "__main__":
    main()