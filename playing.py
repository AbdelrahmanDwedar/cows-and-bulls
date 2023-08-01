def playing(random_num):
    inputed_number = input("> ")
    inputed_number_seq = [i for i in inputed_number]

    if inputed_number_seq == random_num:
        print("We got a winner here!!")
        return
    else:
        cows = 0
        bulls = 0

        for i in range(4):
            if inputed_number_seq[i] == random_num[i]:
                cows += 1
            elif inputed_number_seq[i] in random_num:
                bulls += 1
        print(
            f"""
              cows: {cows} |  bulls: {bulls}

              try again
              """
        )
        playing(random_num)
