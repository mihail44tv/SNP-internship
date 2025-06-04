import datetime as dt


def date_in_future(integer):

    if isinstance(integer, int):
        result = dt.datetime.now() + dt.timedelta(days=integer)
    else:
        result = dt.datetime.now()

    return result.strftime('%d-%m-%Y %H:%M:%S')

