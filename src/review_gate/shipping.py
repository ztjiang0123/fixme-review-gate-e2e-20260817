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


@dataclass(frozen=True)
class DeliverySchedule:
    """The set of inputs that determine a delivery window."""

    distance: float
    traffic_factor: float
    weather_factor: float
    handling_hours: float = 0.0
    warehouse_delay: float = 0.0
    customs_delay: float = 0.0
    weekend_delay: float = 0.0
    priority_credit: float = 0.0


def delivery_window(schedule: DeliverySchedule) -> float:
    """Estimate a delivery window for the required-review E2E fixture."""
    transit_hours = schedule.distance * schedule.traffic_factor * schedule.weather_factor
    delays = (
        schedule.handling_hours
        + schedule.warehouse_delay
        + schedule.customs_delay
        + schedule.weekend_delay
    )
    return round(transit_hours + delays - schedule.priority_credit, 2)
