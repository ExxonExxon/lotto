import dataclasses
import random


# Simple settings using dataclasses
@dataclasses.dataclass
class Settings:
    maximum_lotto_number_range: int
    number_of_lotto_numbers: int
    number_of_tickets: int


settings = Settings(maximum_lotto_number_range=69,
                    number_of_lotto_numbers=7,
                    number_of_tickets=200)


def check_duplicate_lotto_numbers(lotto_numbers: list[int], number_to_check: int) -> bool:
    """Checks if the there is a lotto number that is the same as the generated lotto number,
    if False it means that there is a duplicate lotto number
    """

    return number_to_check in lotto_numbers


def _generate_random_lotto_numbers() -> list[int]:
    """Generates a random lotto numbers, and it makes sure they are unique using the check_duplicate_lotto_numbers
    function"""

    lotto_numbers = []

    while len(lotto_numbers) < settings.number_of_lotto_numbers:
        random_number = random.randint(1, settings.maximum_lotto_number_range)

        # Check number if unique
        is_unique = not check_duplicate_lotto_numbers(lotto_numbers, random_number)

        if is_unique:
            lotto_numbers.append(random_number)

    return lotto_numbers


def _guess_lotto_numbers(lotto_numbers: list[int]) -> int:
    """
    It guesses the lotto using the _generate_random_lotto_numbers function, and it adds to the number of guesses,

    """

    guesses = 0

    for _ in range(settings.number_of_tickets):

        # Generate lotto numbers using the _generate_random_lotto_numbers function
        user_lotto_guess = _generate_random_lotto_numbers()

        for i in user_lotto_guess:
            if i in lotto_numbers:
                guesses += 1

    return guesses


def cli() -> None:
    # Prints the random lotto numbers for debugging
    lotto_numbers = _generate_random_lotto_numbers()
    print(lotto_numbers)
    print(_guess_lotto_numbers(lotto_numbers))
