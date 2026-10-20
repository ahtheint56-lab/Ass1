student_scores = [70, 85, 90, 65, 78]
print(student_scores)
print(student_scores[0])
print(student_scores[2])

scores = [70, 85, 90]
scores.append(95)
print(scores)
scores[0] = 75
print(scores)
scores.remove(85)
print(scores)
print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))


scores = [55, 80, 35, 90, 65] 
scores.append(75)
print(scores)
scores[1] = 85
print(scores) 

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
marks = [55,85,35,90,65,75]
result = calculate_average(marks)
print("Average:", result)


print("Highest:", max(scores))
print("Lowest:", min(scores))