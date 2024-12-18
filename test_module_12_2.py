import module_12_2
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name = module_12_2.Runner('Усэйн', 10)
        self.name2 = module_12_2.Runner('Андрей', 9)
        self.name3 = module_12_2.Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(k)
            for q, i in v.items():
                print(f' {q}: {str(i)}')

    def test_run1(self):
        a = module_12_2.Tournament(90, self.name, self.name3)
        res = a.start()
        self.all_results['test1'] = res
        self.assertTrue(res[max(res.keys())], self.name3)

    def test_run2(self):
        a = module_12_2.Tournament(90, self.name2, self.name3)
        res = a.start()
        self.all_results['test2'] = res
        self.assertTrue(res[max(res.keys())], self.name3)

    def test_run3(self):
        a = module_12_2.Tournament(90, self.name, self.name2, self.name3)
        res = a.start()
        self.all_results['test3'] = res
        self.assertTrue(res[max(res.keys())], self.name3)

if __name__ == '__main__':
    unittest.main()