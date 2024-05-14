def compute_metrics(n, m, r):
    l_values = [5, 11, 15, 20, 25, 30, 35, 40]
    results = []
    
    for l in l_values:
        # compute speed-up
        matches_expected = (m * n) / (4 ** l)
        time_seed_and_extend = (m + n) + (r ** 2 * matches_expected)
        speed_up = (m * n) / time_seed_and_extend
        
        # compute sensitivity
        identity = 0.85
        p_match = (1 - (1 - identity) ** l)
        sensitivity = 1 - (1 - p_match) ** (r - l + 1)
        
        results.append((l, speed_up, sensitivity))
    
    return results

n = m = 10**7
r = 100

results = compute_metrics(n, m, r)
print("l\tSpeed-Up\tSensitivity")
for l, speed_up, sensitivity in results:
    print(f"{l}\t{speed_up:.2e}\t{sensitivity:.4f}")
