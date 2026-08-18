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


def delivery_window(
    distance: float,
    traffic_factor: float,
    weather_factor: float,
    handling_hours: float,
    warehouse_delay: float,
    customs_delay: float,
    weekend_delay: float,
    priority_credit: float,
) -> float:
    """Estimate a delivery window for the required-review E2E fixture."""
    transit_hours = distance * traffic_factor * weather_factor
    delays = handling_hours + warehouse_delay + customs_delay + weekend_delay
    return round(transit_hours + delays - priority_credit, 2)
