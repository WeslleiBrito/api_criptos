from binance.client import Client
from secret import api_key, api_secret

client = Client(api_key, api_secret)

info = client.get_account()
#
# for dados in info['balances']:
#     if float(dados['free']) > 0:
#         print(dados)

cotacao = client.get_recent_trades(symbol='ADABRL')
orders = client.get_all_orders(symbol='ADABRL', limit=10)
compras_vendas = client.get_my_trades(symbol='ADABRL')
preco_atual = float(cotacao[-1]['price'])
preco_compra = float(compras_vendas[-1]['price'])
quantidade = float(compras_vendas[-1]['qty'])
lp = preco_atual - preco_compra

for execucao in compras_vendas:
    print(execucao)

total_compra = preco_compra * quantidade
total_atual = preco_atual * quantidade
lucro_prejuizo = total_atual - total_compra
print(f'Preço unitário atual: {preco_atual}\nPreço unitário compra: {preco_compra}\nQuantidade: {quantidade}')
print(f'Compra: {total_compra}\nValor atual: {total_atual}\nResultado: {lucro_prejuizo:.2f}')
print(f'Porcentagem: {(lucro_prejuizo / total_compra) * 100:.2f}%')

taxas = client.get_trade_fee()


for tx in taxas:
    if tx['symbol'] == 'ADABRL':
        print(tx)