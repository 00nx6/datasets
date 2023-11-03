def print_stats(kind_stats, kind):
    try:
        print(f'{kind}: Average age: {kind_stats[0]} - Maximum age: {kind_stats[2]} - Average procedure price: {kind_stats[1]}')
    except TypeError:
        return
        
def print_dates(date_collection):
    # print first 7, and last 2
    print('\n[Daily totals]')
    for (date) in list(date_collection)[:7]:
        print(f' {date}: {date_collection[date]} euros')
    print('...')
    for (date) in list(date_collection)[-2:]:
        print(f'{date}: {date_collection[date]} euros')
