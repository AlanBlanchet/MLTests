import torch
from pathlib import Path

d = "/".join(__file__.split("/")[:-1])

path = Path(d, "../ecg_sv.ipynb")

print(path)
print(path.resolve())

torch.load(path.resolve())
