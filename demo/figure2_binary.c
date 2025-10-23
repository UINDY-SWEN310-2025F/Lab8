#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

int main(int argc, char *argv[]) {

    int X=1;

    sem_t m;
    sem_init(&m, 0, X); //initialize to X; what value should X be?

    sem_wait(&m);
    // critical section here
    sem_post(&m);
    return 0;
}
    
