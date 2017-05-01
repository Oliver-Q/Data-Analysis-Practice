#load data file
path = "white_wine.csv"
import csv 

#save data in 'content'
f = open(path,'r')
reader = csv.reader(f)
content = []
for re in reader:
    content.append(re)
print(content[:2])
#['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
#['7', '0.27', '0.36', '20.7', '0.045', '45', '170', '1.001', '3', '0.45', '8.8', '6']

#show all 'quality' categories of 'white_wine.csv' 
qualities = []
for row in content[1:]:
    qualities.append(int(row[-1]))
unity_quality = set(qualities)
print unity_quality
#set([3, 4, 5, 6, 7, 8, 9])

#divide 'qualities' data into 7 keys of a dictionary 
content_dict = {}
for row in content[1:]:
    quality = int(row[-1])    
    if quality not in content_dict.keys():
        content_dict[quality] = [row]  
    else:
        content_dict[quality].append(row)
print content_dict.keys()
#[3, 4, 5, 6, 7, 8, 9]

#count the number of sample in each key
number_tuple = []
for key, value in content_dict.items():
    number_tuple.append((key, len(value)))
print number_tuple
#[(3, 14), (4, 115), (5, 1020), (6, 1539), (7, 616), (8, 123), (9, 4)]

#calculate the average of 'fixed acidity' in each key
mean_tuple = []
for key, value in content_dict.items():
    sum_ = 0
    for row in value:
        sum_ += float(row[0])
    mean_tuple.append((key, sum_/len(value)))
print mean_tuple
#[(3, 7.535714285714286), (4, 7.052173913043476), (5, 6.907843137254891), (6, 6.812085769980511), (7, 6.755844155844158), (8, 6.708130081300811), (9, 7.5)]
