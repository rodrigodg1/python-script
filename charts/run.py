import matplotlib.pyplot as plt



def bar_chart():

    categorias = []
    valores = []

    f = open('data_bar_chart.txt','r')
    for row in f:
        row = row.split(', ')
        categorias.append(row[0])
        valores.append(int(row[1]))

    plt.bar(categorias, valores, color = 'gray', label = 'File Data')

    plt.xlabel('Categorias', fontsize = 12)
    plt.ylabel('Valores', fontsize = 12)

    plt.title('Categorias', fontsize = 20)
    plt.legend()
    plt.show()



def line_chart():

    #line chart
    x = []
    y = []
    for line in open('data_line_chart.txt', 'r'):
        lines = [i for i in line.split(',')]
        x.append(lines[0]) #eixo x
        y.append(int(lines[1]))
        
    plt.title("Students Marks")
    plt.xlabel('IDs')
    plt.ylabel('Ages')
    plt.yticks(y)
    plt.plot(x, y, marker = 'o', c = 'g')
    
    plt.show()


def scatter_plot():
    x = []
    y = []
    for line in open('data_scatter_plot.csv', 'r'):
        lines = [i for i in line.split(',')]
        x.append(int(lines[0])) #eixo x
        y.append(int(lines[1]))


    plt.title("Students Marks")
    plt.xlabel('IDs')
    plt.ylabel('Ages')
    plt.yticks(y)

    plt.scatter(x, y)
    plt.show()


#check_all_data_files()

while True:
    op = input(
    '''
    1 - Bar Chart
    2 - Line Chart
    3 - Scatter Plot 
    > ''')

    if op == "1":
        try:
            bar_chart()
        except Exception as e:
            print(e)
            print("\n Check the data file. Most be in format = x, y")
    elif op == "2":
        try:
            line_chart()
        except Exception as e:
            print(e)
            print("\n Check the data file. Most be in format = x, y")
    elif op == "3":
        try:
            scatter_plot()
        except Exception as e:
            print(e)
            print("\n Check the data file. Most be in format = x, y")