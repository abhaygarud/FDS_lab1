
r=int(input("enter the number of rows"))
c=int(input("enter the number of column"))
print("enter the number of matrix in row wise form :")

def matrix_1(r,c):
    out=[]
    for i in range(r):
        m1=[]
        for j in range (c):
            num=int(input("enter the number to be inserted in the matrix= "))
            m1.append(num)
        out.append(m1)
    return out
def matrix_2(r,c):
    out1=[]
    for i in range(r):
        m2=[]
        for j in range (c):
            num1=int(input("enter the number to be inserted in the matrix= "))
            m2.append(num1)
        out1.append(m2)
    return out1
a=matrix_1(r,c)
b=matrix_2(r,c)
print("matrix =",a)
print("matrix = ",b)

#addition of the two matrix

result_add=[]
def add():
    print("______________________ addition________________________") 
        
    for i in range(len(a)):
        temp=[]
        for j in range(len(b[0])):
            temp.append( a[i][j]+b[i][j])
        result_add.append(temp)
    print("addittion of the two matrix is ",result_add)
    
#subtraction of the two matrix

def sub():
    print("_____________________subtraction________________________")
    result_sub=[]

    for i in range (len(a)):
        temp=[]
        for j in range (len(b[0])):
            temp.append(a[i][j]-b[i][j])
        result_sub.append(temp)
    print("subtraction of the two matrix is =",result_sub)

def tranpose():
    print("_______________TRANPOSE_____________")
    tranpose_result=[]

    for i in range(len(a)):
        temp2=[]
        for j in range(len(b[0])):
            temp2.append(a[j][i] and b[j][i])
        tranpose_result.append(temp2)
    print(tranpose_result)

def mul():
        print("__________________multiplication__________________")
        mul_result=[]
        for i in range (len(a)):
            temp=[]
            for j in range(len(b[0])):
                temp.append(a[i][j]*b[i][j])        
            mul_result.append(temp)
        print("Mulitiplication of both the matrix is ",mul_result)

        


add()
sub()
tranpose()
mul()

