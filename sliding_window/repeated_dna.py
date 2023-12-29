




def find_repeated_sequences(s, seq_len):


    repeated = {}
    result_set = set()

    for i in range(len(s) - seq_len + 1):
        window = str(s[i: i + seq_len])
        if window not in repeated:
            repeated[window] = 1
    
        elif window in repeated:
            repeated[window] += 1
            result_set.add(window)

    return list(result_set)

def main():
    """"""
    dna = "AAAAACCCCCAAAAACCCCCC"
    seq_len = 8
    print(f"{find_repeated_sequences(dna, seq_len)}")

    dna = "GGGGGGGGGGGGGGGGGGGGGGGGG"
    seq_len = 9
    print(f"{find_repeated_sequences(dna, seq_len)}")


    dna = "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT"
    seq_len = 10
    print(f"{find_repeated_sequences(dna, seq_len)}")
    

    dna = "ATATATATATATATAT"
    seq_len = 6
    print(f"{find_repeated_sequences(dna, seq_len)}")


if __name__ == "__main__":
    main()