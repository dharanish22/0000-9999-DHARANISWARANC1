sd = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] 
td = [ "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]
tm = [ "Twenty", "Thirty", "Forty","Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
tp = ["Hundred", "Thousand"]
#print("")
print("Enter q to exit")
inp=input("Enter Any Number From 0000-9999:")
if(inp=='q'):
    exit()
try:
  n=int(inp)      
  l=len(inp)  
  s=list(inp)
  j=0
  word=''
  if(n==0):
      print("Zero")
  elif(l>4 or n<0):
      print("Invalid input")
  else:
      for i in range((4-l),4):
          num=int(s[j])
          if i==0 and num!=0:
              word =word+sd[num]+' '+tp[1]
          elif i==1 and num!=0:
              if int(s[j+1])==0:
                word =word+' '+sd[num]+' '+tp[0]
              elif(s[j+1]!=0):
                word =word+' '+sd[num]+' '+tp[0]+' And '
          elif i==2 and num==1 and num!=0:
              word=word+td[int(s[j+1])]+' '
              break
          elif i==2 and num!=1 and num!=0:
              word=word+tm[num-2]+' '
          elif i==3 and num!=0:
              word=word+sd[num]+' '
          j=j+1
      print(word)
except:
  print("Invalid Input")
    
