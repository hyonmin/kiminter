score_file = open("score.txt", "w", encoding = "utf8")
print("Math: 0", file=score_file)
print("English: 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("Science: 80")
score_file.write("\nCoding: 100")
score_file.close()
