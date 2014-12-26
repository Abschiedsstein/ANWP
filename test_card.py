import unittest
from card import Card



class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(Card.Type.asset)

    def test_DifferentIds(self):
        card = Card(Card.Type.asset)
        self.assertTrue(card.id != self.card.id)
