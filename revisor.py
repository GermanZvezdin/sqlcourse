import operator
def process_text(file_path):
    with open(file_path, 'r') as file:
        #text = file.read().lower()
        frequencies = {}
        while text := file.readline():
            text =text.lower()

            symbols = ['.', '!', ',', '...', '?']
            for sym in symbols:
                text = text.replace(sym, '')

            text = text.replace('\n', ' ')

            l = text.split(' ')


            for word in l:
                frequencies[word] = l.count(word)

        frequencies = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

        with open('result.txt', 'w') as output:
            for word, count in frequencies:
                output.write(f"{count}: {word}\n")
def main():
    file_path = "revisor.txt"
    process_text(file_path)

if __name__ == '__main__':
    main()