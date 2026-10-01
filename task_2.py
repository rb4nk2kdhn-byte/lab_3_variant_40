PUNCTUATION = ".,!?;:"


def normalize_word(fragment):
    return fragment.strip(PUNCTUATION).lower()


def analyze_text(text, min_len):
    frequencies = {}
    order = []

    for fragment in text.split():
        word = normalize_word(fragment)

        if word != "" and len(word) >= min_len:
            if word not in frequencies:
                frequencies[word] = 0
                order.append(word)

            frequencies[word] += 1

    return frequencies, order


def select_common_words(freq1, freq2, order1, min_total):
    common = [word for word in order1 if word in freq2]

    selected = [
        word
        for word in common
        if freq1[word] + freq2[word] >= min_total
    ]

    return common, selected


min_len = int(input())
min_total = int(input())

text1 = input()
text2 = input()

freq1, order1 = analyze_text(text1, min_len)
freq2, order2 = analyze_text(text2, min_len)

common, selected = select_common_words(
    freq1, freq2, order1, min_total
)

print(f"Спільних слів: {len(common)}")
print(f"Відібраних спільних: {len(selected)}")
print("Відібрані слова й частоти:")

if len(selected) == 0:
    print("немає")
else:
    for word in selected:
        print(f"{word}: {freq1[word]} | {freq2[word]}")

only_first = [
    word for word in order1
    if word not in freq2
]

only_second = [
    word for word in order2
    if word not in freq1
]

if len(only_first) == 0:
    print("Лише в першому: немає")
else:
    print("Лише в першому: " + ", ".join(only_first))

if len(only_second) == 0:
    print("Лише в другому: немає")
else:
    print("Лише в другому: " + ", ".join(only_second))

total_selected = sum(
    freq1[word] + freq2[word]
    for word in selected
)

print(f"Разом входжень відібраних: {total_selected}")


# цикл
selected_loop = []

for word in common:
    if freq1[word] + freq2[word] >= min_total:
        selected_loop.append(word)


# включення
selected_comprehension = [
    word
    for word in common
    if freq1[word] + freq2[word] >= min_total
]


# генератор
selected_generator = list(
    word
    for word in common
    if freq1[word] + freq2[word] >= min_total
)

print(
    "Цикл і включення: "
    + ("так" if selected_loop == selected_comprehension else "ні")
)

print(
    "Цикл і генератор: "
    + ("так" if selected_loop == selected_generator else "ні")
)