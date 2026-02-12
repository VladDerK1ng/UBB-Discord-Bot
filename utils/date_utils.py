"""
Utility functions for date calculations and operations
"""

import datetime


def days_until(target_month: int, target_day: int) -> int:
    """Calculate days remaining until a specific date"""
    now = datetime.datetime.now()
    current_year = now.year
    
    target_date = datetime.datetime(current_year, target_month, target_day)
    
    # If the date has passed this year, calculate for next year
    if target_date < now:
        target_date = datetime.datetime(current_year + 1, target_month, target_day)
    
    difference = target_date - now
    return difference.days


def hours_until(target_month: int, target_day: int) -> int:
    """Calculate hours remaining until a specific date"""
    now = datetime.datetime.now()
    current_year = now.year
    
    target_date = datetime.datetime(current_year, target_month, target_day)
    
    # If the date has passed this year, calculate for next year
    if target_date < now:
        target_date = datetime.datetime(current_year + 1, target_month, target_day)
    
    difference = target_date - now
    total_seconds = difference.total_seconds()
    return int(total_seconds // 3600)


def get_date_status(target_month: int, target_day: int) -> bool:
    """Check if a date has passed. Returns True if passed, False if future"""
    now = datetime.datetime.now()
    target_date = datetime.datetime(now.year, target_month, target_day)
    return target_date < now
