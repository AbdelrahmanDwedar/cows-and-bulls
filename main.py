from generate_random_number import generate_random_number
from playing import playing


def main():
    random_num = generate_random_number()

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


if __name__ == "__main__":
    main()
