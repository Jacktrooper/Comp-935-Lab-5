import requests
from sys import argv
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'


def main():
    poke_list = search_for_pokemon(argv[1])
    if poke_list is not None:
        print(f'Name: {poke_list["name"]}')
    return
    
def search_for_pokemon(search_term):
    """Gets a list of dad jokes that have a term

    Args:
        search_term (str): pokemon

    Returns:
        str: returns the pokemons name
    """
    
    #steup the header parameters
    header_params = {
        'Accept' : 'application/json'
    }

    query_str_params = {
        'term' : search_term
    }

    #Send the GET request to the Dad jokes api
    print(f'Searching pokemon api for "{search_term}"...', end='')
    poke_url = f'{POKE_API_URL}{search_term}/'
    resp_msg = requests.get(poke_url, headers=header_params, params=query_str_params)
    
    if resp_msg.ok:
        print('success')
        poke_list = resp_msg.json()
        return poke_list
    else:
        print('falied')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
    return


if __name__ == '__main__':
    main()