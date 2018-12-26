import re


def get_data():
    def get_el(line, need):
        el = line[need]
        return el

    def get_season(line):
        needed = int(header.index('season'))
        result = get_el(line, needed)
        season = re.findall(r'\d{4}\-\d{4}', result)
        season = season[0]
        season = season.replace("['", '').replace("']", '')
        return season

    def get_home(line):
        needed = int(header.index('home_team'))
        home = get_el(line, needed)
        return home

    def get_away(line):
        needed = header.index('away_team')
        away = get_el(line, needed)
        return away

    dct = {}
    try:
        with open('results.csv', mode='r') as file:
            header = file.readline()
            header = header.replace(' ', '').rstrip().lower().split(',')

            line_number = 0
            for line in file:
                line = line.strip().rstrip().split(',')
                line_number += 1

                season = str(get_season(line))
                if season not in dct:
                    dct[season] = {}
                home_team = str(get_home(line))
                if home_team not in dct[season]:
                    dct[season][home_team] = {}
                away_team = str(get_away(line))
                away_list = list(dct[season][home_team])
                away_list.append(away_team)
                dct[season][home_team] = away_list

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    except ValueError as ve:
        print("Value error {0} in line {1}".format(ve, line_number))

    return dct


print(get_data())
