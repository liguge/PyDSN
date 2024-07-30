import torch
import torch.nn as nn
def entropy_loss(x):
    x1 = torch.reshape(x, (x.shape[0], -1)) # B, N 
    probs = torch.div(x1.T, x1.sum(dim=-1) + torch.finfo(x.dtype).eps).T # B, N
    entropy = -(probs * torch.clamp(torch.log(probs + torch.finfo(x.dtype).eps), min=torch.finfo(x.dtype).min)).sum(dim=-1) # B
    return entropy.mean()

def cyclostationary(x):
    x = x.pow(2)
    x = x.std(dim=-1) / (x.mean(dim=-1) + torch.finfo(x.dtype).eps)
    x = torch.fft.rfft(x, norm="forward").mean().abs()
    return x


def kurtosis_loss(x):
    kur = x.pow(4).mean(dim=1) / x.pow(2).mean(dim=1).pow(2) # B, T
    return kur.mean()

# def intelligent_spectrogram(x):
#     u_m = x.mean(dim=1)  #7,89
#     u_k = x.mean(dim=2)  #7,25
#     o_m = x.std(dim=1)   #7,89
#     o_k = x.std(dim=2)   #7,25
#     c_m = u_m / (o_m + torch.finfo(x.dtype).min)   #7,89
#     c_k = u_k / (o_k + torch.finfo(x.dtype).min)   #7,25
#     q_f = c_m.mean()
#     q_t = c_k.mean()
#     q = q_f * q_t
#     return q_f, q_t, q

def intelligent_spectrogram_loss(x):
    x = x.abs()
    c_m = x.std(dim=-2) / (x.mean(dim=-2) + torch.finfo(x.dtype).eps)
    c_k = x.std(dim=-1) / (x.mean(dim=-1) + torch.finfo(x.dtype).eps)
    q_f = (c_m / (c_m.max() + torch.finfo(x.dtype).eps)).mean()
    q_t = (c_k / (c_k.max() + torch.finfo(x.dtype).eps)).mean()
    q_ft = q_f * q_t
    # return torch.exp(0.5*(q_f ** 2 + q_t ** 2))-1
    # return torch.exp((q_f + q_t + torch.abs(q_f-q_t))/3.0) - 1
    return torch.exp((q_f + q_t + q_ft + torch.abs(q_f - q_t) + torch.abs(q_f - q_ft) + torch.abs(q_t - q_ft)) / 6.0) - 1

# a = torch.randn(7,25,89)(q_f + q_t + q)/3
# q_f, q_t, q = intelligent_spectrogram(a)
class Intelligent_spectrogram_loss_1(nn.Module):
    def __init__(self, a=1):
        super(Intelligent_spectrogram_loss, self).__init__()
        self.a = a
    def forward(self, x):
        x = x.abs()
        # c_m = x.std(dim=-2) / (x.mean(dim=-2) + torch.finfo(x.dtype).eps)
        # c_k = x.std(dim=-1) / (x.mean(dim=-1) + torch.finfo(x.dtype).eps)
        c_m = x.mean(dim=-2) / (x.std(dim=-2) + torch.finfo(x.dtype).eps)
        c_k = x.mean(dim=-1) / (x.std(dim=-1) + torch.finfo(x.dtype).eps)
        q_f = (c_m / (c_m.max() + torch.finfo(x.dtype).eps)).mean()
        q_t = (c_k / (c_k.max() + torch.finfo(x.dtype).eps)).mean()
        q_ft = q_f * q_t
        # return torch.exp(0.5*(q_f ** 2 + q_t ** 2))-1
        # return torch.exp((q_f + q_t + torch.abs(q_f-q_t))/3.0) - 1
        # return torch.exp(
        #     (q_f + q_t + q_ft + torch.abs(q_f - q_t) + torch.abs(q_f - q_ft) + torch.abs(q_t - q_ft)) / 6.0) - 1
        # return (q_f + q_t)/2.0
        # return (q_f + q_t + q_ft + torch.abs(q_f - q_t) + torch.abs(q_f - q_ft) + torch.abs(q_t - q_ft)) / 6.0
        # return (1 + self.a**2) * (q_f * q_t) / (self.a**2 * q_f + q_t)   ### right
        return 1/q_ft
        # return 3 * q_f * q_t * q_ft / (q_f * q_t + q_t * q_ft + q_ft * q_f)

class Intelligent_spectrogram_loss(nn.Module):
    def __init__(self):
        super(Intelligent_spectrogram_loss, self).__init__()
    def forward(self, x):
        x = x.abs()
        c_m = x.mean(dim=-2) / (x.std(dim=-2) + torch.finfo(x.dtype).eps)
        c_k = x.mean(dim=-1) / (x.std(dim=-1) + torch.finfo(x.dtype).eps)
        q_f = (c_m / (c_m.max() + torch.finfo(x.dtype).eps)).mean()
        q_t = (c_k / (c_k.max() + torch.finfo(x.dtype).eps)).mean()
        return 2.0 * q_f * q_t / (q_f + q_t)


class Calculate_renyi_entropy(nn.Module):
    def __init__(self, bins=50, alpha=2):
        super(Calculate_renyi_entropy, self).__init__()
        self.bins = bins
        self.alpha = alpha

    def forward(self, time_freq_map):
        time_freq_map = time_freq_map[0]
        histogram = torch.histc(time_freq_map, bins=self.bins)
        histogram.requires_grad_(True)
        probability = histogram / torch.sum(histogram)
        renyi_entropy = (1 / (1 - self.alpha)) * torch.log2(torch.sum(probability ** self.alpha))
        return renyi_entropy.mean()






        
        
