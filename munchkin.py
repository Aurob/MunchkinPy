import numpy as np, cv2, math, base64
from random import randint as rn
import mnch_deck
class deck:
    def __init__(self):
        self.info = eval(open('./munchkin_cards/card_info.txt','r').read())
        self.doors = {}
        self.treasures = {}
        self.door_d = []
        self.treasures_d = []

        self.get_deck()
        print("Decks Created...")
        
    def show(self, title, im):
        cv2.imshow(title, im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_deck(self):
        cards = mnch_deck.get_deck()
        doors={}
        treasures={}
        for i in range(0,95):
            self.doors[i] = {'img':cards[i],'type': self.info[i]}

        for i in range(0,73):
            im = cv2.imread('./munchkin_cards/'+str(i+94)+'.png')
            self.treasures[i] = {'img':cards[i+96],'type': self.info[i+94]}

    def draw(self, cards, card_type):
        drawn_cards = []
        if card_type == "door":
            for c in range(cards):
                doors = list(self.doors.keys())
                draw = doors[rn(0, len(doors)-1)]
                drawn_cards.append(self.doors[draw])
                del self.doors[draw]
                #cards = list(map(lambda card: self.encode(self.doors[rn(0,len(self.doors)-1)]), [i for i in range(cards)]))
        elif card_type == "treasure":
            for c in range(cards):
                treasures = list(self.treasures.keys())
                draw = treasures[rn(0, len(treasures)-1)]
                drawn_cards.append(self.treasures[draw])
                del self.treasures[draw]
                #cards = list(map(lambda card: self.encode(self.treasures[rn(0,len(self.treasures)-1)]), [i for i in range(cards)]))
        return drawn_cards

class character:
    def __init__(self):
        self.race_type = "human"
        self.class_type = None
        self.level = 1
        self.sex = ['f','m'][rn(0,1)]
        self.hand = []
        self.in_play = []
        
class game:
    def __init__(self, player_count, decks):
        self.deck = decks
        self.players = list(character() for i in range(player_count))
        self.hand_init()
        
    def hand_init(self):
        for player in self.players:
            player.hand = self.deck.draw(4, 'door') + self.deck.draw(4, 'treasure')

    def play_card(self, player, card):
        if card['type'] == 'race':
            player.race_type = card['type']
        if card['type'] == 'class':
            player.class_type = card['type']
        player.in_play += card
        player.hand.remove(card)
        
    def roll(self):
        return rn(1,6)

d = deck()
g = game(1, d)
