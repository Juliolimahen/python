import sys, os 
sys.path.insert(0, './src')
import unittest
import photoshop 

class TestPhotoshop(unittest.TestCase):
    
    def setUp(self):
        self.psd_origin = os.path.abspath("./tests/resources/1.psd")
        self.jpeg_path = os.path.abspath("./tests/resources/tmp")
        self.jpeg_name = "1.jpg"
        self.jpeg_full_path = os.path.join(self.jpeg_path, self.jpeg_name)
        
        if not os.path.exists(self.jpeg_path):
            os.mkdir(self.jpeg_path)
        
    def tearDown(self):
        self.app.closePhotoshop()
        
        if not os.path.exists(self.jpeg_full_path):
            os.remove(self.jpeg_full_path)
            
        if not os.path.exists(self.jpeg_path):
            os.rmdir(self.jpeg_path)
    
    def test_openPSD(self):
        opened = self.app.openPSD(self.psd_origin)
        if opened:
            self.app.closePSD()
        self.assertTrue(opened)
        
    def testUpdateLayerText(self):
        updated1 = False
        updated2 = False
        
        opened = self.app.openPSD(self.psd_origin)
        
        updated1 = self.app.updateLayerText("PERIODO", "TESTE")
        updated2 = self.app.updateLayerText("NUMERO_EPISODIO", "TESTE")
        self.app.closePSD()
        
        self.assertTrue(updated1)
        self.assertTrue(updated2)
    def test_exportJPEG(self):
        exported = False
        
        opened = self.app.openPSD(self.psd_origin)
        
        if opened:
            updated1 = self.app.updateLayerText("PERIODO", "TESTE")
            updated2 = self.app.updateLayerText("NUMERO_EPISODIO", "TESTE")
            
            if updated1 & updated2:
                exported =self.app.exportJPEG
                
            self.app.closePSD()
        
        self.assertTrue(exported)
        
if __name__ == '__main__':
    unittest.main()