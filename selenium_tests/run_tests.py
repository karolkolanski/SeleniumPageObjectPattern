import unittest
from tests.registration_test import RegistrationTest

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

# Lista testów do uruchomienia
tests_for_run = [
    registration_test,
    # kolejny test
    # ...
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)
