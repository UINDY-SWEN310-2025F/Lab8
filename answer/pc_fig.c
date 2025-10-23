#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <pthread.h>
#include <stdlib.h>
#include <semaphore.h>

int max;
int loops;

sem_t empty;
sem_t full;

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
    if (argc != 4) {
	fprintf(stderr, "usage: %s <buffersize> <loops> <consumers>\n", argv[0]);
	exit(1);
    }
    max   = atoi(argv[1]);
    loops = atoi(argv[2]);
    consumers = atoi(argv[3]);
    assert(consumers <= MAX);

    buffer = (int *) malloc(max * sizeof(int));
    assert(buffer != NULL);
    int i;
    for (i = 0; i < max; i++) {
	    buffer[i] = 0;
    }

    sem_init(&empty, 0, max); // MAX are empty
    sem_init(&full, 0, 0);    // 0 are full

    pthread_t pid, cid[MAX];
    pthread_create(&pid, NULL, producer, NULL); 
    
    for (i = 0; i < consumers; i++) {
	    pthread_create(&cid[i], NULL, consumer, (void *) (long long int) i); 
    }
    pthread_join(pid, NULL); 
    for (i = 0; i < consumers; i++) {
	    pthread_join(cid[i], NULL); 
    }
    return 0;
}

