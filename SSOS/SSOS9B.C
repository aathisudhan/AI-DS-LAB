#include <stdio.h>
#include <conio.h>  // Turbo C requires conio.h for clrscr() and getch()
#include <stdlib.h>

void SCAN(int queue[], int n, int head, int max_range) {
    int seek_time, i, j, temp, arr[50], pos;

    clrscr(); // Clears the screen (for Turbo C)

    seek_time = 0;

    // Adding boundaries and head to the queue
    arr[0] = 0;              // Start boundary
    arr[n + 1] = max_range;  // End boundary
    arr[n] = head;           // Head position

    for (i = 0; i < n; i++) {
        arr[i + 1] = queue[i];
    }

    // Sorting the queue using Bubble Sort
    for (i = 0; i < n + 2; i++) {
        for (j = i + 1; j < n + 2; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // Finding the position of head in sorted array
    for (i = 0; i < n + 2; i++) {
        if (arr[i] == head) {
            pos = i;
            break;
        }
    }

    printf("\nSCAN Disk Scheduling:\n");

    // Moving right first
    for (i = pos; i < n + 2; i++) {
        printf("Head moves from %d to %d, Seek: %d\n", head, arr[i], abs(arr[i] - head));
        seek_time += abs(arr[i] - head);
        head = arr[i];
    }

    // Moving left after reaching max_range
    for (i = pos - 1; i >= 0; i--) {
        printf("Head moves from %d to %d, Seek: %d\n", head, arr[i], abs(arr[i] - head));
        seek_time += abs(arr[i] - head);
        head = arr[i];
    }

    // Print final results
    printf("\nTotal Seek Time: %d\n", seek_time);
    printf("Average Seek Time: %.2f\n", (float)seek_time / n);

    getch(); // Wait for keypress (needed in Turbo C)
}

int main() {
    int max_range, n, head, i;
    int queue[50];  // Fixed size array since Turbo C doesn't support dynamic memory

    clrscr(); // Clears the screen (for Turbo C)

    // Input max disk range
    printf("Enter the max range of disk: ");
    scanf("%d", &max_range);

    // Input number of requests
    printf("Enter the number of requests: ");
    scanf("%d", &n);

    // Input disk requests
    printf("Enter the queue of disk positions to be read: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &queue[i]);
    }

    // Input initial head position
    printf("Enter the initial head position: ");
    scanf("%d", &head);

    // Call SCAN algorithm
    SCAN(queue, n, head, max_range);

    return 0;
}
