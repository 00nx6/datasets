import matplotlib.pyplot as plt; plt.rcdefaults()  # noqa: E702
import numpy as np

def draw_barchart(dates, output='my_plot.jpg'):
    objects = tuple(dates.keys())
    performance = list(dates.values())
    y_pos = np.arange(len(objects))
    
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=90)
    plt.ylabel('Usage')
    plt.title('Programming language usage')
    
    plt.savefig(output)
    plt.show()
