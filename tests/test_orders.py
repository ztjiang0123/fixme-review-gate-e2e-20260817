from review_gate import Invoice, invoice_total, shipment_quote


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
    assert shipment_quote(2, 10, 0.5, 1, 2, 3, 4, 5) == 15
