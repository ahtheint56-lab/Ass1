#for i in range(5):
    #print(i)

scores =[75,85,90,68,45]
for score in scores:
    print(score)

    count = 1
while count <= 5:
    print(count)
    count += 1

scores = [70, 85, 60, 90, 45]
total = 0
for score in scores:
    total +=score
average = total / len(scores)
print("Total:", total)
print("Average:", average)

scores = [45, 70, 85, 30, 90, 55]
total = 0
passing=0
failing=0
for score in scores:
    total +=score
if score>=40:
    passing +=1
else:
    failing +=1

average = total / len(scores)

print("Total:", total)
print("Average:", average)
print("Passing Scores:",passing)
print("Failing Scores:",failing)