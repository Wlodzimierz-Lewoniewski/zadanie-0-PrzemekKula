def main():
    num_documents = int(input().strip())
    documents = []
    for _ in range(num_documents):
        documents.append(input().strip())

    num_keywords = int(input().strip())
    keywords = []
    for _ in range(num_keywords):
        keywords.append(input().strip())

    for keyword in keywords:
        keyword_count = [(index, doc.lower().count(keyword.lower())) for index, doc in enumerate(documents)]
        sorted_documents = sorted(keyword_count, key=lambda x: (-x[1], x[0]))
        sorted_indices = [index for index, _ in sorted_documents]
        print(sorted_indices)

if __name__ == "__main__":
    main()