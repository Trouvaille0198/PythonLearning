import matplotlib.pyplot as plt
with open('Data/score.txt') as file_obj:
    data = {}
    for line in file_obj:
        line_list = line.split()
        data[line_list[0]] = line_list[1:]
del data['考号']

for key, value in data.items():
    total_score = int(value[0])+int(value[1])+int(value[2])
    if total_score < 180 or int(value[0]) < 60 or int(value[1]) < 60 or int(value[2]) < 60:
        value.append('不及格')
    elif total_score >= 260 and int(value[0]) >= 85 and int(value[1]) >= 85 or int(value[2]) >= 85:
        value.append('优秀')
    else:
        value.append('及格')
program = [value[0] for value in data.values()]
biology = [value[1] for value in data.values()]
science = [value[2] for value in data.values()]
plt.figure()
plt.hist(program, bins=4)
plt.hist(biology, bins=4)
plt.hist(science, bins=4)
file_path = "Data/level.txt"
with open(file_path, "w") as file_obj:
    for key, value in data.items():
        one_piece = key + " " + value[-1] + "\n"
        file_obj.write(one_piece)
