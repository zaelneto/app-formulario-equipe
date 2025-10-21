from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
# import webbrowser
# import threading

app = Flask(__name__)

# Configure o e-mail de destino e SMTP aqui
DESTINATION_EMAIL = "cadastro.colaborador.deem@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "cadastro.colaborador.deem@gmail.com"
SMTP_PASSWORD = "guqd lqrj vdkg phke"  # use senha de app, não a senha normal

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    data_nasc = request.form['data_nasc']
    cpf = request.form['cpf']
    rg = request.form['rg']
    cargo = request.form['cargo']
    matricula = request.form['matricula']
    banco = request.form['banco']
    agencia = request.form['agencia']
    conta = request.form['conta']

    # Monta o conteúdo do e-mail
    corpo = f"""
    Dados Pessoais e Bancários

    Nome Completo: {nome}
    Data de Nascimento: {data_nasc}
    CPF: {cpf}
    RG: {rg}
    Cargo: {cargo}
    Matrícula: {matricula}

    💰 Dados Bancários
    Banco: {banco}
    Agência: {agencia}
    Conta Bancária: {conta}
    """

    msg = MIMEText(corpo, "plain", "utf-8")
    msg['Subject'] = "📋 Novo Formulário Recebido"
    msg['From'] = SMTP_USER
    msg['To'] = DESTINATION_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        return "<h3>✅ Formulário enviado com sucesso!</h3>"
    except Exception as e:
        print(e)
        return "<h3>❌ Erro ao enviar formulário. Verifique o servidor.</h3>"

# def abrir_navegador():
#     webbrowser.open_new("http://localhost:5000")

# threading.Timer(1, abrir_navegador).start()
# app.run(debug=False)

# if __name__ == '__main__':
#     app.run(debug=True)