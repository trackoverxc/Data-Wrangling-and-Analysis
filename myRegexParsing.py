import re
word = r'\w+'
sentence = "I love using Regex!"
re.findall(word, sentence)

search_result = re.search(word, sentence)
search_result
search_result.group()

match_result = re.match(word, sentence)
match_result
match_result.group()

capitalized_word = r'[A-Z]\w+'
search_result = re.search(capitalized_word, sentence)
search_result
search_result.group()

match_result = re.match(capitalized_word, sentence)
match_result
match_result.group()

numbers = r'\d+'
sentenceWithDigits = """Even though the airport is 65,070 meters away, I still hear at least 4 planes!"""
search_result = re.search(numbers, sentenceWithDigits)
search_result
search_result.group()

re.findall(numbers, sentenceWithDigits)
thousands_numbers = r'(\d+,\d+|\d+)'
re.findall(thousands_numbers, sentenceWithDigits)

city_state = r'(?P<city>[\w\s]+), (?P<state>[A-Z]{2})'
my_address = 'My House, 123 Main Street, Los Angeles, CA 90013'
for city_st in re.finditer(city_state, my_address):
    print(city_st.group('city'))
    
