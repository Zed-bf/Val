import torch
import torch.nn as nn
#测试[:]
val = torch.zeros(3,4,5,6)
val_1 = val[ : ,2 , : ]
print("fighting")