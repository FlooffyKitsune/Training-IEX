import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            if chips.bet > chips.total:
                print(f"Bet exceeds total chips. You have {chips.total} chips.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            hit(deck, hand)
        elif choice == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Invalid input. Please enter 'h' or 's'.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep='\n ')

    for card in player.cards:
        print(card, end=' ')

def show_all(player, dealer):
    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card, end=' ')

    print("\nDealer's hand:", *dealer.cards, sep='\n ')
    print("Dealer's hand value:", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep='\n ')
    print("Player's hand value:", player.value)

def player_busts(player, dealer, chips):
    print("Player busts! Dealer wins.")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins! Dealer loses.")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts! Player wins.")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins! Player loses.")
    chips.lose_bet()

def push(player, dealer):
    print("It's a tie! Push.")

while True:
    print("Welcome to Blackjack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f"\nPlayer's total chips: {player_chips.total}")

    new_game = input("Would you like to play again? (y/n): ").lower()

    if new_game != 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break