#include <stdio.h>
#include <stdlib.h>

void fcfs(int queue[], int head, int size) {
    int totalSeekTime = 0;
    int currentTrack = head;

    printf("FCFS Disk Scheduling Algorithm:\n");
    printf("Sequence of tracks visited: %d ", currentTrack);
    
    for (int i = 0; i < size; i++) {
        totalSeekTime += abs(currentTrack - queue[i]);
        currentTrack = queue[i];
        printf("%d ", currentTrack);
    }

    printf("\nTotal seek time: %d\n", totalSeekTime);
}

int main() {
    int queue[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int head = 53;
    int size = sizeof(queue) / sizeof(queue[0]);

    fcfs(queue, head, size);

    return 0;
}
