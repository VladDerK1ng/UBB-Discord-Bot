"""
Validation functions for Discord Bot commands
"""

from config import GRADE_MINIMUM, GRADE_MAXIMUM


def validate_grades(*grades: int) -> tuple[bool, str]:
    """
    Validate if grades are within acceptable range
    Returns (is_valid, error_message)
    """
    if not grades:
        return False, "Nicio nota introdusa! Scrie notele dupa comanda, ex: !medie 10 9 8"
    
    for grade in grades:
        if grade < GRADE_MINIMUM or grade > GRADE_MAXIMUM:
            return False, f"Notele trebuie sa fie intre {GRADE_MINIMUM} si {GRADE_MAXIMUM}!"
    
    return True, ""


def validate_dice_value(value: int) -> tuple[bool, str]:
    """
    Validate dice/roll value
    Returns (is_valid, error_message)
    """
    if value < 1:
        return False, "Zarul trebuie sa aiba minim 1!"
    
    return True, ""
