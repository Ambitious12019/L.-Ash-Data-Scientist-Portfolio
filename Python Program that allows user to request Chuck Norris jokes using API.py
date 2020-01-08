


#!/usr/bin/env python
"""downloads a random Chuck Norris joke or fact using the api"""

import json
import requests


def main():
    display_banner()
    print()
    
    data = get_joke()
    text = parse_json(data)
    print(display_joke(text))
   # button_tapped(sender)



def display_banner():
    print('-' * 40)
    print('   Welcome to Chuck Norris Jokes   ')
    print('-' * 40)


    
def get_joke():
    user = input('Enter Y if you want to request Chuck Norris jokes or 0 to quit:')
    print(user)
           
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        print(response.status_code)
        # rest = response.content
   
    elif response.status_code != 200:
        print('Error, unable to connect to api')
    
    else:
        print(response.status_code)
    rest = response.content
    return rest

       
def parse_json(data):
    text = json.loads(data)
    text = (text['value'])
    # print(text)
    return text


def display_joke(text):
    formatted = str(text).strip()
    # print(type(formatted))
    return formatted


# def button_tapped(sender):
# chuck = button_tapped(sender)
#    sender.title = chuck
#    view = ui.load_view('chuck')
#    view.present('full_screen')
#    return # #view.present('full_screen')

if __name__ == '__main__':
    main()