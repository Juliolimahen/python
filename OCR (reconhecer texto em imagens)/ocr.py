import easyocr

class OCR:
    
    ler_imagem=''
    imagem=''
    
    def __init__(self, imagem):
        self.imagem = imagem
    
    def carregarImagem(cls):
        reader = easyocr.Reader(['pt'])
        cls.ler_imagem = reader.readtext(cls.imagem, paragraph=False)
        return cls.ler_imagem
    
    def get_texto(cls):
        print(f'Resultado leitura: ')
        for cls.ler_imagem in cls.ler_imagem:
            #pegar posição f'Posição:{cls.ler_imagem[0]}\n'
             print(f'{cls.ler_imagem[1]}', end=' ')
             