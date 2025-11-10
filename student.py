import sys

if len(sys.argv) ==3:
   script_name= sys.argv[0]
   name= sys.argv[1]
   roll no= sys.argv[2]
   print("user provided input values:")

else:
     script_name = sys.argv[0]
     name= "sameer"
     roll n0= "110"
     print ("No input given - usong default values:")

print ("script Name:", script_name)
print("Student Name:", name)
print ("Roll number:", roll no)

