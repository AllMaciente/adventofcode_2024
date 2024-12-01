import requests
from dotenv import load_dotenv
import os

load_dotenv()

class Erro(Exception):
    pass

def get_input(url):
    
    session_cookie = os.getenv('SESSION_COOKIE')
    
    
    cookies = {'session': session_cookie}
    
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        return response.text  
    else:
        raise Erro(f"Falha ao obter dados: {response.status_code}")

if __name__ == "__main__":
    get_input('https://adventofcode.com/2024/day/1/input')
