<h1><b>Telegram Public IP Notifier</b></h1><br>
A simple Python script to fetch your current public IP address and send it as a message to a specified Telegram chat via a bot. The script also supports sending custom messages and includes basic error handling and retries.

<h3><b>Features</b></h3><br>
Retrieves the public IP address using the api.ipify.org service.

Sends messages to Telegram using the official Bot API.

Supports sending either the current public IP or a custom user-defined message.

Includes retry logic for network requests.

Displays timestamps in messages for better tracking.

User-friendly input prompts for Telegram Bot Token and Chat ID.

Basic input validation and error handling.

<h3><b>Use Cases</b></h3><br>
Keep track of dynamic public IP addresses remotely.

Receive instant notifications about your network status.

Send custom alerts or messages to Telegram.

<h3><b>Requirements</b></h3><br>
Python 3.x

requests library (pip install requests)

<h3><b>How to Use</b></h3><br>

1. Create a Telegram bot and obtain the Bot API Token.

2. Get your Telegram chat ID.

3. Run the script and follow the prompts to send your public IP or a custom message to Telegram.
