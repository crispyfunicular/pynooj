import unittest
import pynooj.main as main


class TestMain(unittest.TestCase):
    def test_unescape1(self):
        txt = "Hello World!"
        result = main.unescape(txt)
        self.assertEqual("Hello World!", result)

    def test_unescape2(self):
        txt = "Hello\\, World!"
        result = main.unescape(txt)
        self.assertEqual("Hello, World!", result)

    dic_amo = [
        {
            "inflected form": "amo",
            "lemma": "amare",
            "category": "V",
            "traits": {
                "Theme": "INF",
                "FLX": "GP1_INF",
                "GP": "1",
            },
        }
    ]

    def test_read_dic1(self):
        path = "tests/dic1.dic"
        result = main.read_dic(path)

        self.assertEqual(self.dic_amo, result)

    def test_read_dic2(self):
        path = "tests/dic2.dic"
        result = main.read_dic(path)

        self.assertEqual(self.dic_amo, result)

    def test_read_dic3(self):
        path = "tests/dic3.dic"
        result = main.read_dic(path)

        self.assertEqual(self.dic_amo, result)

    def test_read_dic4(self):
        path = "tests/dic4.dic"
        result = main.read_dic(path)

        dic_amo2 = [
            {
                "inflected form": "amo",
                "category": "V",
                "traits": {
                    "Theme": "INF",
                    "FLX": "GP1_INF",
                    "GP": "1",
                },
            }
        ]

        self.assertEqual(dic_amo2, result)


if __name__ == "__main__":
    unittest.main()
