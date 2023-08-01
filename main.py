import random


def main():
    random_num = generat_random_number()

    print(
        """
                            game rules
          - cow mean it's right and in the right place
          - key means it's right but not in the right place
          - bull means it's a wrong number
          - write 4 numbers to guess the right number
          """
    )

    playing(random_num)


def generat_random_number():
    numbers_range = "0123456789"
    current_number = []

    for _ in range(4):
        random_char = random.choice(numbers_range)
        current_number.append(random_char)
        numbers_range = numbers_range.replace(random_char, "")

    return current_number


def playing(random_num):
    inputed_number = input()
    inputed_number_seq = [i for i in inputed_number]

    if inputed_number_seq == random_num:
        print("We got a winner here!!")
        return
    else:
        cows = 0
        bulls = 0
        keys = 0

        for i in range(4):
            if inputed_number_seq[i] == random_num[i]:
                cows += 1
            elif inputed_number_seq[i] in random_num:
                keys += 1
            else:
                bulls += 1
        print(
            f"""
              cows: {cows} | keys: {keys} | bulls: {bulls}

              try again
              """
        )
        playing(random_num)


if __name__ == "__main__":
    main()
