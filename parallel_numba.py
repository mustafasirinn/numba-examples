import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(['float32(float32, float32)'], target='cuda')
def us_alma(a, b):
    return a ** b

def main():
    boyut = 100000000
    a = b = np.array(np.random.sample(boyut), dtype=np.float32)
    c = np.zeros(boyut, dtype=np.float32)
    baslama = timer()
    c = us_alma(a, b)
    sure = timer() - baslama
    print(sure)

if __name__ == '__main__':
    main()	