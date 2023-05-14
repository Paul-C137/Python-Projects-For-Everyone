from deep_translator import GoogleTranslator

with open('sample_german.txt', 'r') as text:
    for line in text:
        result = GoogleTranslator(source='de', target='en').translate(line)
        print(result)
        input("Continue? (press enter)")