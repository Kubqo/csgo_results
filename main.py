import csv
import glob, os

maps = ['dust2', 'mirage', 'inferno', 'nuke']
dates = ['23.8.2023', '6.9.2023']

team1 = 'page-1_table-1.csv'
team2 = 'page-1_table-2.csv'
performance = {}


def setupPerformanceDict(performance, file_url):
  with open(file_url) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      performance[row[0]] = {"kills":  0, "assists": 0, "deaths": 0, 'score': 0, 'matches': 0}

def addToPerformanceDict(performance, file_url):
    with open(file_url) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        performance[row[0]] = {"kills":  performance[row[0]]["kills"] + int(row[len(row)-5]), 
                              "assists": performance[row[0]]["assists"] +  int(row[len(row)-4]), 
                              "deaths": performance[row[0]]["deaths"] + int(row[len(row)-3]), 
                              "score": performance[row[0]]["score"] + int(row[len(row)-1]), 
                              'matches': performance[row[0]]['matches'] + 1}

for folder in os.listdir("./"):
  if folder in maps:
    for day in os.listdir("./" + folder):
      path = "./" + folder + '/' + day + '/' 
      pngs = glob.glob(path +"/*.png")

      if len(pngs) == 0:
        for matchFolder in os.listdir(path):
          setupPerformanceDict(performance, path +  matchFolder + '/'+ team1)
          setupPerformanceDict(performance, path +  matchFolder + '/'+ team2)
      else:
          setupPerformanceDict(performance, path + team1)
          setupPerformanceDict(performance, path + team2)

for folder in os.listdir("./"):
  if folder in maps:
    for day in os.listdir("./" + folder):
      path = "./" + folder + '/' + day + '/' 
      pngs = glob.glob(path +"/*.png")

      if len(pngs) == 0:
        for matchFolder in os.listdir(path):
          addToPerformanceDict(performance, path + matchFolder + '/'+ team1)
          addToPerformanceDict(performance, path +  matchFolder + '/'+ team2)
      else:
        addToPerformanceDict(performance, path + team1)    
        addToPerformanceDict(performance, path + team2)


sorted_performance = {k: v for k, v in sorted(performance.items(), key=lambda item: item[1]['score'] / item[1]['matches'], reverse=True)}

for key in sorted_performance:
  print(key, sorted_performance[key])