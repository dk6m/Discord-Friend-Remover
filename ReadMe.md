
# Discord Friend Remover

This script removes all friends from a Discord account using the Discord API.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)
- `fade` library (install with `pip install fade`)
- A valid Discord user token

## Installation & Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/dk6m/discord-friend-remover.git
   cd discord-friend-remover
   ```
2. Install dependencies:
   ```sh
   pip install requests fade
   ```
3. Run the script:
   ```sh
   python main.py
   ```
4. Enter your Discord user token when prompted.

## How It Works
- The script fetches the list of friends using the Discord API.
- It iterates through each friend and sends a request to remove them.
- It prints the name of each removed friend and displays the number of friends left.

## Notes
- Using this script may violate Discord's terms of service.
- Be cautious when using your Discord token.

GitHub: [dk6m](https://github.com/dk6m)

