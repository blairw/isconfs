import os
import yaml

dataset = []
htmlpage = []

####################
## SORT OUT DATASET
####################

# Adapted from https://stackoverflow.com/a/3964691, https://stackoverflow.com/a/1774043
for file in sorted(os.listdir("../data/")):
    if file.endswith(".yml"):
        with open("../data/" + file, "r") as stream:
            try:
                this_file = yaml.safe_load(stream)
                dataset.append(this_file)
            except Exception as exc:
                print(exc)


####################
## GENERATE THE PAGE
####################

with open("../html/010-top.html", "r") as file:
    htmlpage.append(file.read())

htmlpage.append('<table width="100%">')

htmlpage.append('<thead>')
htmlpage.append('<tr>')
htmlpage.append('<th></th>')
for conference in dataset:
    htmlpage.append('<th style="width: 15%;"><a href="' + \
        conference.get('header').get('url') + '">' + \
        conference.get('header').get('name') + '</a></th>')

htmlpage.append('</tr>')
htmlpage.append('</thead>')

htmlpage.append('<tbody>')
for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Oct', 'Nov', 'Dec']:
    htmlpage.append('<tr>')
    htmlpage.append('<td>' + month + '</td>')
    htmlpage.append('</tr>')

htmlpage.append('</tbody>')

htmlpage.append('</table>')

with open("../html/090-bottom.html", "r") as file:
    htmlpage.append(file.read())

print("\n".join(htmlpage))
# print(dataset)
