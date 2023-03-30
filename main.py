import requests
# import the API Token and ID from creds.py module
# please use your own ID, API Token in that module
# Please see https://core.telegram.org/bots/faq to obtain the API TOKEN
# import API Token and user ID from cred.py module
# I might not upload it into remote git
from cred import token_id

# REMINDER!
# Bot can't talk to bot
# Therefore you have to use non-bot ID
# use userinfobot in your telegram app to obtain your ID (non-bot)
# If you insist on using the bot ID, it will produce error code 403

# You might want to fill in your API TOKEN, and chat_id (user ID)
TOKEN = token_id.TOKEN
chat_id = token_id.chat_id


url = f"https://api.telegram.org/bot{TOKEN}/getMe"
print(requests.get(url).json())

message = "hello from your telegram bot"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message

# def send_to_telegram(message):

#     apiToken = '6065004786:AAErNReUq76J2G7_mUGkO62rWNqG2fVZW44'
#     # chatID = '6065004786'
#     chatID = '589156835'
#     apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

#     try:
#         response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
#         print(response.text)
#     except Exception as e:
#         print(e)

# send_to_telegram("Hello from Python!")