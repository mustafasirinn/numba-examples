import numpy as np
from timeit import default_timer as timer

def us_alma(a, b, c):
    for i in range(a.size):
         c[i] = a[i] ** b[i]

def main():
    boyut = 100000000
    a = b = np.array(np.random.sample(boyut), dtype=np.float32)
    c = np.zeros(boyut, dtype=np.float32)
    baslama = timer()
    us_alma(a, b, c)
    sure = timer() - baslama
    print(sure)

if __name__ == '__main__':
    main()