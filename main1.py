string = ("Guvi Geeks Network Private Limited")
count = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count+=1
if count == 0:
    print("No vowels found")
else:
    print("Total vowels are:" + str(count))

for j in string:
    if j=="a":
        count_a+=1
    elif j =="e":
        count_e+=1
    elif j =="i":
        count_i+=1
    elif j =="o":
        count_o+=1
    elif j == "u":
        count_u+=1


if count_a ==0:
      print("No A found")
else:
    print("Total A's are:" + str(count_a))

if count_e ==0:
      print("No E found")
else:
    print("Total E's are:" + str(count_e))
       
if count_i ==0:
      print("No I found")
else:
    print("Total I's are:" + str(count_i))       

if count_o ==0:
      print("No O found")
else:
    print("Total O's are:" + str(count_o)) 

if count_u ==0:
      print("No U found")
else:
    print("Total U's are:" + str(count_u)) 