
documents = []

num_of_docs = int(input("Ile dokumentów chcesz wprowadzić? "))

for i in range(num_of_docs):
    document = input(f"Podaj treść dokumentu {i}: ")
    documents.append(document)

search_word = input("Podaj słowo, którego wystąpienia chcesz policzyć: ").lower()

document_word_count = []

for index, doc in enumerate(documents):
    
    words = doc.lower().split()
    
    word_count = words.count(search_word)
    
    document_word_count.append((index, word_count))

sorted_documents = sorted(document_word_count, key=lambda x: x[1], reverse=True)

print('\nTen wyraz został wprowadzony: ', search_word)
print("\nDokumenty uszeregowane według liczby wystąpień słowa:")
sorted_document_numbers = [doc[0] for doc in sorted_documents]
print(sorted_document_numbers)