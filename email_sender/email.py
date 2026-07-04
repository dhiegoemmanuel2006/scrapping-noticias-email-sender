import yagmail
import logging

# Iniciar SMTP server
def email_server(email, password):
    return yagmail.SMTP(email, password)

# Enviando email
def send_email_template(email_smtp, title, content, email_to):
    try:
        # Remove newlines to prevent yagmail from inserting unwanted <br> tags in the CSS style blocks
        clean_content = content.replace("\n", "").replace("\r", "")
        email_smtp.send(
            to=email_to,
            subject=title,
            contents=[clean_content]
        )
        logging.info("Email enviado com sucesso")
    except Exception as e:
        logging.error(f"Erro ao enviar email: {e}")