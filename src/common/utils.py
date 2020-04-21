"""Método leitura de arquivos de configuração."""

import pandas as pd

def read_credentials_file(file_path):
    """
    Esse método faz a leitura das credenciais dos sites que se deseja fazer o scraping, a partir de um excel.

    Input:

    file_path = '/gr_decio/src/input/credenciais/credenciais.xlsx'

    Output:

    credenciais_dict = {'usuario':
                                    {
                                     'Beira Rio': '00000',
                                     'Beira Rio (Empresa 46)': '00000',
                                     'Urbanos': '0000',
                                     'Urbanos Posto Alto (Empresa 01)': '00000'
                                     },
                        'senha':
                                    {
                                    'Beira Rio': 'XXXX',
                                    'Beira Rio (Empresa 46)': 'XXXX',
                                    'Urbanos': 'XXXX',
                                    'Urbanos Posto Alto (Empresa 01)': 'XXXX'
                                    }
                            }

    O Output é uma tupla: (status, config_dict)

    Como usar:

    import common.utils as ldc

    status, credenciais_dict = ldc.read_credentials_file(file_path)

    """

    try:
        credentials_file = pd.read_excel(
                                         file_path,
                                         dtype = str
                                         )
        credentials_df = credentials_file[['base', 'usuario', 'senha']]
        credentials_df.drop_duplicates(
                                         subset = ['base', 'usuario', 'senha'],
                                         inplace = True
                                         )

        status = 1

    except Exception as e:
        credentials_df = e
        status = 0

    return (status, credentials_df)
