note=[2000,500,200,100,50,20,10,5,2,1]
amount = int(input("Enter Amount :"))
notes=0

for item in note:
    if amount>0:
        notes+=amount//item
        amount=amount%item

print(f"Total notes required are : {notes} .")

            