
print("start")
if 4 > 2:
    print("sometimes run me")
print("end")



a = 4
print("start")
if a > 2:
    print("sometimes run me")
    print("Then run me too!")
print("end")

a = 5
b = 7
if a < b:
    print(str(a) + " on väiksem kui " + str(b))
elif a > b:
    print(str(a) + " on suurem kui " + str(b))
else:
    print(str(a) + " ja " + str(b) + " on võrdsed!")


a = 5
b = 2
if a > 4:
    if b > 1:
        print("on nii")
    print("ja ei ole")

# on nii
# ja ei ole

a = 5
b = 1
if a > 4:
    if b > 1:
        print("on nii")
    print("ja ei ole")
# ja ei ole
