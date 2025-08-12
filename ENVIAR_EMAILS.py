import os
import smtplib
from email.message import EmailMessage

EMAIL_ADRESS = 'diego.azvd8@gmail.com'
EMAIL_PASSWORD = ''
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao ponto'
msg['From'] = ''
msg['To'] = ''
msg.set_content('Favor buscar a carga que acaba de chegar na portaria')

with smtplib.SMTP_SSL('smtp.gamail.com', 465) as smpt:
    smpt.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smpt.send_message(msg)
