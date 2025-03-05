#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define MAX_QUEUE 100  // Fixed maximum queue size

int main() {
    int queueSize, head, i, diff, seek = 0;
    int queue[MAX_QUEUE + 1];  // Fixed-size array

    // Input the size of the queue of disk requests
    printf("Enter the size of queue request (max %d): ", MAX_QUEUE);
    scanf("%d", &queueSize);

    // Validate queue size
    if (queueSize > MAX_QUEUE || queueSize <= 0) {
	printf("Invalid queue size! Please enter a value between 1 and %d.\n", MAX_QUEUE);
	return 1; // Exit with error
    }

    // Input the queue of disk positions to be read
    printf("Enter the queue of disk positions to be read:\n");
    for (i = 1; i <= queueSize; i++) {
	scanf("%d", &queue[i]);
    }

    // Input the initial head position
    printf("Enter the initial head position: ");
    scanf("%d", &head);
    queue[0] = head; // Store head at index 0

    printf("\nDisk head movement:\n");

    // Process requests using FCFS
    for (i = 0; i < queueSize; i++) {
	diff = abs(queue[i + 1] - queue[i]);
	seek += diff;
	printf("Head moves from %d to %d, Seek time: %d\n", queue[i], queue[i + 1], diff);
    }

    // Display total and average seek time
    printf("\nTotal seek time: %d\n", seek);
    printf("Average seek time: %.2f\n", (float)seek / queueSize);

    getch(); // Wait for key press
    return 0;
}
