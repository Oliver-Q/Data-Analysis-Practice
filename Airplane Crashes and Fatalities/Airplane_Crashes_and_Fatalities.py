import numpy as np
import csv



path = "Airplane_Crashes_and_Fatalities_Since_1908_.csv"

# read in data
with open(path, "r") as f:
    reader = csv.reader(f)
    content = [row for row in reader]

# convert to numpy
content_array = np.array(content)

# show number of samples and variables
content_array_shape = content_array.shape	#dimention of numpy data
print "number of samples: %s, number of variables: %s"%content_array.shape
#number of samples: 5269, number of variables: 7

import datetime
import matplotlib.pyplot as plt
from matplotlib import cm
# plot bar graph 
def plot_stat(stat):
    fig, ax = plt.subplots(figsize=(32, 16))
    
    stat_items = stat.items()
    stat_items = sorted(stat_items, key=lambda x:x[0])
    year = list(zip(*stat_items)[0])
    year = map(int, year)
    accident_count = zip(*stat_items)[1]
    ind = np.arange(1, len(stat_items)+1)
    width = 0.35
    N = len(stat_items)
    ind = sorted(ind, key=lambda x:accident_count[x-1])
    accident_count = sorted(accident_count)
    for i in range(N):
        ax.bar(ind[i],accident_count[i],width, color=cm.jet(1.*i/N))
    ind = np.array(sorted(ind))
    plt.xticks(ind + width/2., year, rotation=90)
    plt.show()
    return 


stat_year = {}	#dictionary{year: number of occurrences}

for i in range(content_array.shape[0]):
    try:
        year = datetime.datetime.strptime(content_array[i, 0], '%m/%d/%Y').year	# convert to 'datetime.datetime' type via 'datetime'
		# Count the number of occurrences of each year
        if year in stat_year.keys():
            stat_year[year] += 1
        else:
            stat_year[year] = 1
	# for some items that cannot be converted to 'datetime.datetime' type
    except Exception, e:
        print u"Error items: %s" %content_array[i, 0]
        print e
        
plot_stat(stat_year)


content_array = [tuple(row) for row in content[1:]]	# convert data to 'tuple' type
# set every variables type to 'object'
dtype = [('Date', object),('Location', object),('Operator', object),('Type', object),('Aboard', object),('Fatalities', object),('Summary', object)]
content_name = np.array(content_array, dtype=dtype)


# calculate death_rate
content_name["Aboard"][content_name["Aboard"]==""] = np.nan
content_name["Fatalities"][content_name["Fatalities"]==""] = np.nan	# deal with default value
content_name["Aboard"] = content_name["Aboard"].astype(float)
content_name["Fatalities"] = content_name["Fatalities"].astype(float)

content_name["Aboard"][content_name["Aboard"] == 0] = np.nan	# prevent zero denominator

death_rate = content_name["Fatalities"] / content_name["Aboard"]

zero_death_rate = len(content_name[death_rate==0])


# find the operator which has max number of occurrences 
stat_operator = {}
for i in content_name["Operator"]:
    if i not in stat_operator.keys():
        stat_operator[i] = 1
    else:
        stat_operator[i] += 1

sorted_stat_operator = sorted(stat_operator.items(), key=lambda x:x[1], reverse=True)	#sort according to key values
max_operator = sorted_stat_operator[0][0]
print max_operator
#Aeroflot


# count number of occurrences each year of Aeroflot
stat_aeroflot = {}
content_aeroflot = content_name[content_name["Operator"]=="Aeroflot"]	#get data of Aeroflot

for i in content_aeroflot:
    year = i[0][-4:]	#i[0] is the datetime, [-4:] is the year
    if year not in stat_aeroflot.keys():
        stat_aeroflot[year] = 1
    else:
        stat_aeroflot[year] += 1

# plot stat_aeroflot
plot_stat(stat_aeroflot)