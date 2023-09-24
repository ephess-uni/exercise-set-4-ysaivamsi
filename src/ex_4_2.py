""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    format = '%Y-%m-%dT%H:%M:%S'

    date_ = datetime.strptime(datestr, format)

    return date_


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')