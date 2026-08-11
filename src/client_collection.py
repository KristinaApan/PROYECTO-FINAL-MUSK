from src.client import Client


class ClientCollection:
    """Colección de objetos Client."""

    def __init__(self, clients: list[Client]):
        """Inicializa la colección con una lista de clientes."""
        self.clients = clients

    def get_client_by_id(self, client_id):
        """Devuelve el cliente que coincide con el identificador."""
        for client in self.clients:
            if client.client_id == client_id:
                return client

        raise ValueError(f"Client with id {client_id} not found")

    def clients_by_country(self, country):
        """Devuelve los clientes pertenecientes a un país."""
        return [
            client
            for client in self.clients
            if client.country == country
        ]

       