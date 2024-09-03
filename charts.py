import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['a', 'b', 'c']
    values = [10, 20, 30]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
