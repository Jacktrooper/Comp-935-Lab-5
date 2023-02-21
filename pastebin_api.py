import requests

DEVELOPER_KEY = '_exL1WGUbeOOcMsFpwjwutn8E4ywCF4b'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
   url = post_new_paste('this is the title', 'this is the body', '1H', True)
   print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """POST a new public paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body
        expiration (str, optional): Expiration date of paste N = Never 10M = 10 Minutes 1H = 1 Hour 1D = 1 Day 1W = 1 Week 2W = 2 Weeks 1M = 1 Month 6M = 6 Months 1Y = 1 Year. Defaults to '10M'.
        listed (bool, optional): _description_. Defaults to False.

    Returns:
        str: URL of the new paste, if successful. None if unsuccessful.
    """
    #setup the parameters for the request message
    paste_params = {
            'api_dev_key': DEVELOPER_KEY,
            'api_option': 'paste',
            'api_paste_code': body_text,
            'api_paste_name': title,
            'api_paste_expire_date': expiration,
            'api_paste_private': 0 if listed else 1
    }
    #Send the POST request to the Pastebin api
    print('Sending POST request to PasteBin API...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data = paste_params)

    
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    else:
        print('falied')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

if __name__ == '__main__':
    main()