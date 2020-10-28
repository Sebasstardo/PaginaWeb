from django.test import TestCase 
import unittest
from .models import MisionVision,Insumo,Galeria,Producto


# Create your tests here.

class TestUno(unittest.TestCase):
   
   def grabar_mision_y_vision(self):
      m = MisionVision (
       mision="nuetra mision...", vision="nuesta vision e.."
      )

      valor=0
      try:
         m.save()
         valor = 1
      except:
         valor = 0
      self.assertEqual(valor,1)


if __name__== "__main__":
    unittest.main()

class TestDos(unittest.TestCase):
    def grabar_insumo(self):
        i = Insumo(nombre="spray",precio="9990",descripcion="es el ....",stock="0"
        )
        valor = 0
        try:
            i.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_insumo(self):
        li = Insumo.objects.all()
        self.assertIsInstance(li,Insumo)
    
if __name__ == "__main__":
    unittest.main()

class TestTres(unittest.TestCase):
    def grabar_imagen_galeria(self):
        g = Galeria(ident="6",imagen="Galeria"
        )
        valor = 0
        try:
            g.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_imagen_galeria(self):
        lg = Galeria.objects.all()
        self.assertIsInstance(lg,Galeria)
    
if __name__ == "__main__":
    unittest.main()

class TestCuatro(unittest.TestCase):
    def agregar_producto(self):
        g = Producto(tipo="Cepillo",marca="3M"
        )
        valor = 0
        try:
            g.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_producto(self):
        lp = Producto.objects.all()
        self.assertIsInstance(lp,Producto)
    
if __name__ == "__main__":
    unittest.main()