import pdfplumber as pdftool
find = input("oque deseja procurar? ")
def busca (filepath):
    with pdftool.open(filepath) as tool:
        for p_no, pagina in enumerate(tool.pages,1):
            data = pagina.extract_text()
            data = data + str(p_no)
            if find in data:
                print (data)
                print(p_no)
                exit
            else:
                data = ""
busca(find)
# antes de "numpage p_no" tenta encontrar protocolo se n apagar texto e ir pra 
# proxima interação