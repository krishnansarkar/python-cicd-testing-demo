def calculate_total(items: list[dict], discount_code: str = None, tax_rate: float = 0.08) -> float:
    """
    Calculates final cart price including discounts and sales tax.
    Each item in items should be a dict: {'price': float, 'quantity': int}
    """
    if not items:
        return 0.0

    # Calculate subtotal, ignoring any items with invalid/negative quantities
    subtotal = sum(
        item["price"] * item["quantity"]
        for item in items
        if item.get("quantity", 0) > 0 and item.get("price", 0) > 0
    )

    # Apply valid discount codes
    discounts = {
        "SAVE10": 0.10,
        "HALF": 0.50,
    }
    discount_rate = discounts.get(discount_code, 0.0)
    discounted_subtotal = subtotal * (1 - discount_rate)

    # Apply sales tax and round to two decimal places
    total = discounted_subtotal * (1 + tax_rate)
    return round(total, 2)