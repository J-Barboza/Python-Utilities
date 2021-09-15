import time
from plyer import notification

def notificacaoWin10(_Title, _Message): 
    notification.notify(
        title = _Title,
        message = _Message,
        
        # displaying time
        timeout=3
    )
# waiting time
time.sleep(4)