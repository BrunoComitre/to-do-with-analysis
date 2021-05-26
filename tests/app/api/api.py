################## ARQUIVO DE EXEMPLO PARA CRIAÇÃO DOS TESTES ##################

##################### Códigos de status das respostas HTTP #####################
# As respostas são agrupadas em cinco classes:
## - (100-199) : Respostas de informação
## - (200-299) : Respostas de sucesso
## - (300-399) : Redirecionamentos
## - (400-499) : Erros do cliente
## - (500-599) : Erros do servidor
################################################################################

##################### Códigos de status das respostas HTTP #####################

# 200 OK = Requisição bem sucedida. O significado do sucesso varia de acordo com
# o método HTTP

# 201 Created = Requisição foi bem sucedida e um novo recurso foi criado como 
# resultado. Esta é uma tipica resposta enviada após uma requisição POST

# 404 Not Found = O servidor não pode encontrar o recurso solicitado

# 422 Unprocessable Entity (WebDAV) = A requisição está bem formada mas
# inabilitada para ser seguida devido a erros semânticos
################################################################################


import json
import pytest
# from app.api.api_v1.endpoints import api


##################################### POST #####################################

##################################### GET ######################################

################################### GET ALL ####################################

##################################### PUT ######################################

#################################### DELETE ####################################
