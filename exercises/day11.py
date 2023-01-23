def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return [maximum, minimum]

print(f"Max: {get_max()[0]}, Min: {get_max()[1]}")