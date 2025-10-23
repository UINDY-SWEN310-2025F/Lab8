#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <pthread.h>
#include <stdlib.h>
#include <semaphore.h>

int max;
int loops;

int MAX = 10;
int consumers = 1;

int *buffer;
int use  = 0;
int fill = 0;

void put(int value) {
    buffer[fill] = value;
    fill++;
    if (fill == max)
	fill = 0;
}

int get() {
    int tmp = buffer[use];
    use++;
    if (use == max)
	use = 0;
    return tmp;
}

sem_t empty;
sem_t full;

void *producer(void *arg) {
    int i;
    for (i = 0; i < loops; i++) {
        sem_wait(&empty); // Line P1
        put(i);           // Line P2
        sem_post(&full);  // Line P3
    }
    put(-1);              // Line P4
    return NULL;
}

void *consumer(void *arg) {
    int i, tmp = 0;
    while (tmp != -1) {
        sem_wait(&full);    // Line C1
        tmp = get();        // Line C2
        sem_post(&empty);   // Line C3 
        printf("%lld %d\n", (long long int) arg, tmp);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    //...
    sem_init(&empty, 0, max); // max are empty
    sem_init(&full, 0, 0);    // 0 are full
    //...
}

