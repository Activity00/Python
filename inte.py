from intervals import IntInterval

BLOCK_RANGE_TABLE_NAME = {
    IntInterval.closed(1, 5): 'talbe1',
    IntInterval.closed(5, 10): 'table2'
}

BLOCK_RANGES = BLOCK_RANGE_TABLE_NAME.keys()

for interval in BLOCK_RANGES:
    if 2 in interval:
        print(interval)
        print(interval.lower, interval.upper)
        print(BLOCK_RANGE_TABLE_NAME[interval])
