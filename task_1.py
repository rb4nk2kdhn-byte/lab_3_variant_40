PUNCTUATION = ".,!?;:"


def normalize_word(fragment):
    return fragment.strip(PUNCTUATION).lower()


def analyze_line(line, word_len):
    words = []

    for fragment in line.split():
        word = normalize_word(fragment)

        if word != "" and len(word) == word_len:
            words.append(word)

    frequencies = {}

    for word in words:
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1

    return words, frequencies


def analyze_text(n, word_len, query):
    frequencies = {}
    order = []
    query_count = 0
    query_first_line = None

    for line_number in range(1, n + 1):
        line = input()

        words, line_frequencies = analyze_line(line, word_len)

        print(
            f"Рядок {line_number}: слів {len(words)}; "
            f"різних {len(line_frequencies)}"
        )

        for word in words:
            if word not in frequencies:
                frequencies[word] = 0
                order.append(word)

            frequencies[word] += 1

            if word == query:
                query_count += 1

                if query_first_line is None:
                    query_first_line = line_number

    return frequencies, order, query_count, query_first_line


n = int(input())
word_len = int(input())
query = normalize_word(input())

frequencies, order, query_count, query_first_line = analyze_text(
    n, word_len, query
)

total_words = sum(frequencies.values())

print(f"Усього слів: {total_words}")
print(f"Різних слів: {len(frequencies)}")
print("Частоти:")

if len(frequencies) == 0:
    print("немає")
    print("Найчастіше: немає")
else:
    for word in order:
        print(f"{word}: {frequencies[word]}")

    most_common = order[0]

    for word in order:
        if frequencies[word] > frequencies[most_common]:
            most_common = word

    print(f"Найчастіше: {most_common} ({frequencies[most_common]})")

if query_first_line is None:
    query_first_line = "немає"

print(
    f"Запит: {query}; входжень: {query_count}; "
    f"перший рядок: {query_first_line}"
)