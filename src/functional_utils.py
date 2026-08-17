from functools import reduce


def filter_sales_by_category(sales, category):
    """Filter sales by category."""
    return list(filter(lambda s: s.category == category, sales))


def filter_sales_by_client(sales, client_id):
    """Filter sales by client ID."""
    return list(filter(lambda s: s.client_id == client_id, sales))