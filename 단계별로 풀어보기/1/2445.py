# *11111111*
# **111111**
# ***1111***
# ****11****
# **********

# ****  ****
# ***    ***
# **      **
# *        *


n = int(input())
for i in range(1,n+1):
    print('*'*i+' '*(2*(n-i))+'*'*i)
for i in range(n-1):#4번반복
    print('*'*(n-i-1)+' '*(2*(i+1))+'*'*(n-i-1))

