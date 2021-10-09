# Libraries
import numpy as np
import matplotlib.pyplot as plt


from NHentai import NHentai
import pickle

nh = NHentai()


tag_dict = {}
tag_freq = {}

#test_d = nh.get_doujin(id=373957)
#for x in test_d.tags:
#    print(x.name)

def tagUpdate(book):
    Doujin = nh.get_doujin(id=book)
    #print(Doujin.total_favorites)
    #print(Doujin.title)
    for tag in Doujin.tags:
        if tag.type == "tag":
            if tag.name in tag_dict:
                tag_dict[tag.name] = tag_dict[tag.name] + Doujin.total_favorites
                tag_freq[tag.name] = tag_freq[tag.name] + 1
            else:
                tag_dict[tag.name] = Doujin.total_favorites
                tag_freq[tag.name] = 1


#queryString = "english sakura haruno"
queryString = "english blowjob blackmail"

#random_doujin:
resultsPage = nh.search(query=queryString)


#for pages in resultsPage.total_pages:
pageNum = resultsPage.total_pages

for i in range(1, pageNum + 1):
    searchPage = nh.search(query=queryString, page=i)
    for x in searchPage.doujins:
        tagUpdate(x.id)


# The graph

avg_dict = {}

for x in tag_dict:
    avg_dict[x] = tag_dict[x] / tag_freq[x]

avgOrdered = [(x, avg_dict[x]) for x in sorted(avg_dict, key=avg_dict.get)]

#print(tag_dict)
#print(tag_freq)
#print(avgOrdered)
hValues = []
barNames = []
for x in avgOrdered:
    hValues.append(x[1])
    barNames.append(x[0])

#print(hValues)
#print(barNames)

y_pos = np.arange(len(barNames))
plt.figure(figsize=(10, 10))
plt.barh(barNames, hValues)
#plt.xticks(y_pos, barNames)


plt.show()
"""
# Make a random dataset:
height = [3, 94, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()
"""

