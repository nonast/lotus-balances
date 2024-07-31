"""
Simple script to extract the necessary data for new tokenomics from the snapshot json.
"""

import json
import pandas as pd


def print_first(df):
    print(df.iloc[0])


def print_first_not_null(df, key: str):
    print(df[df[key].notnull()].iloc[0])


def print_first_with_exact_value(df, key: str, value: str):
    print(df[df[key] == value].iloc[0])


if __name__ == '__main__':
    with open("state_epoch_79_ver_33217173.795d.json") as f:
        data = json.load(f)
        df = pd.DataFrame(data)

    # print_first_not_null(df, 'my_pledge')
    # print_first_with_exact_value(df, 'role', 'Validator')

    # We need to keep the following keys: account, role, balance, slow_wallet, my_pledge

    df = df[['account', 'role', 'balance', 'slow_wallet', 'my_pledge']]

    # export to csv
    df.to_csv('snapshot.csv', index=False)

