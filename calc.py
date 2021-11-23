import math
import numpy as np
import calculator
c=9+7
for i in range(0,len(str(c))):
    if str(c)[i]=='.':
        c=str(c)[:i+4]
        break
calculator.var2.set(c)