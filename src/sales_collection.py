from src.sale import Sale


class SalesCollection:
    """Colección de objetos Sale con operaciones de consulta y cálculo."""

    def __init__(self, sales: list[Sale]):
        """Inicializa la colección con una lista de ventas."""
        self.sales = sales

    def sales_by_client(self, client_id: int) -> list[Sale]:
        """Devuelve todas las ventas asociadas a un cliente."""
        return [
            sale
            for sale in self.sales
            if sale.client_id == client_id
        ]

    def total_amount_by_client(self, client_id: int) -> float:
        """Devuelve el importe total de las ventas de un cliente."""
        return sum(
            sale.amount
            for sale in self.sales
            if sale.client_id == client_id
        )

    def total_amount_by_category(self, category: str) -> float:
        """Devuelve el importe total de las ventas de una categoría."""
        return sum(
            sale.amount
            for sale in self.sales
            if sale.category == category
        )

    def average_sale_by_client(self, client_id: int) -> float:
        """Devuelve el importe medio de las ventas de un cliente."""
        client_sales = self.sales_by_client(client_id)

        if not client_sales:
            return 0.0

        return (
            self.total_amount_by_client(client_id)
            / len(client_sales)
        )   