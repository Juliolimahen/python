from ocr import OCR
import easyocr
'''
 reader = easyocr.Reader(['pt'])

ler_imagem = reader.readtext('teste.png', paragraph=False)

for ler_imagem in ler_imagem:
    print(f'Posição:{ler_imagem[0]}\n'
    f'Texto: {ler_imagem[1]}\n')
             
'''
o = OCR(r'OCR\teste.png')
o.carregarImagem()
o.get_texto()