import logging
import module_12_1 as r
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="Timmi_tests.log",
                    encoding="utf-8", format="%(asctime)s -|- %(levelname)s -|- %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r_1 = r.Runner('Вася', -5)
            for _ in range(10):
                r_1.walk()
            self.assertEqual(r_1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            r_2 = r.Runner(2)
            for _ in range(10):
                r_2.run()
            self.assertEqual(r_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    if __name__ == "__main__":
        unittest.main()
