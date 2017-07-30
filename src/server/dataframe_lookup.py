import pandas
import webcolors as wc
import numpy as np

colorList = [
             [255, 255, 255],
             [128, 128, 128],
             [255, 0, 0],
             [192, 192, 192],
             [0, 0, 0],
             [0, 0, 255],
             [165, 42, 42],
             [255, 255, 0],
             [0, 128, 0],
             [255, 165, 0],
             [255, 215, 0],
             [128, 0, 128],
             [128, 0, 0],
             [210, 180, 140],
             [0, 128, 128]
            ]

def findRGBValues(color):
    result = pandas.read_csv('colors.csv', index_col = 0)

    try:
        red = np.asscalar(result.loc[color]['RED'])
        green = np.asscalar(result.loc[color]['GREEN'])
        blue = np.asscalar(result.loc[color]['BLUE'])
        print('Name: ' + color + ' - [' + str(red) + ', ' + str(green) + ', ' + str(blue) + ']')
        return {'red': red, 'green': green, 'blue': blue}
    except KeyError as e:
        print(e)

def getRGBList():
  result = pandas.read_csv('..\..\extras\colors3.csv', index_col=0, encoding='utf-8')

  resultList = []

  for i, row in result.iterrows():
    tempObject = {}
    red = int(row['RED'])
    green = int(row['GREEN'])
    blue = int(row['BLUE'])
    tempList = colorList[calculateDifference(red, green, blue)]
    tempObject['simplifiedColor'] = wc.rgb_to_name((tempList[0], tempList[1], tempList[2]))
    tempObject['name'] = str(i)
    tempObject['red'] = red
    tempObject['green'] = green
    tempObject['blue'] = blue
    resultList.append(tempObject)

  return resultList

def calculateDifference(red, green, blue):
  bestindex = 0
  currentdiff = abs(colorList[0][0] - red) + abs(colorList[0][1] - green) + abs(colorList[0][2] - blue)
  bestdiff = abs(colorList[0][0] - red) + abs(colorList[0][1] - green) + abs(colorList[0][2] - blue)
  for i in range(1, len(colorList)):
    currentdiff = abs(colorList[i][0] - red) + abs(colorList[i][1] - green) + abs(colorList[i][2] - blue)
    if currentdiff < bestdiff:
      bestindex = i
      bestdiff = currentdiff

  return bestindex

getRGBList()




