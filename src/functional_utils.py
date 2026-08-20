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


def average_sale_by_client(sales, client_id):
    """Calculate the average sale amount for a client."""
    total = total_amount_by_client(sales, client_id)
    count = count_sales_by_client(sales, client_id)

    if count == 0:
        return 0

    return round(total / count, 2)


def filter_clients_by_country(clients, country):
    """Filter clients by country."""
    return list(filter(lambda c: c.country == country, clients))


def top_client_by_country(clients, sales, country):
    """Find the client with the highest total spending in a country."""
    country_clients = filter_clients_by_country(clients, country)

    return max(
        country_clients,
        key=lambda c: total_amount_by_client(sales, c.client_id)
    )


def total_amount_by_category(sales, category):
    """Calculate the total amount of sales in a category."""
    category_sales = filter_sales_by_category(sales, category)

    return reduce(
        lambda total, sale: total + sale.amount,
        category_sales,
        0
    )


def filter_high_spending_clients(clients, sales, threshold):
    """Filter clients whose total spending is above a threshold."""
    return list(
        filter(
            lambda c: total_amount_by_client(sales, c.client_id) > threshold,
            clients
        )
    )


def top_client_by_category(clients, sales, category):
    """Find the client with the most sales in a specific category."""
    category_sales = filter_sales_by_category(sales, category)

    return max(
        clients,
        key=lambda client: count_sales_by_client(
            category_sales,
            client.client_id
        )
    )


def total_sales_by_month(sales):
    """Calculate total sales grouped by month."""
    return reduce(
        lambda totals, sale: {
            **totals,
            sale.date[:7]: totals.get(sale.date[:7], 0) + sale.amount
        },
        sales,
        {}
    )
