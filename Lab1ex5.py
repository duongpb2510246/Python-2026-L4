color = ["blue","yellow","purple","red","white"]
favor = input("What is your favorite colors:")
if favor in color:
   idx = color.index(favor)
   print(f"Your color is at {idx} in my list")
else:
   print("Sorry, I could not find my color") 