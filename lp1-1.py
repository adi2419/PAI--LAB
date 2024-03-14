#1st variavtion -mine orginal
#This variation is very basic . The flow of the code is first the inputs are taken and them the input is modified and with respect to the entry the box in the borad is edited

# a is the board its a 3*3 list 
a=[[" "for _ in range(3)]for _ in range(3)]
#p1 is used to store the input of the inde by player one 
p1=[]
#p2 is used to store the input of the inde by player two
p2=[]


#number of boxes is 9 in a 3*3 matrix 
for i in range(9):
    
    #take the input of the user one player after the other --  
    #enter p1 choise :1,0
    #p1=[1,0]
    #here split is used  so that when the input is seperated by "," it stores the input without the "," into the list p1 or p2 as two different entities for example
    
    p1=list(map(int,input("enter p1 choice ([],[]):").split(",")))
    #the list p1/p2 consists of 2 elements  (for example pl1=[1,0]) hence we use these 2 values as indexes in the 3*3 board and update the valuse respectively 
    a[p1[0]][p1[1]]="x"
    p2=list(map(int,input("enter p2 choice ([],[]):").split(",")))
    a[p2[0]][p2[1]]="o"

for i in range(3):
    #to check for winner after the board is filled -- this has a draw back if both had the chance to win but one player wins befor the other in that case the code fails 
    
    #to check if pl has wont vertical or horizontal or diagonal stike 
    if a[i][0]==a[i][1]==a[i][2]=="x" or a[0][i]==a[1][i]==a[2][i]=="x" or a[i][i]=="x" or a[i][2-i]=="x":
        print("ply1 wins")
        break
    elif a[i][0]==a[i][1]==a[i][2]=="o" or a[0][i]==a[1][i]==a[2][i]=="o"or a[i][i]=="o" or a[i][2-i]=="o":
        print("ply2 wins")
    else:
        print("draw")
        
#print the board 
for row in a:
    print(row)
  
