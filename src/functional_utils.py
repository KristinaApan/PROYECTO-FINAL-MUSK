from functools import reduce


def filter_sales_by_category(sales, category):
    """Filter sales by category."""
    return list(filter(lambda s: s.category == category, sales))


def filter_sales_by_client(sales, client_id):
    """Filter sales by client ID."""
    return list(filter(lambda s: s.client_id == client_id, sales))


def total_amount_by_client(sales, client_id):
    """Calculate the total amount spent by a client."""
    client_sales = filter_sales_by_client(sales, client_id)

    return reduce(
        lambda total, sale: total + sale.amount,
        client_sales,
        0
    )


def count_sales_by_client(sales, client_id):
    """Count the number of sales made by a client."""
    return len(filter_sales_by_client(sales, client_id))