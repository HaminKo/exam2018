def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    names_list = []

    name_file = open(file_name, 'r')

    for name in name_file:
        names_list.append(name.split(','))
    
    return names_list


def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_path = './babynames/yob' + str(year) +'.txt'
    data = process_file(file_path)

    birth_total = 0

    for name in data:
        birth_total += int(name[2])

    return birth_total


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    file_path = './babynames/yob' + str(year) +'.txt'
    data = process_file(file_path)
    babies = 0

    for info in data:
        if info[0] == name and info[1] == gender:
            babies = info[2]
    
    return int(babies)/total_births(year)

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    years = range(1880, 2011)
    highest_year = 0
    highest_propotion = 0

    for year in years:
        current_proportion = proportion(name, gender, year)
        if current_proportion > highest_propotion:
            highest_year = year
            highest_propotion = current_proportion
    
    return highest_year


def main():
    # names_1999 = process_file('./babynames/yob1880.txt')
    # print(total_births(1981))
    # print(proportion('Sarah', 'F', 1981))
    print(highest_year('Sarah', 'F'))



if __name__ == '__main__':
    main()
