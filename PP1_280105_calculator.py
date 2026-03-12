def Add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")

    if ",," in numbers:
        raise ValueError("Zly format")

    nums = numbers.split(",")

    suma = 0

    for n in nums:
        if n == "":
            raise ValueError("Zly format")

        suma += int(n)

    return suma