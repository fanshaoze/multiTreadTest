# mpi4py version 3.0.2
# Executed via "mpiexec --hostfile hostfile -n 9 python3.7 -m mpi4py.futures mpi.py"
import sys
sys.path.append("C:\\1D\pypro\\multiTreadTest\\")
from mpi4py.futures import MPIPoolExecutor
import sys
import time
from MPITest.julia import julia_line

if __name__ == '__main__':

    for scale in range(1, 9):
        start_time = time.time()
        with MPIPoolExecutor(8) as executor:
            w = 640*2*scale
            h = 480*2*scale
            image = executor.map(julia_line, ((i, w, h) for i in range(h)))
            with open(f'julia-mpi-{scale}.pgm', 'wb') as f:
                f.write(b'P5 %d %d %d\n' % (w, h, 255))
                for line in image:
                    f.write(line)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Scale {scale}, Time {duration:>6.6f}s")
