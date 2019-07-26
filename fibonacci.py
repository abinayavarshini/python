hcb=int(input())
if hcb!=0:
      print(1,end=' ')
      op=1
      nic=0
      for i in range(1,hcb):
          bvc=nic+op
          print(bvc,end=' ')
          nic=op
          op=bvc
else:
          print(0)
