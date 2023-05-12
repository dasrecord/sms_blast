import requests
import time
import config

# Construct Webhook URL
url = f"https://maker.ifttt.com/trigger/{config.IFTTT_EVENT_NAME}/with/key/{config.MY_IFTTT_KEY}"

# Select Contact List 
file = "test_list.csv"

# Construct Message
premsg = """Hi {}, INSERT_MESSAGE_HERE"""

# Add Optional Footer
footer = """INSERT_FOOTER_TEXT_HERE***"""

with open(file, encoding="UTF-8") as list:
    for entry in list.readlines():
        name = entry.split(",")[0].split(" ")[0].strip()
        number = entry.split(",")[1].strip()
        msg = premsg.format(name).strip()
        params = {"value1": number, "value2": msg, "value3": footer}
        with open("sent.txt", "a") as sent:
            sent.writelines("\n")
            sent.writelines(name + "," + number)

        # Post Web Request
        # requests.post(url, params)

        # Display Message Confirmation
        print("Message sent to " + name + " at " + number)
        time.sleep(30)
    print("DONE")
