from fuzzywuzzy import fuzz
from fuzzywuzzy import process

user_search_one = "How to learn Python Data Wrangling"
user_search_two = "How to learn python charming"

fuzz.ratio(user_search_one, user_search_two)
fuzz.partial_ratio(user_search_one, user_search_two)
fuzz.token_sort_ratio(user_search_one, user_search_two)
fuzz.token_set_ratio(user_search_one, user_search_two)

my_favorite_foods = 'pizza, sushi, malaysian stirfry'
my_misspelled_words = 'pizzah, sewshy, malaisiayn stirfri'

fuzz.ratio(my_favorite_foods, my_misspelled_words)
fuzz.partial_ratio(my_favorite_foods, my_misspelled_words)
fuzz.token_sort_ratio(my_favorite_foods, my_misspelled_words)
fuzz.token_set_ratio(my_favorite_foods, my_misspelled_words)

choices = ['Python', 'R', 'Julia', 'Java', 'Scala', 'Go']
process.extract('jlia', choices, limit=2)

process.extractOne('java virtual engine', choices)
