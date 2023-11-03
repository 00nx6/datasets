def file_reader_module(file_name):
    with open(file_name, encoding='utf-8') as file:
        keys = file.readline().strip().lower().split(';')
        lines = [line.strip().split(';') for line in file]
        return [dict(zip(keys, line)) for line in lines]  # noqa: B905

def get_species(catalog):
    species = ['All']
    for entry in catalog:
        if entry['kind'] not in species:
            species.append(entry['kind'])
    return species

def filter_catalog(filters, catalog):
    # for entry in catalog:
    #     print((filters[1] == '' or filters[1] in entry['pet name']) and (filters[0] == 'All' or filters[0] == entry['kind']), entry['kind'])
    return [entry for entry in catalog if
                        (filters[1] == '' or filters[1] in entry['pet name']) and  # noqa: PLC1901
                        (filters[0] == 'All' or filters[0] == entry['kind'])]

def zip_dates_prices(catalog):
    date_collection = {}
    for entry in catalog:
        if entry['date'] not in date_collection:
            date_collection[entry['date']] = int(entry['price'])
        else:
            date_collection[entry['date']] += int(entry['price'])
    
    return date_collection


def calculate_stats(catalog, kind):
    total_age, max_age, total_price, counter = 0, 0, 0, 0
    for entry in catalog:
        if entry['kind'] == kind or kind == 'All':
            counter += 1
            total_age += int(entry['age'])
            total_price += int(entry['price'])
            if int(entry['age']) > max_age:
                max_age = int(entry['age'])

    if counter > 0:  # noqa: RET503
        return round(total_age / counter, 2), round(total_price / counter, 2), max_age

