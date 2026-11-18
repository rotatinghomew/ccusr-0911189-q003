def operating(windows, inventory):
    calendar = {(row['day'], row['cabinet']): row for row in windows}
    result = {}
    for row in inventory:
        key = row['day'], row['cabinet']
        if row['copies'] < 0 or key not in calendar:
            raise ValueError('库存快照缺少有效柜机日历')
        if calendar[key]['state'] == 'open':
            result[key + (row['item'],)] = (row['copies'], calendar[key]['request_log'])
    return result
