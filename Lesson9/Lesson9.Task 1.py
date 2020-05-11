import json

new_file = open('myfile.txt', 'w+')
new_file.write('Hello file world!\n')
new_file.close()

new_file = open('myfile.txt', 'r+')
print(new_file.read(17))
new_file.write('Hello file world!')
new_file.seek(0)
print(new_file.read())
new_file.close()

# Does the new file show up in the directory where you ran your scripts? Ні, не створився окремий файл
# What if you add a different directory path to the filename passed to open? Вибиває помилку.
