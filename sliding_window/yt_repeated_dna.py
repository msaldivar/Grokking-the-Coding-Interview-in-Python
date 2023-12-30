"""
Repeated DNA Sequences - LeetCode 187

Grokking Life

Algo:
Rabin-Karp Algorithm

Solution Summary:
* We'll create a window of size 10, the length of the dna sequence 

"""

def find_repeated_dna_sequences(dna: str) -> list[str]:
    """LeetCode 187"""

    repeated_seq = {}
    seq_len = 10
    result_set = set()

    for i in range(len(dna) - seq_len + 1):
        window = str(dna[i: i + seq_len])
        if window not in repeated_seq:
            repeated_seq[window] = 1
        else:
            repeated_seq[window] += 1
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