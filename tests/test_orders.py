from review_gate import Invoice, invoice_total


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
