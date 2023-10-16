from models import Order
from typing import List


def process_orders(orders: List[Order], criterion: str) -> float:
    total = 0
    all = False

    if criterion == 'all':
        all = True

    for order in orders:
        if all or order.status == criterion:
            total += order.price * order.quantity
    return total

