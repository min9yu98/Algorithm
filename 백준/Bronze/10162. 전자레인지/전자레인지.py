t = int(input())
h = t//300
m = (t - (t//300)*300)//60
if (t - (h*300 + m*60))%10:  
    print(-1)
else:
    print(h, m, (t - (h*300 + m*60))//10)
