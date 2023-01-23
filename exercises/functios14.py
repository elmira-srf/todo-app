low = 0
high = 100

def water_state(temperature):
    if temperature <= low:
        return "Solid"
    elif low < temperature < high:
        return "Liquid"
    else:
        return "Gas"
