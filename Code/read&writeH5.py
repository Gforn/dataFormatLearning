import h5py
import numpy as np

# writing to h5
imgData = np.zeros((30, 3, 128, 256))
f = h5py.File('testH5.h5', 'w')
f['data'] = imgData
f['labels'] = range(100)
f.close()

# reading from h5
f = h5py.File('testH5.h5', 'r')
print('key:')
print(f.keys())
print('#######################################')
a = f['data'][:]
print('value:')
print(a)
f.close()
