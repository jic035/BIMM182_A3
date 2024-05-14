def l_mers(s, l):
    l_mers = []
    for i in range(len(s) - l + 1):
        l_mers.append(s[i:i+l])
    return l_mers

def expected_val(l_mers, f_A, f_T, f_C, f_G, m, l):
    freqency = [1 for _ in range(len(l_mers))]
    for i in range(len(l_mers)):
        for nuc in l_mers[i]:
            if nuc == 'A':
                freqency[i] *= f_A
            elif nuc == 'T':
                freqency[i] *= f_T
            elif nuc == 'C':
                freqency[i] *= f_C
            else:
                freqency[i] *= f_G
    sum_freq = 0
    for freq in freqency:
        sum_freq += freq
    return sum_freq * (m - l + 1)

lmers = l_mers("AATAAGCCGC", 5)
print(lmers)
e_val = expected_val(lmers, 0.1, 0.1, 0.4, 0.4, 10, 5)
print(e_val)


