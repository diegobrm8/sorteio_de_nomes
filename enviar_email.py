import smtplib
import email.message


def criar_email(destinatario, assunto, corpo):
    # Cria uma mensagem de e-mail
    msg = email.message.EmailMessage()
    msg.set_content(corpo)
    msg['Subject'] = assunto
    msg['From'] = 'diego.azvd@gmail@gmail.com'  # Insira o seu e-mail aqui
    msg['To'] = destinatario

    # Conecta-se ao servidor SMTP do Gmail
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()

    # Faça login no servidor SMTP
    email_origem = 'diego.azvd@gmail@gmail.com'  # Insira o seu e-mail aqui
    senha = 'sua_senha'  # Insira a sua senha aqui
    servidor_smtp.login(email_origem, senha)

    # Envie o e-mail
    servidor_smtp.send_message(msg)

    # Encerre a conexão com o servidor SMTP
    servidor_smtp.quit()


# Exemplo de uso da função criar_email
destinatario = 'destinatario@example.com'
assunto = 'Teste de e-mail'
corpo = 'Este é um e-mail de teste enviado usando Python!'
criar_email(destinatario, assunto, corpo)
