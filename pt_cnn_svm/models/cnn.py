import torch


class CNN(torch.nn.Module):
    def __init__(
        self,
        input_dim: int = 1,
        num_classes: int = 10,
        model_device: torch.device = torch.device("cpu"),
        learning_rate: float = 1e-4,
    ):
        super().__init__()
        self.layers = torch.nn.ModuleList(
            [
                torch.nn.Conv2d(
                    in_channels=input_dim,
                    out_channels=64,
                    kernel_size=8,
                    stride=2,
                    padding=1,
                ),
                torch.nn.ReLU(),
                torch.nn.Conv2d(
                    in_channels=64, out_channels=128, kernel_size=6, stride=2, padding=1
                ),
                torch.nn.ReLU(),
                torch.nn.Flatten(),
                torch.nn.Linear(in_features=(128 * 5 * 5), out_features=2048),
                torch.nn.ReLU(),
                torch.nn.Linear(in_features=2048, out_features=2048),
                torch.nn.ReLU(),
                torch.nn.Linear(in_features=2048, out_features=512),
                torch.nn.ReLU(),
                torch.nn.Linear(in_features=512, out_features=num_classes),
            ]
        )
