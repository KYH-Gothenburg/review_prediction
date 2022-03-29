import re
import string
import contractions


def clean_text(text):
    text = text.lower()

    # Remove punctuation marks
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # Remove digits from the text
    text = re.sub(r'\w*\d\w*', '', text)
    return text


def fix_text(text):
    # Contractions will expand words such as it's to it is
    text = contractions.fix(text)
    # Call our clean_text function
    text = clean_text(text)

    # Read the stopwords from the stopwords.txt file and remove line breaks
    # The result will be a list of strings
    stopwords = [word.strip() for word in open('stopwords.txt')]
    # Remove all stopwords from the text
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text



def main():
    test_text = "In 1987 I read this book for the first time. It was great then, and is still the best."
    test_text = fix_text(test_text)
    print(test_text)


if __name__ == '__main__':
    main()
