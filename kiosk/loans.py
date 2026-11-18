from collections import Counter


def lent(rows):
    tickets = {}
    for row in rows:
        facts = row['day'], row['cabinet'], row['requested'], row['loaned']
        key = row['ticket']
        if key in tickets and tickets[key] != facts:
            raise ValueError('同一请求票号的结果相互冲突')
        tickets[key] = facts
    return dict(Counter(f'{cabinet}/{item}' for _, cabinet, _, item in tickets.values() if item))
