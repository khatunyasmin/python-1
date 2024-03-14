def multiples_of_seven(start, end):
    multiples = []
    for num in range(start, end + 1):
        if num % 7 == 0:
            multiples.append(num)
    return multiples

start_range = 1
end_range = 70

multiples_list = multiples_of_seven(start_range, end_range)
print("Multiples of 7 within the range", start_range, "to", end_range, ":", multiples_list)
