import random
from typing import List, Dict
from .pipeline_utils import fake

def generate_fact_transaction(
    num_records: int,
    accounts: List[Dict[str, any]],
    dates: List[Dict[str, any]],
    transaction_types: List[Dict[str, any]],
    channels: List[Dict[str, any]],
    locations: List[Dict[str, any]],
    currencies: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    transactions = []
    for _ in range(num_records):
        transactions.append({
            'transaction_id': fake.unique.random_int(min=1, max=10000000),
            'date_id': random.choice(dates)['date_id'],
            'transaction_type_id': random.choice(transaction_types)['transaction_type_id'],
            'account_id': random.choice(accounts)['account_id'],
            'channel_id': random.choice(channels)['channel_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'transaction_amount': round(random.uniform(1.00, 10000), 2),
            'transaction_status': random.choice(['Pending', 'Completed', 'Failed'])
        })
    return transactions


def generate_fact_investment(
    num_records: int,
    accounts: List[Dict[str, any]],
    dates: List[Dict[str, any]],
    investment_types: List[Dict[str, any]],
    locations: List[Dict[str, any]],
    currencies: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    investments = []
    for _ in range(num_records):
        investments.append({
            'investment_id': fake.unique.random_int(min=1, max=10000000),
            'date_id': random.choice(dates)['date_id'],
            'investment_type_id': random.choice(investment_types)['investment_type_id'],
            'account_id': random.choice(accounts)['account_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'investment_amount': round(random.uniform(1000.00, 1000000.00), 2),
            'investment_return': round(random.uniform(-5000, 15000), 2)
        })
    return investments


def generate_fact_loans(
    num_records: int,
    accounts: List[Dict[str, any]],
    dates: List[Dict[str, any]],
    loans: List[Dict[str, any]],
    locations: List[Dict[str, any]],
    currencies: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    fact_loans = []
    for _ in range(num_records):
        fact_loans.append({
            'loan_fact_id': fake.unique.random_int(min=1, max=10000000),
            'date_id': random.choice(dates)['date_id'],
            'loan_id': random.choice(loans)['loan_id'],
            'account_id': random.choice(accounts)['account_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'loan_amount': round(random.uniform(5000, 500000), 2),
            'loan_status': random.choice(['Pending', 'Approved', 'Rejected'])
        })
    return fact_loans


def generate_fact_customer_interactions(
    num_records: int,
    customers: List[Dict[str, any]],
    dates: List[Dict[str, any]],
    channels: List[Dict[str, any]],
    locations: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    interactions = []
    for _ in range(num_records):
        interactions.append({
            'interaction_id': fake.unique.random_int(min=1, max=10000000),
            'date_id': random.choice(dates)['date_id'],
            'customer_id': random.choice(customers)['customer_id'],
            'channel_id': random.choice(channels)['channel_id'],
            'location_id': random.choice(locations)['location_id'],
            'interaction_type': random.choice(['Call', 'Email', 'Chat', 'In-Person']),
            'interaction_rating': random.randint(1, 5),
        })
    return interactions


def generate_fact_daily_balances(
    num_records: int,
    accounts: List[Dict[str, any]],
    dates: List[Dict[str, any]],
    currencies: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    daily_balances = []
    for _ in range(num_records):
        opening = round(random.uniform(0, 1000000), 2)
        closing = round(random.uniform(0, 1000000), 2)
        average = round((opening + closing) / 2, 2)

        daily_balances.append({
            'balance_id': fake.unique.random_int(min=1, max=10000000),
            'date_id': random.choice(dates)['date_id'],
            'account_id': random.choice(accounts)['account_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'opening_balance': opening,
            'closing_balance': closing,
            'average_balance': average,
        })
    return daily_balances
