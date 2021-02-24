"""Module containing helper function(s) to find price after discount and/or
   taxes.
"""
import math

def price_after_discount(price: float, discount_percent: float) -> float:
    """Function to compute price after discount is applied."""
    if discount_percent > 1:
        raise ValueError("Error: Discount is more than 100%.")
    else:
        return price * (1 - discount_percent)


def price_after_tax(price: float, tax_percent: float) -> float:
    """Function to compute price after taxes are included."""
    return price * (1 + tax_percent)


def price_adjustment(price: float, adjustment: float) -> float:
    """More general function for computing price adjustments, than computing
       discounts or price increases separately.
    """
    if math.fabs(adjustment) > 1:
        raise ValueError("Error: Adjustment is more than 100% of price.")
    else:
        return price * (1 + adjustment)
