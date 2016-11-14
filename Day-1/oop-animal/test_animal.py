import unittest

from animal import Animal, Bird, Mammal

class AnimalClassTest(unittest.TestCase):
    """Tests for the Animal class"""

    def test_animal_instance(self):
        an_animal = Animal()
        self.assertIsInstance(an_animal, Animal, msg="The object should be an instance of the `Animal` class")

    def test_if_the_default_value_for_feed_is_true(self):
        an_animal = Animal()
        self.assertEqual(True, an_animal.feed, msg="The default value for feed should be True")
    
    def test_if_the_default_value_for_multicellular_is_true(self):
        an_animal = Animal()
        self.assertEqual(True, an_animal.multicellular, msg="The default value for multicellular should be True")

    def test_if_input_is_a_string(self):
        an_animal = Animal()
        self.assertEqual(an_animal.movement(""), "The animal moves by: %s" % (an_animal.moves_by), msg="Only strings are allowed!")


class BirdClassTest(unittest.TestCase):
    """Tests for the Bird class"""

    def test_bird_instance(self):
        a_bird = Bird()
        self.assertIsInstance(a_bird, Animal, msg="The object should be an instance of the `Animal` class")

    def test_object_type(self):
        parrot = Bird()
        self.assertTrue((type(parrot) is Bird), msg="The object should be a type of `Bird`")

    def test_if_output_is_correct(self):
        a_bird = Bird()
        self.assertEqual(a_bird.skin_covered_with(), "The animal is covered with: %s" % (a_bird.cover))
     
        
class MammalClassTest(unittest.TestCase):
    """Tests for the Mammal class"""

    def test_mammal_instance(self):
        a_mammal = Animal()
        self.assertIsInstance(a_mammal, Animal, msg="The object should be an instance of the `Animal` class")

    def test_object_type(self):
        lion = Mammal()
        self.assertTrue((type(lion) is Mammal), msg="The object should be a type of `Mammal`")

    def test_if_input_is_a_string(self):
        a_mammal = Mammal()
        self.assertEqual(a_mammal.skin_covered_with(""), "The animal is covered with: %s" % (a_mammal.cover), msg="Only strings are allowed!")

 
if __name__ == '__main__':
    unittest.main()