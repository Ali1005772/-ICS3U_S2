import math

def hx(TdegC: float, dewPtC: float) -> float:
    """
    Calculates the humidex, given:
    TdegC: air temperature in degrees Celsius
    dewPtC: dew point temperature in degrees Celsius
    Returns:
    Humidex temperature in degrees Celsius (float)
    """
    # Calculate p using the formula:
    p = 5417.753 * (1/273.15 - 1/(273.15 + dewPtC))
    
    # Calculate the exponent term e^p
    e_p = math.exp(p)
    
    # Calculate humidex according to formula:
    hTemp = TdegC + (5/9) * (6.11 * e_p - 10)
    
    return hTemp

def humidex_warning(hTemp: float) -> str:
    """
    Returns health warning based on humidex value
    """
    if hTemp < 30:
        return "Normal"
    elif 30 <= hTemp < 39:
        return "Causes some discomfort"
    elif 39 <= hTemp < 44:
        return "Causes great discomfort"
    elif 44 <= hTemp < 49:
        return "Considered dangerous"
    else:  # 49 or above
        return "Heat stroke is very likely"

# Main Program - DO NOT MODIFY!
T = 28.0
D = 26.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f  Warning: %s" % (h, T, D, humidex_warning(h)))

T = 30.0
D = 20.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f  Warning: %s" % (h, T, D, humidex_warning(h)))

T = 26.0
D = 28.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f  Warning: %s\n" % (h, T, D, humidex_warning(h)))
