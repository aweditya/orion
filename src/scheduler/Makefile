CC=g++
NVCC=/usr/local/cuda/bin/nvcc
CFLAGS=-O3
CUDAINCLUDE=/usr/local/cuda/include/
CUDALIB=/usr/local/cuda/lib
CUDALIB64=/usr/local/cuda/lib64

utils_sched.o: utils_sched.cpp
	$(NVCC) $(CFLAGS) -Xcompiler  -fPIC -x cu -shared -c utils_sched.cpp -I$(CUDAINCLUDE) -L$(CUDALIB64) -L$(CUDALIB) -lcudart -lcudnn -lcublas -lpthread

scheduler.o: scheduler.cpp
	$(NVCC) $(CFLAGS) -Xcompiler  -fPIC  -x cu -shared -c scheduler.cpp -I$(CUDAINCLUDE) -L$(CUDALIB64) -L$(CUDALIB) -lcudart -lcudnn -lcublas -lpthread

scheduler_eval.o: scheduler_eval.cpp
	$(NVCC) $(CFLAGS) -Xcompiler  -fPIC  -x cu -shared -c scheduler_eval.cpp -I$(CUDAINCLUDE) -L$(CUDALIB64) -L$(CUDALIB) -lcudart -lcudnn -lcublas -lpthread

scheduler_eval.so: scheduler_eval.o utils_sched.o
	 $(CC) $(CFLAGS) -fPIC -shared utils_sched.o scheduler_eval.o -I$(CUDAINCLUDE) -L$(CUDALIB64) -L$(CUDALIB) -lcudart -lcudnn -lcublas -lpthread -o scheduler_eval.so

all:
	make scheduler_eval.so

clean:
	rm -rf *.o *.so
