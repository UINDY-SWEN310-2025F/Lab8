#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "common_threads.h"
#include "zemaphore.h"

Zem_t s;

//@TODO: add necessary codes to fix this
void *child(void *arg) {
    sleep(4);
    printf("child\n");
    return NULL;
}

int main(int argc, char *argv[]) {
    Zem_init(&s, 0); 
    printf("parent: begin\n");
    pthread_t c;
    printf("parent: end\n");
    return 0;
}
    
