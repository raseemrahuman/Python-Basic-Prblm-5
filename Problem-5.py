#A.Answer
Var = input("ENTER SOMETHING TO FIND ")
UPcount = 0
LOcount = 0

for ch in Var:
   if ch.isupper():
      UPcount=UPcount+1
   elif ch.islower():
      LOcount=LOcount+1
   else:
      pass
print("UPPERCASE:", UPcount)
print("LOWERCASE:", LOcount)
