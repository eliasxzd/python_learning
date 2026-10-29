# scores = [88,92,45]
# s = 0.0
# ave = 0.0
# for i in scores:
#     s += i
# ave = s / len(scores)
# print(f"平均分是{ave}")

# print("1-50之间能被3整除的数有：")
# s = 0
# for i in range(1,51):
#     if i % 3 == 0:
#         s += i
#         print(f"{i}",end=" ")
# print(f"这些总和为{s}")

# def count_vowels(s):
#     count = 0
#     for char in s:
#         if char in "aeiouAEIOU":
#             count +=1
#     return count
# s = input("请输入一个字符串:")
# count = count_vowels(s)
# print(f"该字符串的元音字母有{count}个")

# students = {"张三": 55, "李四": 18, "王五": 90}
# student = []
# for name, score in students.items():
#     if score < 60:
#         student.append(name)
# with open("fail.txt","w",encoding="utf-8") as f:
#         for name in student:
#             f.write(name + "\n")
# with open("fail.txt","r",encoding="utf-8") as f:
#     content = f.read()
# print(f"成绩不合格的学生有：\n{content}")