def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    friend_a_hobbies = a[-1]
    friend_b_hobbies = b[-1]
    for hobby in friend_a_hobbies:
        if hobby in friend_b_hobbies:
            return True

    return False

    # can use Set here
    # but how?? Isn't this solution more optimal? Or is there a way that a Set
    # can return True as soon as a duplicated item tries to enter the Set?