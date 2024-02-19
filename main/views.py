from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests
import json

psid = "fggo0z3MRTjJwGXgMjQKv3Fc6vfugDEePThJXyWNdjuLGdzwDpfWZA0VBIgb42FSpBRYTg."
psidts = "sidts-CjEBPVxjSuD9MhpNOkaZsBP0TfYknJfHMijPe2JeiwsRIQEsrSSWBun_bZwQOl6jDctdEAA"
psidcc = "ABTWhQF825AG80PZHHfMEDcjfMOAMxlZA-HNbzUaOK3mP_SobCA5kKteXrR-FaOvwiWpd7Q9Zec"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado

mockedResponse = '{"content": "blá blá blá"}'
enableMock = True


#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        bard = None
        answer =json.loads(mockedResponse)
        
        if enableMock== False:
         bard = BardCookies(cookie_dict=tokenCookies)
        

        #pega os dados que veio na requisição
        data = request.data

        conversationID = data.get("conversationID")

        if(conversationID is not None):
            bard.conversation_id = conversationID
        elif enableMock == False:
            bard.conversation_id= None 

        

        #answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

