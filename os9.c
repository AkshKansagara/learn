#include <stdio.h>
#include <stdbool.h>

#define MAX_FRAMES 10

void lru(int pages[], int n, int capacity) {
    int frame[MAX_FRAMES], frameCount = 0, pageFaults = 0;
    int leastRecent[MAX_FRAMES];

    for (int i = 0; i < n; i++) {
        bool pageFound = false;

        // Check if the page is already in the frame
        for (int j = 0; j < frameCount; j++) {
            if (frame[j] == pages[i]) {
                pageFound = true;

                // Update least recently used index
                for (int k = 0; k < frameCount; k++) {
                    if (leastRecent[k] < leastRecent[j]) {
                        leastRecent[k]++;
                    }
                }
                leastRecent[j] = 0;

                break;
            }
        }

        if (!pageFound) {
            if (frameCount < capacity) {
                frame[frameCount] = pages[i];
                leastRecent[frameCount] = 0;
                frameCount++;
            } else {
                int replaceIndex = 0;

                // Find the page with the highest least recent value
                for (int j = 0; j < frameCount; j++) {
                    if (leastRecent[j] > leastRecent[replaceIndex]) {
                        replaceIndex = j;
                    }
                }

                frame[replaceIndex] = pages[i];

                // Update least recently used index
                for (int k = 0; k < frameCount; k++) {
                    if (k != replaceIndex) {
                        leastRecent[k]++;
                    } else {
                        leastRecent[k] = 0;
                    }
                }
            }
            pageFaults++;
        }
    }

    printf("\nLRU Page Replacement Algorithm:\n");
    printf("Total page faults: %d\n", pageFaults);
}

int main() {
    int pages[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1};
    int n = sizeof(pages) / sizeof(pages[0]);
    int capacity = 3;

    lru(pages, n, capacity);

    return 0;
}
