from dataclasses import dataclass


@dataclass(frozen=True)
class Shipment:
    """The set of inputs that determine a shipment quote."""

    weight: float
    distance: float
    base_rate: float
    fuel_surcharge: float = 0.0
    residential_fee: float = 0.0
    weekend_fee: float = 0.0
    insurance_fee: float = 0.0
    discount: float = 0.0


def shipment_quote(shipment: Shipment) -> float:
    """Calculate a deterministic shipment quote for the E2E fixture."""
    variable_cost = shipment.weight * shipment.distance * shipment.base_rate
    fees = (
        shipment.fuel_surcharge
        + shipment.residential_fee
        + shipment.weekend_fee
        + shipment.insurance_fee
    )
    return round(variable_cost + fees - shipment.discount, 2)
