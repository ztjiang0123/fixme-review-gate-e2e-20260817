from review_gate import invoice_total


def test_invoice_total() -> None:
    assert invoice_total(100, 0.1, 5, 4, 2, 1, 3, 1) == 110

