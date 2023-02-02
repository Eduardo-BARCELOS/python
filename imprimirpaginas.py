
import pdfplumber as pdftool
def busca (filepath):
    with pdftool.open(filepath) as tool:
        for p_no, pagina in enumerate(tool.pages,1):
            data = pagina.extract_text()
            data = data + str(p_no)
            if p_no>=100 and p_no <=200:
                print (data)
                print(p_no)
            else:
                data = ""
busca("Marcas2716.pdf")
# antes de "numpage p_no" tenta encontrar protocolo se n apagar texto e ir pra 
# proxima interação