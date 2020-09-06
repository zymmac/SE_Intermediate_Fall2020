# 3-10. Every Function: Think of something you could store in a list. 
#   For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#   Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

languages = ['javascript', 'python', 'java', 'php']

print(f'In alphabetical order, the top languages from 2019 are {sorted(languages)}.')

languages.append('c#')
print(f'There are now {len(languages)} languages in our list! The last item is {languages[-1]}!')

languages.reverse()
print(f'The list from least to most popular is {languages}.')
languages.reverse()
print(f'But our list is still organized by most to least popular: {languages}')

first_language = languages.pop(0)
print(f'If we remove the most popular language, {first_language}, {languages[0]} becomes the most popular language of all!')

print(f'There are now {len(languages)} languages in our list!')

languages.sort()
print(f'If we want this list organized by alphabetical order, then: {languages}. We can also get it reversed:')
languages.sort(reverse=True)
print(languages)

languages.insert(0, 'javascript')
print('Let\'s return javascript to the list and sort it again!')
languages.sort()
print(languages)

print("Let's delete PHP from the list!")
languages.remove('php')
print(languages)

print(f'finally, let\'s just delete all {len(languages)} items from the list!')

del languages[0]
del languages[0]
del languages[0]
del languages[0]

print(languages)
