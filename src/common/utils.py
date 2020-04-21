"""Provide some widely useful utilities."""

import pandas as pd

def read_credentials(file_path):
    """
    This method reads the credentials of the sites to be scraped from an excel.

    Input:

    file_path = '/stackoverflow/src/input/credentials.xlsx'

    Output:

    credenciais_dict = {'user':
                                    {
                                     'user': 'xxxxx',
                                     },
                        'password':
                                    {
                                    'user': 'XXXXXX',
                                    }
                            }

    The output is a tuple: (status, config_dict)

    How to Use:

    import common.utils as ldc

    status, credentials_dict = ldc.read_credentials(file_path)

    """

    try:
        credentials_file = pd.read_excel(file_path, dtype=str)
        credentials_file.set_index('portal', inplace=True)
        credentials_dict = credentials_file.to_dict()
        status = 1

    except Exception as e:
        credentials_dict = e
        status = 0

    return (status, credentials_dict)
