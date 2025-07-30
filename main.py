import requests
import sys
import time
from datetime import datetime

def get_public_ip(retries=3, delay=2):
    for _ in range(retries):
        try:
            ip = requests.get("https://api.ipify.org", timeout=5).text
            return ip
        except requests.RequestException:
            time.sleep(delay)
    return None

def send_to_telegram(api_token, chat_id, message):
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(api_url, json=payload, timeout=5)
        response.raise_for_status()  # raise error for bad HTTP response
        print("Message sent successfully.")
        return True
    except requests.RequestException as e:
        print(f"Failed to send message: {e}")
        return False

def main():
    print("What do you want to send?")
    print("1: Your public IP address")
    print("2: A custom message")
    
    choice = input(">> ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice, exiting.")
        sys.exit(1)

    api_token = input('Enter your Telegram Bot API Token: ').strip()
    chat_id = input('Enter your Telegram Chat ID: ').strip()

    if choice == '1':
        ip = get_public_ip()
        if ip is None:
            print("Could not retrieve public IP address.")
            sys.exit(1)
        message = f"Public IP Address as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:\n{ip}"
    else:
        custom_message = input("Enter your custom message: ").strip()
        message = f"{custom_message}\nSent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    send_to_telegram(api_token, chat_id, message)
    print("Thank you for using the script. Goodbye!")

if __name__ == "__main__":
    main()
