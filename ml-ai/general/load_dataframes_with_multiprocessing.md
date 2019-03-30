# pd.read_csv with multiprocessing
This trick will come in handy for loading multiple large datasets.
```python
import time
import multiprocessing
start = time.time()
def load_dataframe(dataset):
    return pd.read_csv(dataset)

with multiprocessing.Pool() as pool:
    train, test = pool.map(load_dataframe, ['data/train.csv', 'data/test.csv'])
end = time.time()
print(f"Time multiprocessing: {end - start}")

start = time.time()
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
end = time.time()    
print(f"Time normal: {end - start}")
```

