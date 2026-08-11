from src.client import Client


class ClientCollection: 
    def __init__(self, clients: list[Client]):
        self.clients = clients 


    def get_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

        raise ValueError(f"Client with id {client_id} not found")  

    def clients_by_country(self, country):
        return [
            client 
            for client in self.clients
            if client.country == country
        ]  

       