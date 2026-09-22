def calculate_average(values):
    if not values:
        return None

    return sum(values) / len(values)

# This gives the amount by which an observed value differs from the speaker's usual value.
def calculate_difference(actual, usual):
    
    if actual is None or usual is None:
        return None

    return actual - usual

# This checks whether a difference is small enough to be considered normal according to one of the classification tolerances.
def value_within_tolerance(value, tolerance):
    
    if value is None:
        return False

    return abs(value) <= tolerance

# Formatting metric values for better presentation
def format_metric(value, decimal_places=2):
    if value is None:
        return "N/A"

    return round(value, decimal_places)