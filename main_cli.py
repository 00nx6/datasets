import fire
import file_reader_module as frm
from draw_barchart import draw_barchart

def main(file_name, output='my_plot.jpg', name='', kind=''):
    try:
        catalog = frm.file_reader_module(file_name)
    except FileNotFoundError:
        return 'ERROR: Could not open file.'
    filters = [kind, name]
    filtered_catalog = frm.filter_catalog(catalog=catalog, filters=filters)
    date_collection = frm.zip_dates_prices(catalog=filtered_catalog)
    draw_barchart(dates=date_collection, output=output)

    return '\n >> Have a nice day Timothy!\n'

if __name__ == "__main__":
    fire.Fire(main)
