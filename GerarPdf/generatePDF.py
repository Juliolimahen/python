from reportlab.pdfgen import canvas


def generatePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247, x, '{} : {}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245, 750, 'lista de clientes')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(name_pdf))

lista = {'Bruna': '24', 'Carlos': '56', 'Manoel': '22', 'Junior': '31' }

generatePDF(lista)
