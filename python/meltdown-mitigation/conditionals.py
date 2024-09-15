def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
def reactor_efficiency(voltage, current, theoretical_max_power):
    temp = (voltage * current/theoretical_max_power) * 100
    if temp >= 80:
        return "green"
    if 60 <= temp < 80:
        return "orange"
    if 30 <= temp < 60:
        return "red"
    return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    production_rate = temperature * neutrons_produced_per_second
    if production_rate < 0.9 * threshold:
        return "LOW"
    if production_rate <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"
