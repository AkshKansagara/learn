#include <stdio.h>
#include <stdbool.h>

#define MAX_FRAMES 10

void fifo(int pages[], int n, int capacity)
{
    int frame[MAX_FRAMES], frameCount = 0, pageFaults = 0;
    int front = 0, rear = 0;

    for (int i = 0; i < n; i++)
    {
        bool pageFound = false;

        // Check if the page is already in the frame
        for (int j = 0; j < frameCount; j++)
        {
            if (frame[j] == pages[i])
            {
                pageFound = true;
                break;
            }
        }

        if (!pageFound)
        {
            if (frameCount < capacity)
            {
                frame[frameCount++] = pages[i];
            }
            else
            {
                frame[front] = pages[i];
                front = (front + 1) % capacity;
            }
            pageFaults++;
        }
    }

    printf("FIFO Page Replacement Algorithm:\n");
    printf("Total page faults: %d\n", pageFaults);
}

void optimal(int pages[], int n, int capacity)
{
    int frame[MAX_FRAMES], frameCount = 0, pageFaults = 0;
    int nextUse[MAX_FRAMES];

    for (int i = 0; i < n; i++)
    {
        bool pageFound = false;

        // Check if the page is already in the frame
        for (int j = 0; j < frameCount; j++)
        {
            if (frame[j] == pages[i])
            {
                pageFound = true;
                break;
            }
        }

        if (!pageFound)
        {
            if (frameCount < capacity)
            {
                frame[frameCount++] = pages[i];
            }
            else
            {
                int farthest = i + 1;
                int replaceIndex = 0;

                for (int j = 0; j < frameCount; j++)
                {
                    int k;
                    for (k = i + 1; k < n; k++)
                    {
                        if (frame[j] == pages[k])
                        {
                            if (k > farthest)
                            {
                                farthest = k;
                                replaceIndex = j;
                            }
                            break;
                        }
                    }
                    if (k == n)
                    {
                        replaceIndex = j;
                        break;
                    }
                }

                frame[replaceIndex] = pages[i];
            }
            pageFaults++;
        }
    }

    printf("\nOPTIMAL Page Replacement Algorithm:\n");
    printf("Total page faults: %d\n", pageFaults);
}

int main()
{
    int pages[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1};
    int n = sizeof(pages) / sizeof(pages[0]);
    int capacity = 3;

    fifo(pages, n, capacity);
    optimal(pages, n, capacity);

    return 0;
}
// hello how are you i am writing this comment to test github learnning 