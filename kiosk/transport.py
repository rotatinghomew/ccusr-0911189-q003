def board(routes, transfers):
    if any(row['arrive'] < row['depart'] for row in routes):
        raise ValueError('到达日不能早于出发日')
    return {'routes': sorted(row['id'] for row in routes),
            'committed': sorted(row['id'] for row in transfers if row['status'] == 'confirmed')}
