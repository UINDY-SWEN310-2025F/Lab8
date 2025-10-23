#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "common_threads.h"


//TODO: Declare semaphore variable 
volatile int counter = 0;

//TODO: Fix the codes by using functions in common_threads.h
void *child(void *arg) {
    int i;
    for (i = 0; i < 10000000; i++) {
	   counter++;
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t c1, c2;	
    Pthread_join(c1, NULL);
    Pthread_join(c2, NULL);
    printf("result: %d (should be 20000000)\n", counter);
    return 0;
}
    
