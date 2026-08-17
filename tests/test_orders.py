from review_gate import Invoice, Shipment, invoice_total, shipment_quote


def test_invoice_total() -> None:
    invoice = Invoice(
        subtotal=100,
        tax_rate=0.1,
        shipping=5,
        discount=4,
        handling=2,
        insurance=1,
        store_credit=3,
        loyalty_credit=1,
    )
    assert invoice_total(invoice) == 110


def test_shipment_quote() -> None:
    shipment = Shipment(
        weight=2,
        distance=10,
        base_rate=0.5,
        fuel_surcharge=1,
        residential_fee=2,
        weekend_fee=3,
        insurance_fee=4,
        discount=5,
    )
    assert shipment_quote(shipment) == 15
