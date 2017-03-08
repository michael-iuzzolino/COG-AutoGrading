
count = 0
incorrect_count = 0
with open("test.txt", "r") as infile:
    for line in infile:
        if line.strip() != "50":
            print(line)
            incorrect_count += 1

        count +=1

print("{} / {}".format(incorrect_count, count))

average_incorrect = incorrect_count / (count * 1.0)

print("Average incorrect: {}".format(average_incorrect*100))
print("Average correct: {}".format((1 - average_incorrect)*100))
