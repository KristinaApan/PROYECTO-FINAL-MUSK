from src.sale import Sale


class SalesCollection:
    def __init__(self, sales: list[Sale]):
        self.sales = sales

    def sales_by_client(self, client_id: int) -> list[Sale]:
        return [
            sale
            for sale in self.sales
            if sale.client_id == client_id
        ]

    def total_amount_by_client(self, client_id: int) -> float:
        return sum(
            sale.amount
            for sale in self.sales
            if sale.client_id == client_id
        )

    def total_amount_by_category(self, category: str) -> float:
        return sum(
            sale.amount
            for sale in self.sales
            if sale.category == category
        )

    def average_sale_by_client(self, client_id: int) -> float:
        client_sales = self.sales_by_client(client_id)

        if not client_sales:
            return 0.0

        return (
            self.total_amount_by_client(client_id)
            / len(client_sales)
        )