# Executed via "python3.7 mp.py"

from multiprocessing import Pool
import sys
import time
from MPITest.julia import julia_line

if __name__ == '__main__':

    for scale in range(1, 9):
        start_time = time.time()
        with Pool(8) as pool:
            w = 640*2*scale
            h = 480*2*scale
            image = pool.map(julia_line, ((i, w, h) for i in range(h)))
            with open(f'julia-mp-{scale}.pgm', 'wb') as f:
                f.write(b'P5 %d %d %d\n' % (w, h, 255))
                for line in image:
                    f.write(line)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Scale {scale}, Time {duration:>6.6f}s")
