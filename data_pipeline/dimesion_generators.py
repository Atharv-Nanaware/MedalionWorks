import random
from datetime import datetime, timedelta
from typing import List, Dict
from pipeline_utils import fake, id_generator

# Initialize ID generators for different dimensions
customer_id_gen = id_generator()
date_id_gen = id_generator()
channel_id_gen = id_generator()
account_id_gen = id_generator()
transaction_type_id_gen = id_generator()
location_id_gen = id_generator()
currency_id_gen = id_generator()
investment_type_id_gen = id_generator()
loan_id_gen = id_generator()

def generate_dim_customer(num_records: int = 1000) -> List[Dict[str, any]]:

    customers = []
    for _ in range(num_records):
        customers.append({
            'customer_id': next(customer_id_gen),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'address': fake.address().replace('\n', ', '),
            'city': fake.city(),
            'state': fake.state(),
            'postal_code': fake.postalcode(),
            'phone_number': fake.phone_number()
        })
    return customers


def generate_dim_date(start_year: int = 2020, end_year: int = 2024) -> List[Dict[str, any]]:

    date_list = []
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = timedelta(days=1)

    num_days = (end_date - start_date).days + 1
    for _ in range(num_days):
        # Use the ID generator to assign a unique date_id
        current_date = start_date.strftime('%Y-%m-%d')
        date_list.append({
            'date_id': next(date_id_gen),
            'date': current_date,
            'day': start_date.day,
            'month': start_date.month,
            'year': start_date.year,
            'weekday': start_date.weekday() + 1
        })
        start_date += delta

    return date_list


def generate_dim_channel() -> List[Dict[str, any]]:

    channel_names = ['Online', 'Mobile App', 'In-Store', 'ATM', 'Telephone']
    channels = []
    for name in channel_names:
        channels.append({
            'channel_id': next(channel_id_gen),
            'channel_name': name
        })
    return channels


def generate_dim_account(num_records: int = 100, customer_ids: List[int] = None) -> List[Dict[str, any]]:

    if customer_ids is None:
        customer_ids = []

    accounts = []
    for _ in range(num_records):
        accounts.append({
            'account_id': next(account_id_gen),
            'customer_id': random.choice(customer_ids),
            'account_number': fake.unique.random_int(min=1000000000, max=9999999999),
            'account_type': random.choice(['Savings', 'Checking', 'Investment']),
            'account_balance': round(random.uniform(0, 1000000), 2),
            'credit_score': random.randint(300, 850)
        })
    return accounts


def generate_dim_transaction_type() -> List[Dict[str, any]]:

    transaction_types = [
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Deposit'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Withdrawal'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Transfer'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Payment'
        },
    ]
    return transaction_types


def generate_dim_location(num_records: int = 50) -> List[Dict[str, any]]:

    locations = []
    for _ in range(num_records):
        locations.append({
            'location_id': next(location_id_gen),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'postal_code': fake.postcode()
        })
    return locations


def generate_dim_currency() -> List[Dict[str, any]]:

    return [
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'USD',
            'currency_name': 'US Dollar'
        },
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'EUR',
            'currency_name': 'Euro'
        },
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'JPY',
            'currency_name': 'Japanese Yen'
        },
    ]


def generate_dim_investment_type(num_records: int = 5) -> List[Dict[str, any]]:

    investment_types = []
    for _ in range(num_records):
        investment_types.append({
            'investment_type_id': next(investment_type_id_gen),
            'investment_type_name': fake.word().capitalize() + 'Investment'
        })
    return investment_types


def generate_dim_loan(num_records: int = 50) -> List[Dict[str, any]]:

    loans = []
    for _ in range(num_records):
        loans.append({
            'loan_id': next(loan_id_gen),
            'loan_type': random.choice(['Mortgage', 'Personal', 'Auto', 'Student']),
            'loan_amount': round(random.uniform(5000, 500000), 2),
            'interest_rate': round(random.uniform(1.5, 10.0), 2)
        })
    return loans
