def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    lower_phrase = phrase.split(" ")
    titled_phrase = []
    for word in lower_phrase:
        title = word[0].upper() + word[1::]
        titled_phrase.append(title)

    return " ".join(titled_phrase)
