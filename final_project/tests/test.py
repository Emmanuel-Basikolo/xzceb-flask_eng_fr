import unittest
import translator

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(translator.englishToFrench(None)) 
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour") 

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(translator.frenchToEnglish(None)) 
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello") 
        
unittest.main()
