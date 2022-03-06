import torch

a=torch.load('../DAMSMencoders/bird/text_encoder550.pth')
a_keys=a.keys()
print(a_keys)