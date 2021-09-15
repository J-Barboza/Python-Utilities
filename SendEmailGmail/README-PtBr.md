# Python Utilities

### Send Email using Gmail with 2-Step Verification
- Acesse sua conta Gmail e faça Login
- Habilite verificação em duas etapas
  > Pode usar esse [link](https://myaccount.google.com/signinoptions/two-step-verification) para habilitar. 
- Gerar a senha (Token) de acesso para o aplicativo
  > Usar esse [link](https://security.google.com/settings/security/apppasswords) e criar a senha.
 

### Requerimentos
- Instalar o pacote Win32
  > pip install pywin32.

### Parametros 
- _emailFrom = e-mail de quem está enviando.
- _password = Token criado para acessar a conta Gmail.
- _emailTO = e-mail de quem irá receber.
- _assunto = Assunto do E-mail.
- _corpo = Corpo de E-mail.

### Observações
- Lembre-se que para chamar a função, deve ser passado um dicionário.
- Como é passado um Kwargs, os parametros podem ser facilmente alterados e/ou incluídos, basta ajustar os parâmetros.




