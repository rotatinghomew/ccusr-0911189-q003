from .loans import lent
from .opening import operating
from .transport import board


def report(data):
    calendar = operating(data['windows'], data['inventory'])
    return {'open_item_days':len(calendar), 'loan_totals':lent(data['requests']),
            'transport':board(data['shipping'],data['transfers'])}
