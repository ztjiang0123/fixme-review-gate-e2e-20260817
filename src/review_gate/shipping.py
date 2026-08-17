def shipment_quote(
    weight: float,
    distance: float,
    base_rate: float,
    fuel_surcharge: float,
    residential_fee: float,
    weekend_fee: float,
    insurance_fee: float,
    discount: float,
) -> float:
    """Calculate a deterministic shipment quote for the E2E fixture."""
    variable_cost = weight * distance * base_rate
    fees = fuel_surcharge + residential_fee + weekend_fee + insurance_fee
    return round(variable_cost + fees - discount, 2)
