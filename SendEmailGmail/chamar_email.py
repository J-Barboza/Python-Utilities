from Enviar_Email import enviar_email
from datetime import datetime

_dateTime = datetime.now().strftime("%d/%m/%Y %H:%M")

_bodyEmail = f"""
    <p><h3>Teste de Evio de Email usando o Python <h3></p>
    <p><h3>Verificado em: {_dateTime}</h3></p>
    """

parametros = {'_from':'Remetente@email.com'
             ,'_to':'Destinatario@email.com'
             ,'_assunto':'Assunto'
             ,'_password':'Token'
             ,'_corpoEmail':'Corpo Email'
             }

enviar_email(**parametros)