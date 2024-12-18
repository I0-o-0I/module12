import module_12_1

import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name = module_12_1.Runner('a')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name = module_12_1.Runner('a')
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name = module_12_1.Runner('a')
        name2 = module_12_1.Runner('b')
        for i in range(10):
            name.walk()
            name2.run()
        self.assertNotEqual(name.distance, name2.distance)

if __name__ == '__main__':
    unittest.main()