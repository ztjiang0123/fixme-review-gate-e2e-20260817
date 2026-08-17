def invoice_total(
    subtotal: float,
    tax_rate: float,
    shipping: float,
    discount: float,
    handling: float,
    insurance: float,
    store_credit: float,
    loyalty_credit: float,
) -> float:
    """Compute an invoice total; intentionally has too many parameters."""
    taxed = subtotal * (1 + tax_rate)
    additions = shipping + handling + insurance
    credits = discount + store_credit + loyalty_credit
    return round(taxed + additions - credits, 2)

