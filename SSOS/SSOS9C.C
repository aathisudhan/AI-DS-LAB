#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

void CSCAN(int *queue, int n, int head, int max_range) {
    int seek_time = 0, i, j, temp, pos;
    
    // Dynamically allocate memory for arr
    int *arr = (int *)malloc((n + 2) * sizeof(int));

    arr[0] = head;
    arr[n + 1] = max_range; // End boundary
    for (i = 1; i <= n; i++) {
        arr[i] = queue[i - 1];
    }

    // Sorting the queue
    for (i = 0; i < n + 2; i++) {
        for (j = i + 1; j < n + 2; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // Find position of head in sorted array
    for (i = 0; i < n + 2; i++) {
        if (arr[i] == head) {
            pos = i;
            break;
        }
    }

    printf("\nC-SCAN Disk Scheduling:\n");

    // Moving right
    for (i = pos; i < n + 2; i++) {
        printf("Disk head moves from %d to %d with seek %d\n", head, arr[i], abs(arr[i] - head));
        seek_time += abs(arr[i] - head);
        head = arr[i];
    }

    // Jump to start of the disk (0)
    printf("Disk head jumps from %d to 0 with seek %d\n", head, head);
    seek_time += head;
    head = 0;

    // Moving right again
    for (i = 0; i < pos; i++) {
        printf("Disk head moves from %d to %d with seek %d\n", head, arr[i], abs(arr[i] - head));
        seek_time += abs(arr[i] - head);
        head = arr[i];
    }

    printf("Total seek time is %d\n", seek_time);
    printf("Average seek time is %.6f\n", (float)seek_time / n);

    // Free dynamically allocated memory
    free(arr);
}

int main() {
    int max_range, n, head, i;

    // Dynamically allocate memory for queue
    int *queue = (int *)malloc(n * sizeof(int));
    
    printf("Enter the max range of disk: ");
    scanf("%d", &max_range);

    printf("Enter the size of queue request: ");
    scanf("%d", &n);

    printf("Enter the queue of disk positions to be read: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &queue[i]);
    }

    printf("Enter the initial head position: ");
    scanf("%d", &head);

    CSCAN(queue, n, head, max_range);

    // Free dynamically allocated memory
    free(queue);

    getch(); // To hold the console screen
    return 0;
}
