from hub.api.dataset import Dataset
from torch import tensor


def test_logs():
    logs = Dataset(dtype={"train_acc": float, "train_loss": float, 
                          "val_acc": float, "val_loss": float},
                   shape=(2,), url='./models', mode='w')
    metrics_1 = {'val_loss': tensor(1.21), 
               'val_acc': tensor(0.5),
               'train_loss': tensor(2.4),
               'train_acc': tensor(0.75)}
    metrics_2 = metrics_1
    for key, value in metrics_1.items():
        logs[key][0] = value.item()
    for key, value in metrics_2.items():
        logs[key][1] = value.item()
    assert logs['val_loss'][0].numpy() == 1.21
    assert logs['train_loss'][1].numpy() == 2.4
    
if __name__ == "__main__":
    test_logs()