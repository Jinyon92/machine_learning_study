record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo','Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']

di = dict()
for line in record:
    word = line.split()
    if word[0] == 'Enter' or word[0] == 'Change':
        di[word[1]] = word[2]

answer = []
for line in record:
    word = line.split()
    if word[0] == 'Enter':
        answer.append("{}님이 들어왔습니다.".format(di[word[1]]))
    if word[0] == 'Leave':
        answer.append("{}님이 나갔습니다.".format(di[word[1]]))

print(answer)
