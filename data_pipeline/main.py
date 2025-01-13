from data_pipeline.dimesion_generators import (
    generate_dim_customer,
    generate_dim_date,
    generate_dim_channel,
    generate_dim_account,
    generate_dim_transaction_type,
    generate_dim_location,
    generate_dim_currency,
    generate_dim_investment_type,
    generate_dim_loan
)

from data_pipeline.fact_generators import (
    generate_fact_transaction,
    generate_fact_investment,
    generate_fact_loans,
    generate_fact_customer_interactions,
    generate_fact_daily_balances
)

from data_pipeline.writer import write_to_csv


def main():

    print("Generating dimension tables...")
    customers = generate_dim_customer(100)
    dates = generate_dim_date(2020, 2024)
    channels = generate_dim_channel()
    transaction_types = generate_dim_transaction_type()
    locations = generate_dim_location(50)
    currencies = generate_dim_currency()
    accounts = generate_dim_account(100, [c['customer_id'] for c in customers])
    investment_types = generate_dim_investment_type(5)
    loans = generate_dim_loan(50)

    # Write dimension data to CSV
    print("Writing dimension tables to CSV...")
    write_to_csv(customers, 'dim_customers.csv')
    write_to_csv(dates, 'dim_dates.csv')
    write_to_csv(channels, 'dim_channels.csv')
    write_to_csv(transaction_types, 'dim_transaction_types.csv')
    write_to_csv(locations, 'dim_locations.csv')
    write_to_csv(currencies, 'dim_currencies.csv')
    write_to_csv(accounts, 'dim_accounts.csv')
    write_to_csv(investment_types, 'dim_investment_types.csv')
    write_to_csv(loans, 'dim_loans.csv')

    print("Generating fact tables...")
    transactions = generate_fact_transaction(
        10000,
        accounts,
        dates,
        transaction_types,
        channels,
        locations,
        currencies
    )
    investments = generate_fact_investment(
        10000,
        accounts,
        dates,
        investment_types,
        locations,
        currencies
    )
    fact_loans = generate_fact_loans(
        10000,
        accounts,
        dates,
        loans,
        locations,
        currencies
    )
    interactions = generate_fact_customer_interactions(
        10000,
        customers,
        dates,
        channels,
        locations
    )
    daily_balances = generate_fact_daily_balances(
        10000,
        accounts,
        dates,
        currencies
    )


    print("Writing fact tables to CSV...")
    write_to_csv(transactions, 'fact_transactions.csv')
    write_to_csv(investments, 'fact_investments.csv')
    write_to_csv(fact_loans, 'fact_loans.csv')
    write_to_csv(interactions, 'fact_customer_interactions.csv')
    write_to_csv(daily_balances, 'fact_daily_balances.csv')


    # Add Upload to S3

if __name__ == "__main__":
    main()
