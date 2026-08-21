from functools import reduce


def filter_sales_by_category(sales, category):
    """Filtra las ventas por categoría."""
    return list(filter(lambda s: s.category == category, sales))


def filter_sales_by_client(sales, client_id):
    """Filtra las ventas por ID de cliente."""
    return list(filter(lambda s: s.client_id == client_id, sales))


def total_amount_by_client(sales, client_id):
    """Calcula el importe total gastado por un cliente."""
    client_sales = filter_sales_by_client(sales, client_id)

    return reduce(
        lambda total, sale: total + sale.amount,
        client_sales,
        0
    )


def count_sales_by_client(sales, client_id):
    """Cuenta el número de ventas realizadas por un cliente."""
    return len(filter_sales_by_client(sales, client_id))


def average_sale_by_client(sales, client_id):
    """Calcula el importe medio de las ventas de un cliente."""
    total = total_amount_by_client(sales, client_id)
    count = count_sales_by_client(sales, client_id)

    if count == 0:
        return 0

    return round(total / count, 2)


def filter_clients_by_country(clients, country):
    """Filtra los clientes por país."""
    return list(filter(lambda c: c.country == country, clients))


def top_client_by_country(clients, sales, country):
    """Encuentra el cliente con mayor gasto total de un país."""
    country_clients = filter_clients_by_country(clients, country)

    return max(
        country_clients,
        key=lambda c: total_amount_by_client(sales, c.client_id)
    )


def total_amount_by_category(sales, category):
    """Calcula el importe total de las ventas de una categoría."""
    category_sales = filter_sales_by_category(sales, category)

    return reduce(
        lambda total, sale: total + sale.amount,
        category_sales,
        0
    )


def filter_high_spending_clients(clients, sales, threshold):
    """Filtra los clientes cuyo gasto total supera un umbral."""
    return list(
        filter(
            lambda c: total_amount_by_client(sales, c.client_id) > threshold,
            clients
        )
    )


def top_client_by_category(clients, sales, category):
    """Encuentra el cliente con más ventas de una categoría específica."""
    category_sales = filter_sales_by_category(sales, category)

    return max(
        clients,
        key=lambda client: count_sales_by_client(
            category_sales,
            client.client_id
        )
    )


def total_sales_by_month(sales):
    """Calcula el total de ventas agrupadas por mes."""
    return reduce(
        lambda totals, sale: {
            **totals,
            sale.date[:7]: totals.get(sale.date[:7], 0) + sale.amount
        },
        sales,
        {}
    )
