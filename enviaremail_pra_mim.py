import smtplib
from email.message import EmailMessage

# Configurações
remetente = "diego.azvd8@gmail.com"
senha = ""
destinatario = "diego.brum8888@gmail.com"
assunto = "Teste de E-mail"
mensagem = "Olá blz?"

# Criar a mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = assunto
msg['From'] = remetente
msg['To'] = destinatario
msg.set_content(mensagem)

# Iniciar conexão com o servidor SMTP do Gmail
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    # Fazer login na conta do remetente
    server.login(remetente, senha)
    # Enviar e-mail
    server.send_message(msg)

print("E-mail enviado com sucesso para", destinatario)
