import unittest
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    
    
    def test_es_mayor_edad(self):
        edad = 20
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado,True)
        
    def test_es_menor_edad(self):
        edad = 17
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado,False)


if __name__ == '__main__':
    #verbosity=2 muestra mas detalladamente el proceso
    unittest.main(verbosity=2)