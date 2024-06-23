from art import logo
from data import data
import random

print(logo)


def get_random_account():
    return random.choice(data)

def format_data(account):
    """This formats the data nicely to print out"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name} a {description} from {country} '

def game_go():
    game_should_continue = True
    choice_1 = get_random_account()
    choice_2 = get_random_account()

    while game_should_continue:
        choice_1 = choice_2
        choice_2 = get_random_account()

        while choice_1 == choice_2:
            choice_2 = get_random_account()

        def correct_choice(a,b):
            """if follower count in choice 1 is greater than follower count in choice 2,
            return follower count of a, else return follower count of choice b"""
            correct_choice = a if a > b else b
            return correct_choice

        user_guess = input(f'Who has more followers? \n'
                           f'(A) {format_data(choice_1)} \n'
                           f'or \n'
                           f'(B) {format_data(choice_2)}? ').upper()

        user_guess = choice_1['follower_count'] if user_guess == 'A' else choice_2['follower_count']

        a = choice_1['follower_count']
        b = choice_2['follower_count']

        right_num = correct_choice(a, b)

        if user_guess == right_num:
            print('You are correct')
        else:
            print('Sorry, not correct!')
            break


if __name__ == '__main__':
    game_go()



