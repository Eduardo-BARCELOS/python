import gc
import requests
import pdfplumber as pdftool
import smtplib
import email.message
print ("este código pega uma URL que você deseje fazer o dowload de um PDF, então o link tem que ser direto de um PDF, você colocara o nome do PDF e em seguida o nome ou numero que deseja procurar nesse PDF")
nam = (input("qual nome deseja pro arquivo? ")) + ".pdf"
print(nam)
url = input("digite a URL direta do dowload: ")
op = input("você quer enviar um email pra você com o resultado ? SIM[1] NÃO[2] ")
if op == 1:
    asun = input("assunto do email : ")
    de = input("email dê? ")
    para = input("para ? ")
    print ("criado em apps menos seguros > apps de terceiros > adicionar > pegar senha temporaria e colocar aqui embaixo")
    sen = input("senha ? ")
if op == 2:
    print("ok aguarde")
response = requests.get(url)
cont = 0
lis_pages = ["",""]
lis = [""]
# criar o arquivo PDF
if response.status_code == 200:
    print ("status 200 > ok 👍")
    with open (nam, "wb") as f:
        f.write(response.content)
else:
    print("tente outra url que esteja funcionando")
# achar oque o usuario está procurando
find = input("oque deseja procurar? ")
with pdftool.open(nam) as tool:
        for p_no, pagina in enumerate(tool.pages,1):
            data = pagina.extract_text()
            if find in data:
                lis_pages[cont] = str(p_no)
                print (data)
                lis[cont] = data
                print(p_no)
                cont = cont + 1
            data = ""

####### enviar o email ###################


def enviar_email():  
    corpo_email = f"""
   <p>Pagina > {lis_pages}</p>
    <p>pag.. {lis}</p>
   <p>Foram encontrados {cont} paginas com a palavra {find} </p>
   """

    msg = email.message.Message()
    msg['Subject'] = asun
    msg['From'] = de
    msg['To'] = para
    password = sen
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')




enviar_email()
