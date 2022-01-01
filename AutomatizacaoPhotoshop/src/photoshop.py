import win32com.client
import os
from pathvalidate import sanitize_filename

class Photoshop:
    #atributo photoshop
    app = None
    #atributo arquivo aberto
    psd_file = None
    
    #construtor
    def __init__(self):
        self.app = win32com.client.Dispatch("AdobePhotoshop2021.Application")
        #self.app.Visible = False
        
    #metodo fecha photoshop
    def closePhotoshop(self):
        self.app.Quit()
    
    def openPSD(self, filename):
        if os.path.isfile(filename) == False:
            self.psd_file = self.app.Application.ActiveDocument
            return True
        
    def closePSD(self):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        
        self.app.Application.ActiveDocument.Close(2)
    
    def updateLayerText(self, layer_name, text):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        
        layer = self.psd_file.ArtLayers[layer_name]
        layer_text = layer_TextItem
        layer_text.contents = text
        
        return True
    
    def exportJPEG(self, filename, folder='',quality=10):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        
        filename = sanitize_filename(filename)
        full_path = os.path.join(folder, filename)
        
        options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
        options.Format = 6
        options.Quality = quality
        
        self.psd_file.Export(ExportIn=full_path, ExportAs=2, Options=options)
        
        return os.path.isfile(full_path)
    