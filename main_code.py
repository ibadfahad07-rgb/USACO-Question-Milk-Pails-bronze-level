cap_a,milk_a=map(int,input().split())
cap_b,milk_b=map(int,input().split())
cap_c,milk_c=map(int,input().split())

cap=[cap_a,cap_b,cap_c]
milk=[milk_a,milk_b,milk_c]

for i in range(100):
  a=i%3
  b=(i+1)%3
  space=cap[b]-milk[b]
  amount=min(milk[a],space)
  milk[a]-=amount
  milk[b]+=amount

print(*milk)