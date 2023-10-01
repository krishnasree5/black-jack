
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card():

    def __init__(self,suit,rank):       #create a card object
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):    #to create  a deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))   #add cards to deck


    def __str__(self):   #print the deck
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__() 
        return "The deck has: " + deck_comp
        
    def shuffle_deck(self):       #shuffle the deck
        shuffle(self.deck)


    def deal(self):         #remove a card from the deck
        return self.deck.pop()


class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0     #to deal with aces (they have the value 1 or 11 ,depends on the player

    def add_card(self,card):          #this card is from deal() method in class Deck
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':       #count the number of aces
            self.aces += 1
            

    def handle_ace(self):
        while self.value > 21 and self.aces:
            #only if total of player's card is >21 then change the value of ace to 1
            #initially the value of ace is 11.adjusting to 1 by subtractiong 10 from total of player's card
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))

        except:
            print("Please provide an integer")

        else:
            if chips.bet > chips.total:
                print("Sorry, your bet cant exceed",chips.total)
            else:
                break


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.handle_ace()


def ask_hit_or_stand(deck,hand):

    global playing
    
    while True:
        x = input("\nHit or Stand?(h/s)")

        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
            
        else:
            print("Enter h or s only")
            continue
        break



def show_cards(player,dealer):
    
    print("\nDealer's Hand: ")
    print("First card hdden!")
    print(dealer.cards[1])

    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)



def show_all(player,dealer):

    print("\nDealer's hand: ",*dealer.cards,sep="\n")

    print(f"Value of Dealer's hand is: {dealer.value}")
        
    print("\nPlayer's hand: ",*player.cards,sep="\n")

    print(f"Value of Player's hand is: {player.value}")


def player_busts(player,dealer,chips):
    print("Player Busted!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Busted!")
    chips.win_bet()

    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()
    

def push(player,dealer):
    print("It's a Tie")

    

while True:
    
    print("Welcome to BlackJack")

    #create and shuffle the deck     
    deck = Deck()        
    deck.shuffle_deck()

    #create player hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    
    #create dealer hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_cards(player_hand,dealer_hand)

    while playing:

        #ask user to hit or stand
        ask_hit_or_stand(deck,player_hand)    

        #show cards except 1st card of dealer
        show_cards(player_hand,dealer_hand)


        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)


    print(f"\n Player's chips: {player_chips.total}")

    new_game = input("Play again: y/n")

    if new_game[0].lower() == 'y':
        playing = True
    else:
        print("Thank you for playing!")
        break
    






        
