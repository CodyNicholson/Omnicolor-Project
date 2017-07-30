import pandas

def findRGBValues(color):
    result = pandas.read_csv('..\colors2.csv', index_col = 0)
    print(result)

    try:
        print('Name: ' + color)
        print('Red: ' + result.loc[color]['RED'].astype(str))
        print('Green: ' + result.loc[color]['GREEN'].astype(str))
        print('Blue: ' + result.loc[color]['BLUE'].astype(str))
        red = result.loc[color]['RED'].astype(int)
        green = result.loc[color]['GREEN'].astype(int)
        blue = result.loc[color]['BLUE'].astype(int)
        answer = [red, green, blue]
        print(answer)
    except KeyError as e:
        print(e)

