from file_reader_module import file_reader_module

def get_species(catalog):
    species = ['All']
    for entry in catalog:
        if entry['kind'] not in species:
            species.append(entry['kind'])
    return species

def filter_catalog(filters, catalog):
    return [entry for entry in catalog if
                        (filters[1] == '' or filters[1] in entry['pet name']) and  # noqa: PLC1901
                        (filters[0] == 'All' or filters[0] == entry['kind'])]
    
def print_stats(avg_age, avg_price, max_age, kind):
    print(f'{kind}: Average age: {avg_age} - Maximum age: {max_age} - Average procedure price: {avg_price}')

def print_dates(date_collection):
    # print first 7, and last 2
    print('\n[Daily totals]')
    for (date) in list(date_collection)[:7]:
        print(f' {date}: {date_collection[date]} euros')
    print('...')
    for (date) in list(date_collection)[-2:]:
        print(f'{date}: {date_collection[date]} euros')
        
def zip_dates_prices(catalog):
    date_collection = {}
    for entry in catalog:
        if entry['date'] not in date_collection:
            date_collection[entry['date']] = int(entry['price'])
        else:
            date_collection[entry['date']] += int(entry['price'])
    print_dates(date_collection=date_collection)

def calculate_stats(catalog, kind):
    total_age, max_age, total_price, counter = 0, 0, 0, 0
    for entry in catalog:
        if entry['kind'] == kind or kind == 'All':
            counter += 1
            total_age += int(entry['age'])
            total_price += int(entry['price'])
            if int(entry['age']) > max_age:
                max_age = int(entry['age'])

    if counter > 0:
        print_stats(round(total_age / counter, 2), round(total_price / counter, 2), max_age, kind)
    else:
        print(f'No data for species: {kind}')

def main():
    print('*** Little Paws Veterinary Administration ***')
    while True:
        file_name = input('Enter the name of the  file containing your procedure history (type \'exit\' to quit the application): ')
        try:
            catalog = file_reader_module(file_name)
        except FileNotFoundError:
            print('ERROR: Unable to open file')
        else:
            print(len(catalog), 'procedures.')
            species = get_species(catalog=catalog)
            break
    
    for kind in species:
        calculate_stats(catalog=catalog, kind=kind)
    
    zip_dates_prices(catalog=catalog)


if __name__ == "__main__":
    main()
