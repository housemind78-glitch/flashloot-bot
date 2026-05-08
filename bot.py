import requests
import random

BOT_TOKEN = "8703751712:AAGDB_XXc_ueR9s8MrXQ03JuosOixgMVy0c"
CHAT_ID = "@FlashLootDealsa"

deals = [
    "https://amzn.to/3OUEjEe",
    "https://amzn.to/49pkvQb",
    "https://amzn.to/4d8Bfw5"
]

messages = [
    "🔥 FLASH DEAL ALERT\n⚡ Limited Time Offer\n👉 {}",
    "💸 HOT DEAL LIVE\n🛍️ Grab Fast\n👉 {}",
    "⚡ MEGA OFFER\n🔥 Limited Stock\n👉 {}"
]

link = random.choice(deals)
message = random.choice(messages).format(link)

url = f"https://api.telegram.org/bot{8242223953:AAHwT4z3k2P4Gd5eO_t0B1CQdFu92XuUbZ4}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
