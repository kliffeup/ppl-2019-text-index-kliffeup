import unittest
from sort_functions import sorting_by_order, sorting_by_frequency


class SortByOrderTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            sorting_by_order({'курица': [1, [1]], 'мышь': [1, [1]], 'дрожь': [1, [1]], 'радуга': [2, [1]]}),
            ['дрожь', 'курица', 'мышь', 'радуга'])

    def test_2(self):
        self.assertEqual(sorting_by_order({'cat': [2, [1]], 'dog': [3, [1]], 'mouse': [1, [1]], 'horse': [1, [1]]}),
                         ['cat', 'dog', 'horse', 'mouse'])

    def test_3(self):
        self.assertEqual(sorting_by_order(
            {'крапива': [2, [1]], 'мак': [1, [1]], 'куст': [1, [1]], 'выдра': [1, [1]], 'лось': [1, [1]],
             'река': [1, [1]]}), ['выдра', 'крапива', 'куст', 'лось', 'мак', 'река'])

    def test_4(self):
        self.assertEqual(sorting_by_order(
            {'coat': [1, [1]], 'river': [1, [1]], 'letter': [1, [1]], 'zoo': [1, [1]], 'dear': [1, [1]]}),
            ['coat', 'dear', 'letter', 'river', 'zoo'])

    def test_5(self):
        self.assertEqual(sorting_by_order(
            {'room': [2, [1]], 'python': [1, [1]], 'qadrat': [1, [1]], 'cygwin': [1, [1]], 'restore': [1, [1]]}),
            ['cygwin', 'python', 'qadrat', 'restore', 'room'])


class SortByFrequenceTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sorting_by_frequency(
            {'happy': [3, [1]], 'wet': [2, [1]], 'dry': [1, [1]], 'well': [2, [1]], 'good': [1, [1]]}),
            [('happy', [3, [1]]), ('well', [2, [1]]), ('wet', [2, [1]]), ('good', [1, [1]]),
             ('dry', [1, [1]])])

    def test_2(self):
        self.assertEqual(sorting_by_frequency(
            {'port': [2, [1]], 'checked': [1, [1]], 'aunt': [1, [1]], 'smile': [1, [1]], 'aqua': [1, [1]],
             'feature': [1, [1]]}), [('port', [2, [1]]), ('feature', [1, [1]]), ('aqua', [1, [1]]), ('smile', [1, [1]]),
                                     ('aunt', [1, [1]]), ('checked', [1, [1]])])

    def test_3(self):
        self.assertEqual(sorting_by_frequency(
            {'TNT': [1, [1]], 'Vassel': [2, [1]], 'Spirit': [1, [1]], 'Frost': [2, [1]], 'Ray': [3, [1]],
             'Thunder': [4, [1]], 'request': [1, [1]]}),
            [('Thunder', [4, [1]]), ('Ray', [3, [1]]), ('Frost', [2, [1]]), ('Vassel', [2, [1]]),
             ('request', [1, [1]]), ('Spirit', [1, [1]]), ('TNT', [1, [1]])]
        )

    def test_4(self):
        self.assertEqual(
            sorting_by_frequency({'terminate': [2, [1]], 'doctor': [2, [1]], 'reduce': [2, [1]], 'porridge': [1, [1]]}),
            [('reduce', [2, [1]]), ('doctor', [2, [1]]), ('terminate', [2, [1]]), ('porridge', [1, [1]])])

    def test_5(self):
        self.assertEqual(sorting_by_frequency(
            {'walk': [1, [1]], 'trY': [2, [1]], 'LauncH': [1, [1]], 'faDe': [1, [1]], 'waLk': [2, [1]],
             'xeNon': [1, [1]]}), [('waLk', [2, [1]]), ('trY', [2, [1]]), ('xeNon', [1, [1]]), ('faDe', [1, [1]]),
                                   ('LauncH', [1, [1]]), ('walk', [1, [1]])])


if __name__ == '__main__':
    unittest.main()
