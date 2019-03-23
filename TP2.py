import subprocess
app = "gophersat-1.1.exe"
fichier_licorne = "licorne.cnf"
fichier_graphie = "graphie3.cnf"

def interpretation(list1, list2):
    return dict(zip(list1, list2))
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# # EX1
# list_licorne_positives = ["mortel", "myrthique", "mammifice", "corne", "magique"]
# list_num_licorne_positives = [1, 2, 3, 4, 5]
# list_licorne_negatives = ["immortel", "pas myrthique", "pas mammifice", "pas corne", "pas magique"]
# list_num_licorne_negatives = [-1, -2, -3, -4, -5]
#
# licorne_positives=interpretation(list_num_licorne_positives,list_licorne_positives)
# licorne_negatives = interpretation(list_num_licorne_negatives,list_licorne_negatives)
# licorne_negatives.update(licorne_positives)
#
# sorti = subprocess.run([app,fichier_licorne],stdout = subprocess.PIPE).stdout.decode("UTF-8").split()
#
# licorn = ""
# for i in sorti:
#     if RepresentsInt(i):
#         for j in licorne_negatives:
#             if int(i) == j:
#                 licorn += " soit " + licorne_negatives[j]
# print("le licorne est: " + licorn)

#EX2
list_color = ["r", "g", "b"]
list_sommet = ["S1", "S2", "S3"]
list_object = []
list_num_graphie = []
num = 1
for sommet in list_sommet:
    for color in list_color:
        list_object.append(color+sommet)
        list_num_graphie.append(num)
        num += 1

graphie_object = interpretation(list_num_graphie,list_object)
sorti = subprocess.run([app,fichier_graphie],stdout = subprocess.PIPE).stdout.decode("UTF-8").split()
graphie = ""
print(sorti)
for i in sorti:
    if RepresentsInt(i):
        for j in graphie_object:
            if int(i) == j:
                graphie += "  " + graphie_object[j]
print("le graphie est: " + graphie)