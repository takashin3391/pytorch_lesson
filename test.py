import torch

device = torch.device(type='mps')
a = torch.tensor([3])
a.to(device)
print(a)
print(device)
