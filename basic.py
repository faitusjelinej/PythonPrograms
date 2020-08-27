def sentence_maker(phrase):
    interagative = ("how","why","what")
    capital = phrase.capitalize()
    if phrase.startswith(interagative):
        return " {}?".format(capital)
    else:
        return " {}.".format(capital)




result = []



while True:
    user_input = input("Say Something: ")
    if user_input == '\end':
        break
    else:
        result.append(sentence_maker(user_input))


print("".join(result))
