from typing import Union, List

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


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

    def deal_onecard(self) -> Card:
        return self.cards.pop()


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.holding_cards: list[Card] = []

    def remove_one_card(self) -> Card:
        return self.holding_cards.pop(0)

    def add_cards(self, cards: Union[List[Card], Card]) -> None:
        if isinstance(cards, List):
            self.holding_cards.extend(cards)
        else:
            self.holding_cards.append(cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.holding_cards)} cards.'


def print_win_lost_msg(loser: str, winner: str):
    print(f"{loser} unable to play war! Game Over at War")
    print(f"{winner} Wins! {loser} Loses!")


number_of_cards_for_war = 3


def play_war_game():
    # setup
    player_one = Player('One')
    player_two = Player('Two')
    new_deck = Deck()
    new_deck.shuffle()
    for _ in range(26):
        player_one.add_cards(new_deck.deal_onecard())
        player_two.add_cards(new_deck.deal_onecard())

    round_number = 0
    game_on = True

    while game_on:

        round_number += 1
        print(f'Round {round_number}')

        if (len(player_one.holding_cards)) < 1:
            print('Player One out of cards!')
            print('Player Two Wins!')
            game_on = False
            break

        if (len(player_two.holding_cards)) < 1:
            print('Player Two out of cards!')
            print('Player One Wins!')
            game_on = False
            break

        player_one_cards_on_table: list[Card] = []
        player_one_cards_on_table.append(player_one.remove_one_card())

        player_two_cards_on_table: list[Card] = []
        player_two_cards_on_table.append(player_two.remove_one_card())

        at_war = True

        while at_war:
            if player_one_cards_on_table[-1].value > player_two_cards_on_table[-1].value:
                player_one.add_cards(player_one_cards_on_table)
                player_one.add_cards(player_two_cards_on_table)
                at_war = False

            elif player_one_cards_on_table[-1].value < player_two_cards_on_table[-1].value:
                player_two.add_cards(player_one_cards_on_table)
                player_two.add_cards(player_two_cards_on_table)
                at_war = False

            else:
                print('WAR!')
                if len(player_one.holding_cards) < number_of_cards_for_war:
                    print_win_lost_msg('Player One', 'Player Two')
                    game_on = False
                    break
                if len(player_two.holding_cards) < number_of_cards_for_war:
                    print_win_lost_msg('Player Two', 'Player One')
                    game_on = False
                    break

                for _ in range(number_of_cards_for_war):
                    player_one_cards_on_table.append(
                        player_one.remove_one_card())
                    player_two_cards_on_table.append(
                        player_two.remove_one_card())


play_war_game()
