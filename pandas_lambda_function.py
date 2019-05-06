import json
import pandas as pd


def lambda_handler(event, context):

    print((pd.DataFrame(data={'col1': [1, 2, 3, 4]})))
