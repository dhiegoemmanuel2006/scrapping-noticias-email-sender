import yagmail

# Iniciar SMTP server
def email_server(email, password):
    return yagmail.SMTP(email, password)

# Enviando email
def send_email_template(email_smtp, title, content, email_to):
    try:
        email_smtp.send(
            to=email_to,
            subject=title,
            contents=content
        )
        print("Email enviado com sucesso")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")