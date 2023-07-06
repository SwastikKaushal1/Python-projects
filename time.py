a=int(input("Enter the time in secounds"))
b= a//3600
c= a-(3600*b)
a=c// 60
d= c//60
e= c-(60*a)
print("The time is ",b,"hours ",d,"min and",e,"secounds")
