import emailer
import advice
import schedule
import time
import configuration


def send(msg, number):
    to = str(number)
    emailer.email_alert('daily quote', msg, to)

def run():
    tl = configuration.phone_numbers
    msg = advice.rendmsg()

    for x in tl:
        print(str(x))
        send(msg, x)
        print("done")
time_to_run = configuration.time_to_run
schedule.every().day.at(time_to_run).do(run)
while 1:
    schedule.run_pending()
    time.sleep(1)