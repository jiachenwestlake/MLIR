import torch

a = torch.abs(torch.ones(1) - torch.zeros(1))
b = 0.
b += a

print(b)