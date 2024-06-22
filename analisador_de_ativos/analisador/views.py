from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import requests

class PaginaInicial(View):
    template_name = 'pagina_inicial.html'

    def get(self, request, **kwargs):
        base_url = 'https://brapi.dev/api/quote/'
        token = 'jt7Nv3nvDyAAhgsM1zFuzp'
        url = f'{base_url}list?token={token}'
        
        ativos = []

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            ativos = [item.get("stock") for item in data.get("stocks", [])]
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")

        context = {
            'ativos': ativos
        }

        return render(request, self.template_name, context)