import json


def main():
    ITERATIONS = 100000

    with open('Pet_Supplies_5.json') as in_file:
        with open(f'pet_supplies_{ITERATIONS}.json', 'w') as out_file:
            for _ in range(ITERATIONS):
                line = in_file.readline()
                data = json.loads(line)
                a, b = data['helpful']
                if b > 0:
                    c = a / b
                    print()
                    if c > 0.66:
                        out_file.write(line)


if __name__ == '__main__':
    main()
