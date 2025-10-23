#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <pthread.h>
#include <stdlib.h>

#include "common_threads.h"

#include <semaphore.h>

int max;
int loops;
int *buffer;

//@Todo: declare variables that are needed

#define CMAX (10)
int consumers = 1;

void do_fill(int value) {
    buffer[fill] = value;
    //@Todo: finish do_fill()

}

int do_get() {
    int tmp = buffer[use];
    //@Todo:  finish do_get()

}

void *producer(void *arg) {
    //@Todo

    return NULL;
}
                                                                               
void *consumer(void *arg) {
    //@Todo

    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "usage: %s <buffersize> <loops> <consumers>\n", argv[0]);
        exit(1);
    }
    max   = atoi(argv[1]);
    loops = atoi(argv[2]);
    consumers = atoi(argv[3]);
    assert(consumers <= CMAX);

    buffer = (int *) malloc(max * sizeof(int));
    assert(buffer != NULL);
    int i;
    for (i = 0; i < max; i++) {
	buffer[i] = 0;
    }

    // Todo: finish main()


    return 0;
}

