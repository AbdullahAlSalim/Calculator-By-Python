Exam1 = 0   # this Number for First Exam
Exam2 = 0   # this Number for Second Exam
Exam3 = 0   # this Number for third Exam
Exam4 = 0   # this Number for 4 Exam
Exam5 = 0   # this Number for 5 Exam
Exam6 = 0   # this Number for 6 Exam
Exam7 = 0   # this Number for 7 Exam
Exam8 = 0   # this Number for 8 Exam
Exam9 = 0   # this Number for 9 Exam
Exam10 = 0   # this Number for 10 Exam

    # the codes below are constant you can not change it
total = Exam1 + \
        Exam2 + \
        Exam3 + \
        Exam4 + \
        Exam5 + \
        Exam6 + \
        Exam7 + \
        Exam8 + \
        Exam9 + \
        Exam10
    # the codes above are constant you can not change it

print("total contains:", total)

note = total
 
if note >= 100:  # 100 is not constant you can change it if you want
    print("Congratulations.. you passed the test!")
 
else:
    print("Sorry.. you failed the test!")