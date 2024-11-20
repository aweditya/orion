CC=g++
CUDAINCLUDE=/usr/local/cuda/include/
CUDALIB64=/usr/local/cuda/lib64
CUDALIB=/usr/local/cuda/lib

libinttemp.so: utils_interc.cpp intercept_cudnn.cpp intercept_cublas.cpp intercept_temp.cpp
	$(CC) -O3 -fPIC -shared utils_interc.cpp intercept_cudnn.cpp intercept_cublas.cpp intercept_temp.cpp -I$(CUDAINCLUDE) -L$(CUDALIB64) -L$(CUDALIB) -lcudart -lcudnn -lcublas -lpthread -o libinttemp.so

all:
	make libinttemp.so

clean:
	rm -rf *.o libinttemp.so
