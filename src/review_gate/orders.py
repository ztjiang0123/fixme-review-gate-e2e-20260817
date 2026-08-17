from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    """The set of monetary components that make up an invoice."""

    subtotal: float
    tax_rate: float
    shipping: float = 0.0
    discount: float = 0.0
    handling: float = 0.0
    insurance: float = 0.0
    store_credit: float = 0.0
    loyalty_credit: float = 0.0


def invoice_total(invoice: Invoice) -> float:
    """Compute an invoice total from its component amounts."""
    taxed = invoice.subtotal * (1 + invoice.tax_rate)
    additions = invoice.shipping + invoice.handling + invoice.insurance
    credits = invoice.discount + invoice.store_credit + invoice.loyalty_credit
    return round(taxed + additions - credits, 2)
