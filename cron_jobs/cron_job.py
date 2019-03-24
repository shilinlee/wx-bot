import time
import random
import itchat
import arrow
from cron_jobs.greetings_config import Morning

itchat.auto_login(enableCmdQR=2)

myself = itchat.search_friends()

search_friend = itchat.search_friends


def search_jlz(names=None):
    if not names:
        names = []
    jlz = None
    for name in names:
        jlz = search_friend(name)
        if jlz:
            break

    if not jlz:
        return None
    else:
        return jlz[0]


def get_morning_greeting():
    greeting = random.choice(Morning.greeting)
    return greeting


def get_random_clock(type):
    if type == "morning":
        hour = random.randrange(7, 9)
        minute = random.randrange(60)
        return hour, minute
    # elif type == "night":
    #     hour = random.randrange(7, 9)
    #     minute = random.randrange(60)
    #     return "{}:{}".format(hour, minute)


def main():
    while True:
        time.sleep(58)
        now = arrow.now()
        if (now.hour, now.minute) == get_random_clock("morning"):
            #  "A小傻子", "A大傻子", "A小可爱", "对不起，我取不出来名字了"
            jlz = search_jlz(names=["此账号存在异常"])
            greeting = get_morning_greeting()
            jlz.send(greeting)


if __name__ == '__main__':
    main()