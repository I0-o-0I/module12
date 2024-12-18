import unittest
import test_module_12_3
import test_module12_1

st = unittest.TestSuite()
st.addTest(unittest.TestLoader().loadTestsFromTestCase(test_module12_1.RunnerTest))
st.addTest(unittest.TestLoader().loadTestsFromTestCase(test_module_12_3.TournamentTest))

a = unittest.TextTestRunner(verbosity=2)
a.run(st)