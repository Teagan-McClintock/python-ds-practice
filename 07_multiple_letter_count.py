def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    freq_counter = {}
    for ltr in phrase:
        # can be if ltr in freq_counter
        # use in
        if freq_counter.get(ltr) == None:
            freq_counter[ltr] = 1
        else:
            freq_counter[ltr] += 1
    return freq_counter