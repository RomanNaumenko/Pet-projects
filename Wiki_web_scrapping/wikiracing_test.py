import unittest

from wiki_racing_titlecheck_ver import *


class WikiRacerTest(unittest.TestCase):
    racer = WikiRacer()

    def test_0(self):
        path = self.racer.pathfinder('Дружба', 'Рим')
        self.assertEqual(path, ['Дружба', 'Якопо Понтормо', 'Рим'])

    def test_1(self):
        path = self.racer.pathfinder('Дружба', 'Рим')
        self.assertEqual(path, ['Дружба', 'Якопо Понтормо', 'Рим'])

    def test_2(self):
        path = self.racer.pathfinder('Мітохондріальна ДНК', 'Вітамін K')
        self.fail("implement me")

    def test_3(self):
        path = self.racer.pathfinder('Марка (грошова одиниця)', 'Китайський календар')
        self.fail("implement me")

    def test_4(self):
        path = self.racer.pathfinder('Фестиваль', 'Пілястра')
        self.fail("implement me")

    def test_5(self):
        path = self.racer.pathfinder('Дружина (військо)', '6 жовтня')
        self.fail("implement me")


if __name__ == '__main__':
    unittest.main()
