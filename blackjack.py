import pprint

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self) -> None:
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

    def __str__(self) -> str:
        return pprint.pformat([str(card) for card in self.cards])


def test_deck():
    new_deck = Deck()
    print(new_deck)

    new_deck.shuffle()
    print(new_deck)


# test_deck()


class Hand:

    def __init__(self):
        self.cards: list[Card] = []
        self.value: int = 0
        self.aces: int = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __str__(self) -> str:
        return pprint.pformat([str(card) for card in self.cards]) + '\n' + str(self.value) + '\n' + str(self.aces)


def test_hand():
    test_deck = Deck()
    test_deck.shuffle()

    test_player = Hand()
    test_player.add_card(test_deck.deal())
    test_player.add_card(test_deck.deal())
    print(test_player)


# test_hand()


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self) -> None:
        self.total += self.bet

    def lose_bet(self) -> None:
        self.total -= self.bet


def take_bet(chips: Chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'You do not have enough chips!  You have {
                      chips.total} chips total')
            else:
                break


def hit(deck: Deck, hand: Hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck: Deck, hand: Hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands.  Dealer's turn")
            playing = False

        else:
            print('I did not understand that, please enter h or s only! ')
            continue

        break


def show_some(player: Hand, dealer: Hand):
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\n Players's Hand: ")
    [print(card) for card in player.cards]


def show_all(player: Hand, dealer: Hand):
    print("\n Dealer's Hand: ", *dealer.cards, sep='\n')
    print(f"Value of Dealer's hand is {dealer.value}")

    print("\n Player's Hand: ", *player.cards, sep='\n')
    print(f"Value of Player's hand is {player.value}")


def player_burst(player: Hand, dealer: Hand, chips: Chips):
    print('Bust Player!')
    chips.lose_bet()


def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print('Player Win!')
    chips.win_bet()


def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print('Bust Dealer!')
    player_wins(player, dealer, chips)


def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print('Dealer Win!')
    chips.lose_bet()


def push(player: Hand, dealer: Hand):
    print('Dealer and player tie! Push')


def blackjack_game():
    global playing
    player_chips = Chips()

    while True:
        print("Welcome to BlackJack")

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_burst(player_hand, dealer_hand, player_chips)
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

        print(f"\n Player total chips are at : {player_chips.total}")

        new_game = input("Another game? y/n: ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing!')
            break


blackjack_game()
