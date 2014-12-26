import unittest
from controller import Controller
from server import Server, Remote, RnD, HQ
from card import Card



class TestServer(unittest.TestCase):
    def setUp(self):
        c = Controller()
        self.server = Server(c)

    def test_NoController(self):
        self.server = Server(5)

    def test_install(self):
        self.assertEqual(self.server.install(Card(Card.Type.ice)),0)
        self.assertEqual(self.server.install(Card(Card.Type.operation)),-1)


class TestRemote(unittest.TestCase):
    def setUp(self):
        c = Controller()
        self.server = Remote(c)

    def test_NoController(self):
        self.server = Remote(5)

class TestRnD(unittest.TestCase):
    def setUp(self):
        c = Controller()
        self.server = RnD(c)
        for _ in range(10):
            self.server.addCard(Card(Card.Type.asset))

    def test_CardInsertion(self):
        self.server.addCard(Card(Card.Type.asset))
        self.server.addCard(Card(Card.Type.asset))
        self.assertNotEqual(len(self.server.cardStack), 0)
        self.assertTrue(self.server.cardStack[0].id<self.server.cardStack[1].id)

    def test_Draw(self):
        c = Card(Card.Type.asset)
        self.assertTrue(issubclass(self.server.draw()[0].__class__, Card))
        self.server.addCard(c)
        self.assertEqual(self.server.draw()[0].id, c.id)
        numCards = 5
        self.assertEqual(len(self.server.draw(numCards)), numCards)

    def test_Shuffle(self):
        ids = [card.id for card in self.server.cardStack]
        self.server.shuffle()
        ids2 = [card.id for card in self.server.cardStack]
        self.assertNotEqual(ids,ids2)

class TestHQ(unittest.TestCase):
    def setUp(self):
        c = Controller()
        self.server = HQ(c)

    def test_hand(self):
        cards = []
        for _ in range(5):
            cards.append(Card(Card.Type.asset))
            self.server.add(cards[-1])
        self.assertEqual(cards[0].id, self.server.reveal(0).id)
        self.server.remove(cards[0])
        self.assertNotEqual(cards[0].id, self.server.reveal(0).id)

