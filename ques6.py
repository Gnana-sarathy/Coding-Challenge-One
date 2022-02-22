def trailing_zeros(num):
    if num < 5:
        return 0
    count = 0
    # At each five steps trailing zero is incremented by 1
    while num >= 5:
        num //= 5
        count += num

    return count


print(trailing_zeros(30))
