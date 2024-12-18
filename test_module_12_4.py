import logging

import module_12_4
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            name = module_12_4.Runner('a', -10)
            for i in range(10):
                name.walk()
            self.assertEqual(name.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            name = module_12_4.Runner(2, 10)
            for i in range(10):
                name.run()
            self.assertEqual(name.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            
    def test_challenge(self):
        name = module_12_4.Runner('a')
        name2 = module_12_4.Runner('b')
        for i in range(10):
            name.walk()
            name2.run()
        self.assertNotEqual(name.distance, name2.distance)

if __name__ == '__main__':
    unittest.main()
