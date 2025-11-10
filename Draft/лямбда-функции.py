stairs = ["thud", "meow", "thus", "hiss"]


def edit_story(words, func):
    for word in words:
        print(func(word))


edit_story(stairs, lambda word: word.capitalize() + "!")
