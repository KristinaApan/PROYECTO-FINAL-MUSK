import json

import pandas as pd

from src.client import Client
from src.sale import Sale
from src.functional_utils import (
    total_amount_by_client,
    count_sales_by_client,
    average_sale_by_client,
    top_client_by_country,
    filter_high_spending_clients,
    top_client_by_category,
    
)


def load_clients(path):
    """Load clients from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Client(**client) for client in data]


def load_sales(path):
    """Load sales from a CSV file into a DataFrame."""
    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(df["date"])

    return df


def clients_to_dataframe(clients):
    """Convert clients to a Pandas DataFrame."""
    return pd.DataFrame([client.to_dict() for client in clients])


def merge_clients_sales(clients_df, sales_df):
    """Merge client and sales data."""
    return clients_df.merge(
        sales_df,
        on="client_id",
        how="left"
    )


def add_month_column(df):
    """Add a year-month period column to sales data."""
    result = df.copy()
    result["month"] = result["date"].dt.to_period("M")
    return result


def monthly_sales(merged_df):
    """Calculate total sales grouped by month."""
    return ( 
        merged_df
        .groupby("month")["amount"]
        .sum()
        .rename(lambda month: str(month))
        .to_dict()
    )


def sales_by_category(sales_df):
    """Calculate total sales grouped by category."""
    return (
        sales_df
        .groupby("category")["amount"]
        .sum()
        .round(2)
        .to_dict()
    )


def sales_to_objects(sales_df):
    """Convert a sales DataFrame to a list of Sale objects."""
    return [
        Sale(
            sale_id=row.sale_id,
            client_id=row.client_id,
            product=row.product,
            category=row.category,
            amount=row.amount,
            date=row.date,
        )
        for row in sales_df.itertuples(index=False)
    ]


def generate_report():
    """Generate the complete sales analysis report."""
    clients = load_clients("data/clients.json")
    sales_df = load_sales("data/sales.csv")
    sales = sales_to_objects(sales_df)
    
    summary = {
        "total_clients": len(clients),
        "total_sales": len(sales_df),
        "total_revenue": float(round(sales_df["amount"].sum(), 2)),
        
    }

    client_reports = [
        {
            "client_id": client.client_id,
            "name": client.name,
            "total_spent": total_amount_by_client(
                sales, client.client_id
            ),
            "sale_count": count_sales_by_client(
                sales, client.client_id
            ),
            "average_sale": average_sale_by_client(
                sales, client.client_id
            ),
        }
        for client in clients
    ]

    countries = [client.country for client in clients]

    top_clients = {
        country: top_client_by_country(clients, sales, country).name
        for country in countries
    }

    high_spenders = [
        client.name
        for client in filter_high_spending_clients(
            clients, sales, 500
        )
    ]

    top_electronics_client = top_client_by_category(
        clients,
        sales,
        "Electronics",
    ).name

    clients_df = clients_to_dataframe(clients)
    merged = merge_clients_sales(clients_df, sales_df)
    merged_with_month = add_month_column(merged)

    category_totals = sales_by_category(sales_df)
    monthly_totals = monthly_sales(merged_with_month)

    return {
       "summary": summary,
       "clients": client_reports,
       "top_client_by_country": top_clients,
       "sales_by_category": category_totals,
       "top_electronics_client": top_electronics_client,
       "high_spending_clients": high_spenders,
       "monthly_sales": monthly_totals,
}


if __name__ == "__main__":
    report = generate_report()

    with open("final_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    

  