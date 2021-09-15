import smtplib
import email.message

def enviar_email(**params):
    msg = email.message.Message()
    msg['From'] = params.get('_from')
    msg['To'] = params.get('_to')
    msg['Subject'] = params.get('_subject')
    _token = params.get('_token')
    _bodyEmail = params.get('_bodyEmail')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(_bodyEmail)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], _token)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
