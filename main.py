import requests
import time
import fade

def print_banner():
    text = """
  █████▒██▀███   ██▓▓█████  ███▄    █ ▓█████▄     ██▀███  ▓█████  ███▄ ▄███▓ ▒█████   ██▒   █▓▓█████  ██▀███  
▓██   ▒▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒░██   █▌   ▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█▒  ░▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌   ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░░▒████▓    ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
"""
    print(fade.purplepink(text))  

def get_friends(token):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v10/users/@me/relationships", headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print(" Invalid token")
    elif response.status_code == 429:
        print(" Too many requests")
    else:
        print(f" Unknown error: {response.text}")

    return []

def remove_friend(token, friend_id, friend_name):
    headers = {"Authorization": token}
    response = requests.delete(f"https://discord.com/api/v10/users/@me/relationships/{friend_id}", headers=headers)

    if response.status_code == 204:
        print(f" {friend_name} deleted.")
    else:
        print(f" {friend_name} failed deleting. error: {response.text}")

def main():
    print_banner()
    token = input("Token: ").strip()

    friends = get_friends(token)
    
    if not friends:
        print("No friends found.")
        return

    for friend in friends:
        friend_name = friend['user']['username']
        remove_friend(token, friend['id'], friend_name)
        time.sleep(0)

    friends_left = get_friends(token)
    print(f"Friends remaining: {len(friends_left)}")

    print(" https://github.com/dk6m")

if __name__ == "__main__":
    main()
