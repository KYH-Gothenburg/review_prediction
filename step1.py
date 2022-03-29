from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

def main():
    corpus = [
        "i love the book",
        "this book was not so great",
        "the fit is great",
        "i love the shoes"
    ]
    vectorizer = CountVectorizer()

    vectors = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(vectors.toarray())

    books = "Books"
    clothing = "Clothing"

    categories = [books, books, clothing, clothing]

    clf_svm = SVC(kernel='linear')
    clf_svm.fit(vectors, categories)

    test_x = ['i love this read', 'such a nice hat', 'what a great book']
    test_y = [books, clothing, books]

    test_vectors = vectorizer.transform(test_x)
    print("The result is: ", clf_svm.score(test_vectors, test_y))

    vectorizer = CountVectorizer(ngram_range=(1, 3))
    vectors = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(vectors.toarray())


if __name__ == '__main__':
    main()
