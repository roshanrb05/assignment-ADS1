import matplotlib.pyplot as plt
import pandas as pd


def read(excel_file):
    """
    This fucntion can be used for reading the data from an excel file, and 
    it returns two dataframes, the original and transposed data.
    """
    file = pd.read_excel(excel_file)
    file = file.drop(['Series Name', 'Series Code','Country Code'], axis=1).dropna()
    file_transpose = file.transpose()
    return file, file_transpose


def bar_plot(file, head, img_name, ylabel):
    """
    This function will return a bargraph.
    """

    plt.figure(figsize=(17, 18))
    years = ["2012 [YR2012]","2014 [YR2014]", "2016 [YR2016]", "2018 [YR2018]"]
    file.plot(x="Country Name", y=years, kind='bar')
    plt.title(head, fontsize=12)
    plt.xlabel('Countries', fontsize=10)
    plt.xticks(fontsize=10, rotation=90)
    plt.ylabel(ylabel, fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(frameon=False, fontsize=10)
    plt.savefig(img_name, bbox_inches="tight", dpi=200)
    plt.show()


def line_plot(file, head, img_name, ylabel):
    """
    This function will return a lineplot.
    """
    plt.figure(figsize=(17, 18))
    years = ["2012 [YR2012]", "2014 [YR2014]", "2016 [YR2016]","2018 [YR2018]"]
    file.plot(x="Country Name", y=years, kind='line')
    plt.title(head, fontsize=12)
    plt.xlabel('Countries', fontsize=10)
    plt.xticks(range(0, len(file.index)),file["Country Name"], rotation=90)
    plt.ylabel(ylabel, fontsize=5)
    plt.yticks(fontsize=10)
    plt.legend(frameon=False, fontsize=10)
    plt.savefig(img_name, bbox_inches="tight", dpi=200)
    plt.show()


# Reading the excel files
population, population_trans = read("C:/Users/babur/OneDrive/ADS1 Assignment/Total Population.xlsx")
co2, co2_trans = read("C:/Users/babur/OneDrive/ADS1 Assignment/CO2 Emission.xlsx")
poverty, poverty_trans = read("C:/Users/babur/OneDrive/ADS1 Assignment/Poverty headcount ratio.xlsx")
urban, urban_trans = read("C:/Users/babur/OneDrive/ADS1 Assignment/Urban population.xlsx")

#Plotting the bar graph
bar_plot(population, "Total population","population Bargraph.png", "world")
bar_plot(co2, "CO2 emission","CO2 emission Bargraph.png", "metric tonnes per capita")

#Plotting the line graph
line_plot(poverty, "Poverty headcount ratio","poverty Linegraph.png", "percentage of population")
line_plot(urban, "Urban population","Urban population Linegraph.png", "percentage of pop")
