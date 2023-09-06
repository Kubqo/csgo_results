import csv
import glob, os

maps = ['dust2', 'mirage', 'inferno', 'nuke']
dates = ['23.8.2023']

team1 = 'page-1_table-1.csv'
team2 = 'page-1_table-2.csv'

folders = [i+ '_' + j for i in maps for j in dates]

performance = {}


def setupPerformanceDict(performance, csv_file):
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    performance[row[0]] = {"kills":  0, "assists": 0, "deaths": 0, 'matches': 0}

def addToPerformanceDict(performance, csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      performance[row[0]] = {"kills":  performance[row[0]]["kills"] + int(row[len(row)-5]), 
                             "assists": performance[row[0]]["assists"] +  int(row[len(row)-4]), 
                             "deaths": performance[row[0]]["deaths"] + int(row[len(row)-3]), 
                             'matches': performance[row[0]]['matches'] + 1}

for folder in os.listdir("./"):
    pngs = glob.glob("./" + folder +"/*.png")

    if len(pngs) == 0 and folder in folders:
        for matchFolder in os.listdir("./" + folder):
          with open("./" + folder+'/'+  matchFolder + '/'+ team1) as csv_file:
            setupPerformanceDict(performance, csv_file)

          with open("./" + folder+'/'+  matchFolder + '/'+ team2) as csv_file:
            setupPerformanceDict(performance, csv_file)
    else:
      if folder in folders:
        with open("./" + folder+'/'+ team1) as csv_file:
          setupPerformanceDict(performance, csv_file)
     
        with open("./" + folder+'/'+ team2) as csv_file:
          setupPerformanceDict(performance, csv_file)

          
for folder in os.listdir("./"):
    pngs = glob.glob("./" + folder +"/*.png")

    if len(pngs) == 0 and folder in folders:
        for matchFolder in os.listdir("./" + folder):
          with open("./" + folder+'/'+  matchFolder + '/'+ team1) as csv_file:
            addToPerformanceDict(performance, csv_file)
            
          with open("./" + folder+'/'+  matchFolder + '/'+ team2) as csv_file:
           addToPerformanceDict(performance, csv_file)

    else:
      if folder in folders:
        with open("./" + folder+'/'+ team1) as csv_file:
          addToPerformanceDict(performance, csv_file)    

        with open("./" + folder+'/'+ team2) as csv_file:
         addToPerformanceDict(performance, csv_file)

          
for key in performance:
  print(key, performance[key])