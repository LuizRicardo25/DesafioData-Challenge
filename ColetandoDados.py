import sys
import hashlib
import TwitterSearch as TwitterSearch
from TwitterSearch import *


print('Você deseja efetuar pesquisa no conteúdo Twitter?')
print('Digite: '
      '1 - SIM'  
      '  ou  ''2 - NÃO')
menu = int(input())
if menu == 2:
    print('Interrompendo a execução')
    sys.exit()
print('Você deverá entrar com três parâmetros de pesquisa')
par1 = (input('Entre com primeiro parâmetro: '))
par2 = (input('Entre com primeiro parâmetro: '))
par3 = (input('Entre com primeiro parâmetro: '))

try:

    ts = TwitterSearch(
        consumer_key = 'IMJh4kjQLGDzUaT9t1v0RXm5Y',
        consumer_secret = 'cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE',
        access_token = '968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf',
        access_token_secret = 'hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'
     )

    tso = TwitterSearchOrder()
    #tso.set_keywords(['digital innovation one'])
    tso.set_keywords([par1])
    tso.set_keywords([par2])
    tso.set_keywords([par3])
    tso.set_language('pt')

    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e:
    print(e)