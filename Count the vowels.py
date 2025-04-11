s=input()
V="aeiouAEIOU"
c=sum(1 for char in s if char in V)
print(c)
