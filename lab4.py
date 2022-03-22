# zadanie 1
# list = []
# for x in range(0, 31):
#     x*=2
#     list.append(x)
# folder = open('list.txt', 'a+')
# folder.writelines(str(list))
# folder.close()

# zadanie 2
# folder = open('list.txt', 'r')
# print(folder.readlines())
# folder.close()

# zadanie 3
with open('list.txt', 'a+') as folder:
    for x in range(0, 5):
        folder.writelines('kilka linijki tekstu \n')
folder = open('list.txt', 'r')
print(folder.readlines())
folder.close()
