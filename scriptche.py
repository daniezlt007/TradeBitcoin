# -*- coding: utf-8 -*-

import json
import requests
import os.path
from datetime import datetime

URL    = 'https://api.coinmarketcap.com/v1/ticker/'
MOEDAS = ['bitcoin', 'ethereum', 'litecoin', 'monero']

def write_to_file(resultado, filename='scriptche.csv'):
    if not os.path.isfile(filename):
        cabecalho = 'horario'
        for moeda in MOEDAS:
            cabecalho += ';%s' % moeda
        resultado = cabecalho + resultado

    with open(filename, 'a') as wfile:
        wfile.write(resultado)


if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        response_list = json.loads(response.text)
        resultado = ''
        
        # Adiciona a coluna com o horário da solicitação.
        resultado += '\n%s' % datetime.now()

        # Adiciona as colunas com as moedas.
        for moeda in response_list:
            if moeda['id'] in MOEDAS:
                resultado += ';%s' % moeda['price_usd']

        write_to_file(resultado)
    else:
        print 'Erro ao consultar: %s' % response.status_code