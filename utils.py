import numpy as np

def format_currency(value):
    """Formats numerical value to Kenyan Shilling string."""
    return f"KSh {value:,.2f}"

def calculate_percentage_change(old_val, new_val):
    """Computes growth/decrease percentage."""
    if old_val == 0: return 0
    return ((new_val - old_val) / old_val) * 100

def get_growth_label(change):
    """Returns a visual indicator for inflation status."""
    return "📈 Up" if change > 0 else "📉 Down"
