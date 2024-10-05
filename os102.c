#include <stdio.h>
#include <stdlib.h>

void scan(int queue[], int head, int size, char direction) {
    int totalSeekTime = 0;
    int currentTrack = head;
    int minTrack = 0, maxTrack = 199;
    int seekSequence[100];
    int seekCount = 0;

    printf("\nSCAN Disk Scheduling Algorithm:\n");

    if (direction == 'l') {
        printf("Sequence of tracks visited: %d ", currentTrack);
        for (int i = currentTrack; i >= minTrack; i--) {
            if (i == minTrack) {
                totalSeekTime += abs(currentTrack - minTrack);
                currentTrack = minTrack;
                printf("%d ", currentTrack);
            } else {
                if (queue[i] == 1) {
                    totalSeekTime += abs(currentTrack - i);
                    currentTrack = i;
                    printf("%d ", currentTrack);
                    seekSequence[seekCount++] = currentTrack;
                }
            }
        }

        for (int i = 0; i < size; i++) {
            if (queue[i] == 1) {
                continue;
            } else {
                if (i == 0) {
                    totalSeekTime += abs(currentTrack - minTrack);
                    currentTrack = minTrack;
                    printf("%d ", currentTrack);
                }
            }
        }
    } else if (direction == 'r') {
        printf("Sequence of tracks visited: %d ", currentTrack);
        for (int i = currentTrack; i <= maxTrack; i++) {
            if (i == maxTrack) {
                totalSeekTime += abs(currentTrack - maxTrack);
                currentTrack = maxTrack;
                printf("%d ", currentTrack);
            } else {
                if (queue[i] == 1) {
                    totalSeekTime += abs(currentTrack - i);
                    currentTrack = i;
                    printf("%d ", currentTrack);
                    seekSequence[seekCount++] = currentTrack;
                }
            }
        }

        for (int i = size - 1; i >= 0; i--) {
            if (queue[i] == 1) {
                continue;
            } else {
                if (i == size - 1) {
                    totalSeekTime += abs(currentTrack - maxTrack);
                    currentTrack = maxTrack;
                    printf("%d ", currentTrack);
                }
            }
        }
    }

    printf("\nTotal seek time: %d\n", totalSeekTime);
}

int main() {
    int queue[] = {0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0};
    int head = 53;
    int size = sizeof(queue) / sizeof(queue[0]);

    // Setting 1's at the tracks where we have requests
    for (int i = 0; i < size; i++) {
        if (queue[i] == head) {
            queue[i] = 1;
        } else {
            queue[i] = 0;
        }
    }

    scan(queue, head, size, 'l');

    return 0;
}
