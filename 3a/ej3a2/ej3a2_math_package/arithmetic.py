# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
		return base ** exponent
	raise ValueError("Both base and exponent must be numbers.")

def square_root(num_1: float) -> float:
	if isinstance(num_1, (int, float)):
		return math.sqrt(num_1)
	raise ValueError("num_1 must be a number.")	


