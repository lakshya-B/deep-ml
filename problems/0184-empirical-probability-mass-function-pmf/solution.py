def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    counter = {}
    n = len(samples)
    for index in range(n):
        ele = samples[index]
        if ele in counter:
            counter[ele] += 1
        else:
            counter[ele] = 1
    output = []
    for key, value in counter.items():
        output.append((key, value/n))
    return output