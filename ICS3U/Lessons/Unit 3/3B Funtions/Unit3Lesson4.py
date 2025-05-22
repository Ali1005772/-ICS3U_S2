import math

def wc(TdegC: float, windKPH: float) -> float:
    """
    Calculates the wind chill temperature.
    TdegC: air temperature in degrees Celsius
    windKPH: wind speed in kilometers per hour
    Returns:
    Wind chill temperature (float)
    """
    # Apply the formula step by step
    vTemp = 13.12 + 0.6215 * TdegC
    vTemp = vTemp - 11.37 * math.pow(windKPH, 0.16)
    vTemp = vTemp + 0.3965 * TdegC * math.pow(windKPH, 0.16)
    return vTemp

def risk_message(wind_chill: float) -> str:
    """
    Returns the risk category message based on wind chill temperature
    """
    if 0 >= wind_chill > -9:
        return "Low risk"
    elif -10 >= wind_chill > -27:
        return "Moderate risk of hypothermia"
    elif -28 >= wind_chill > -39:
        return "High risk of frostbite"
    elif -40 >= wind_chill > -47:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif -48 >= wind_chill > -54:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    elif wind_chill <= -55:
        return "Extreme risk: exposed skin freezes in under 2 minutes"
    else:
        return "No risk"

# Main program
test_values = [
    (-5.0, 10.0),
    (-20.0, 20.0),
    (-45.0, 40.0)
]

for T, W in test_values:
    WC = wc(T, W)
    print("WC=%8.3f T=%8.3f W=%6.3f km/h  Risk: %s" % (WC, T, W, risk_message(WC)))
