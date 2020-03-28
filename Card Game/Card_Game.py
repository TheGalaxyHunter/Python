import time


class Card:
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["none", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rankList[self.rank] + " of " + self.suitList[self.suit]

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1

        # suits are the same... check ranks

        # check ranks for ace
        if self.rank == 1 and other.rank != 1:
            return 1
        elif self.rank != 1 and other.rank == 1:
            return -1
        # check the ranks further
        elif self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        # ranks are the same... it’s a tie
        return 0


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # def printDeck(self):
    #     for card in self.cards:
    #         print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def removeCard(self, card):
        for clone in self.cards:
            if card.suit == clone.suit and card.rank == clone.rank:
                self.cards.remove(clone)
                return True
        else:
            return False

    def popCard(self):
        return self.cards.pop()

    def isEmpty(self):
        return len(self.cards) == 0

    def notEmpty(self):
        return len(self.cards) != 0

    def deal(self, hands, nCards=52):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty():
                break                   # break if out of cards
            card = self.popCard()       # take the top card
            hand = hands[i % nHands]    # whose turn is next?
            hand.addCard(card)          # add the card to the hand


class Hand(Deck):

    def __init__(self, name=""):
        super().__init__()
        self.cards = []
        self.name = name

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name

        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains\n" + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        self.deck.shuffle()


class OldMaidHand(Hand):

    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card(3 - card.suit, card.rank)
            for clone in originalCards:
                if match.suit == clone.suit and match.rank == clone.rank:
                    self.cards.remove(card)
                    self.cards.remove(clone)
                    originalCards.remove(card)
                    originalCards.remove(clone)
                    print("\nHand %s: %s matches %s\n" % (self.name, card, match))
                    count = count + 1

        return count


class OldMaidGame(CardGame):

    def __init__(self):
        super().__init__()
        self.hands = []

    def play(self, names):
        time.sleep(1)
        # remove Queen of Clubs
        self.deck.removeCard(Card(0, 12))

        # make a hand for each player
        for name in names:
            self.hands.append(OldMaidHand(name))

        # deal the cards
        self.deck.deal(self.hands)
        print("\n---------- Cards have been dealt")
        self.printHands()
        time.sleep(1)

        # remove initial matches
        matches = self.removeAllMatches()
        print("---------- Matches discarded, play begins\n")
        self.printHands()
        time.sleep(1)

        # play until all 50 cards are matched
        turn = 0
        numHands = len(self.hands)
        while matches < 25:
            matches = matches + self.playOneTurn(turn)
            turn = (turn + 1) % numHands
            time.sleep(0.5)

        print("---------- Game is Over\n\n")
        self.printHands()
        time.sleep(1)

        # print the loser's name
        for hand in self.hands:
            if hand.notEmpty():
                print("So " + hand.name + " loses\n\n")

    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.removeMatches()
        return count

    def printHands(self):
        for hand in self.hands:
            time.sleep(1)
            print(hand)

    def playOneTurn(self, i):
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)
        pickedCard = self.hands[neighbor].popCard()
        self.hands[i].addCard(pickedCard)
        print("Hand", self.hands[i].name, "picked", pickedCard, "from", self.hands[neighbor].name)
        count = self.hands[i].removeMatches()
        self.hands[i].shuffle()
        return count

    def findNeighbor(self, i):
        numHands = len(self.hands)
        for nxt in range(1, numHands):
            neighbor = (i + nxt) % numHands
            if not self.hands[neighbor].isEmpty():
                return neighbor


game = OldMaidGame()
names_of_players = input("Enter the names of the players (comma in between them): ").split(", ")
print("\nLet's begin the game of cards......!!!!!\n")
game.play(names_of_players)
