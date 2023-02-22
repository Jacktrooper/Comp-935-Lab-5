import requests

DAD_JOKE_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKE_SEARCH_URL = f'{DAD_JOKE_API_URL}search'


def main():
    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list, sep='\n')
    return
    
def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that have a term

    Args:
        search_term (str): cow

    Returns:
        str: returns the lsit of jokes
    """
    
    #steup the header parameters
    header_params = {
        'Accept' : 'application/json'
    }

    query_str_params = {
        'term' : search_term
    }

    #Send the GET request to the Dad jokes api
    print(f'Searching dad jokes api for "{search_term}" jokes...', end='')
    resp_msg = requests.get(DAD_JOKE_SEARCH_URL, headers=header_params, params=query_str_params)

    
    if resp_msg.ok:
        print('success')
        body_dic = resp_msg.json()
        jokes_list = [j['joke'] for j in body_dic['results']]
        return jokes_list['joke']
    else:
        print('falied')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
    return
def get_random_dad_joke():

    """Gets a random dad joke

    Returns:
        str: returns the dad joke
    """

    #steup the header parameters
    header_params = {
        'Accept' : 'application/json'
    }

    #Send the GET request to the Dad jokes api
    print('Sending POST request to PasteBin API...', end='')
    resp_msg = requests.get(DAD_JOKE_API_URL, headers=header_params)

    
    if resp_msg.ok:
        print('success')
        joke_dic = resp_msg.json()
        return joke_dic['joke']
    else:
        print('falied')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
    return


if __name__ == '__main__':
    main()