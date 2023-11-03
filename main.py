import file_reader_module as frm
import print_functions as pf
import menu as nav
from draw_barchart import draw_barchart

def main():
    print('*** Little Paws Veterinary Administration ***')
    while True:
        file_name = input('Enter the name of the  file containing your procedure history (type \'exit\' to quit the application): ')
        try:
            catalog = frm.file_reader_module(file_name)
        except FileNotFoundError:
            print('ERROR: Unable to open file')
        else:
            print(len(catalog), 'procedures.')
            species = frm.get_species(catalog=catalog)
            break
    
    filtered_catalog = None
    
    while True:
        base_catalog = catalog if filtered_catalog is None else filtered_catalog
        date_collection = frm.zip_dates_prices(catalog=base_catalog)
        usr_nav = nav.menu()
        match usr_nav:
            case 1:
                for kind in species:
                    kind_stats = frm.calculate_stats(catalog=catalog, kind=kind)
                    pf.print_stats(kind_stats=kind_stats, kind=kind)
                pf.print_dates(date_collection=date_collection)

            case 2:
                filters = nav.get_filter()
                filtered_catalog = frm.filter_catalog(catalog=base_catalog, filters=filters)
                
                for kind in species:
                    kind_stats = frm.calculate_stats(catalog=filtered_catalog, kind=kind) if kind != 'All' else frm.calculate_stats(catalog=catalog, kind=kind)
                    pf.print_stats(kind_stats=kind_stats, kind=kind)
                    
            case 3:
                filters = ['All', '']
                filtered_catalog = None
                
            case 4:
                draw_barchart(dates=date_collection)

            case _:
                print('ERROR: Not given option')


if __name__ == "__main__":
    main()
