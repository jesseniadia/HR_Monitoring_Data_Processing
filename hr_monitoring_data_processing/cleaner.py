def filter_nondigits(data: list) -> list:   
    """
    Filters out non-digit values from a list of strings, it strips both leading and trailing whitespace by removing newline characters and converts valid numeric strings into integers.

    Args:
    data (list): A list of strings, some of which may contain non-numeric characters.

    Returns:
    list: A list of integers containing only the valid numeric values from the input list.

    """

    valid_numbers = []

    #in_data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]

    for numbers in data:
        numbers = numbers.strip()

        if numbers.isdigit():
            valid_numbers.append(int(numbers))

    return valid_numbers