import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analisador_de_ativos.settings.py')
django.setup()

from analisador.models import Ativo
import requests


def popula_ativo():
    listaAtivos = pega_dados_ativos_no_brapi()

    for dadoAtivo in listaAtivos:
        novoAtivo = Ativo(ativo=dadoAtivo.get('ativo'),
                          nome=dadoAtivo.get('nome'),
                          volume=dadoAtivo.get('volume'),
                          setor=dadoAtivo.get('setor'))
        novoAtivo.save()


def pega_dados_ativos_no_brapi():
    base_url = 'https://brapi.dev/api/quote/'
    token = 'jt7Nv3nvDyAAhgsM1zFuzp'
    url = f'{base_url}list?token={token}'
    
    listaAtivos = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for dadoAtivo in data.get('stocks'):
            ativo = {
                "ativo":dadoAtivo.get('stock'),
                "nome":dadoAtivo.get('name'),
                "volume":dadoAtivo.get('volume'),
                "setor":dadoAtivo.get('sector')
            }
            listaAtivos.append(ativo)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")

    return listaAtivos