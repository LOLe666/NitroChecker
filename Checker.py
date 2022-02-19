import random, string
import requests


print("Starting...")



letters = string.ascii_letters
digits = string.digits
while True:
        nitro = (''.join(random.choice(letters + digits) for i in range(19)))

        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" The code is working! | https://discord.gift/{nitro}")
            break
        else:
            print(f" Code Isn't working | https://discord.gift/{nitro}")
