from datetime import datetime
from .models import Receipt


def generate_receipt_number():
    current_year = datetime.now().year

    # Check for existing receipts for the current year
    last_receipt = Receipt.objects.filter(year=current_year).order_by('-number').first()

    if last_receipt:
        next_number = last_receipt.number + 1
    else:
        next_number = 1  # Start from 1 if no receipts exist for the current year

    # Create a new receipt instance
    new_receipt = Receipt.objects.create(number=next_number, year=current_year)

    return new_receipt
