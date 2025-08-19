import requests

url = 'https://www.pudim.com.br/'

def acessar(msg):
    try:
        response = requests.get(msg)

        response.raise_for_status()

        print('Acesso bem sucedido!')
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao tentar acessar o site: {e}')   

acessar(url)         