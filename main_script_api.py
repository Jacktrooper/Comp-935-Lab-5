from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys

def main():
    search_term = get_search_term()
    poke_list = search_for_pokemon(search_term)
    if poke_list:
        title, body_text = get_paste_data(poke_list, search_term)
        new_paste_url = new_paste(title, body_text)
        print(f'If needed URL od new past: {new_paste_url}')
        

    return

def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_data(poke_list, search_term):
    poke_name = poke_list['name'].lower()
    poke_abilities = ['- ' + ability['ability']['name'] for ability in poke_list['abilities']]
    title = f'The pokemons name is: "{poke_name}"'
    divider = '\n'
    body_text = divider.join(poke_list)

    return title, body_text

def new_paste(title, body_text):
    new_paste_url = post_new_paste(title, body_text, '1M', '0')
    
    return new_paste_url

if __name__ == '__main__':
    main()