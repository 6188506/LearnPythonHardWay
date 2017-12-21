python 100例
===
+ 1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
  ```for i in range(1,5):
        for x in range(1,5):
           for y in range(1,5):
               if i<>x and i<>y and x<>y:
                   print i,x,y ```

+ 2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
 ```  I = int(raw_input("please input profitablity!"))
      if I < = 10:
         print "The bonus is %f " % I*10%
      elif 10 < I < 20:
         print "The bonus is %f " % (I-10)*7.5% + 10*10%
      elif 20 <= I < 40:
         print "The bonus is %f " % (I-20)*5% + 20*7.5%
      elif 40 <= I < 60:
         print "The bonus is %f " % (I-40)*3% + 40*5%
      elif 60 <= I < 100:
         print "The bonus is %f " % (I-60)*1.5% + 60*3%
      else 100 < I :
         print "The bonus is %f " % (I-100)*1% + 100*1.5%