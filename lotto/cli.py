import dataclasses
import random
from tqdm import tqdm


# Simple settings using dataclasses
@dataclasses.dataclass
class Settings:
    maximum_lotto_number_range: int
    number_of_lotto_numbers: int
    number_of_tickets: int
    ticket_price: int


settings = Settings(maximum_lotto_number_range=69,
                    number_of_lotto_numbers=7,
                    number_of_tickets=100,
                    ticket_price=10)

class ChangeSettings():
    def __init__(self, settings: Settings) -> list[int]:
        """A Class to change any settings in a dataclass. Returns list of ints"""
        
        self.settings = settings
        self.red_color_code = red_color_code = "\033[91m"  # ANSI escape code for red color
        self.reset_color_code = reset_color_code = "\033[0m"  # ANSI escape code to reset color
        
        
    def start(self):
        
        
        print(f"""
            Choose one of the options:
                    
            '1'. Change maximum lotto number range. {self.red_color_code}Currently at {self.settings.maximum_lotto_number_range}{self.reset_color_code}
            '2'. Change number of lotto numbers. {self.red_color_code}Currently at {self.settings.number_of_lotto_numbers}{self.reset_color_code}
            '3'. Change number of tickets to simulate. {self.red_color_code}Currently at {self.settings.number_of_tickets}{self.reset_color_code}
            '4'. Change ticket price. {self.red_color_code}Currently at {self.settings.ticket_price}{self.reset_color_code}
            '5'. Apply and start.
                  
        """)
    
    def change_lotto_range(self):
        print("New maximum lotto range: ")
        new_number_range = input()
        
    def change_amount_lotto_numbers():
        print("New amount of lotto numbers: ")
        
        
        

def _generate_random_lotto_numbers() -> list[int]:
    """Generates a random lotto numbers and returns it in a list."""

    lotto_numbers = []

    while len(lotto_numbers) < settings.number_of_lotto_numbers:
        random_number = random.randint(1, settings.maximum_lotto_number_range)

        # Check number if unique
        is_unique = random_number not in lotto_numbers

        if is_unique:
            lotto_numbers.append(random_number)

    return lotto_numbers


def _guess_lotto_numbers(lotto_numbers: list[int]) -> tuple[int, int]:
    """
    It guesses the lotto using the _generate_random_lotto_numbers function, and it adds to the number of guesses,
    """

    total_guesses = 0
    total_money_amount = 0
    
    money_dictionary = {
        0: 0,  # No correct guesses
        1: 7,
        2: 13,
        3: 100,
        4: 1000,
        5: 10000,
        6: 100000,
        7: 5000000
    }

    
    for _ in tqdm(range(settings.number_of_tickets), desc="Guessing Lottery"):
        guesses = 0  # Reset guesses for each ticket
        user_lotto_guess = _generate_random_lotto_numbers()

        for i in range(settings.number_of_lotto_numbers):
            if user_lotto_guess[i] == lotto_numbers[i]:
                guesses += 1

        total_guesses += guesses
        if guesses in money_dictionary:
            total_money_amount += money_dictionary[guesses]

    total_money_amount -= settings.ticket_price * settings.number_of_tickets

    return total_guesses, total_money_amount



def cli() -> None:
    # Prints the random lotto numbers for debugging
    lotto_numbers = _generate_random_lotto_numbers()
    print(lotto_numbers)
    print(_guess_lotto_numbers(lotto_numbers))
    
    change_settings = ChangeSettings(settings)
    change_settings.start()

cli()