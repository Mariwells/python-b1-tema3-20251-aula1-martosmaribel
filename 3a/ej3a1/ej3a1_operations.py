# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
        raise ValueError("Both num_1 and num_2 must be numbers.")
    return num_1 + num_2


def subtract(num_1: float, num_2: float) -> float:
    if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
        raise ValueError("Both num_1 and num_2 must be numbers.")
    return num_1 - num_2
    pass


def multiply(num_1: float, num_2: float) -> float:
    if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
        raise ValueError("Both num_1 and num_2 must be numbers.")
    return num_1 * num_2


def divide(num_1: float, num_2: float) -> float:
    if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
        raise ValueError("Both num_1 and num_2 must be numbers.")
    if num_2 == 0:
        raise ValueError("num_2 cannot be zero.")
    return num_1 / num_2    
    pass
