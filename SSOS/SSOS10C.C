#include <stdio.h>
#include <conio.h>

#define MAX_PARTITIONS 10
#define MAX_PROCESSES 10

// Function to allocate memory using Worst Fit method for fixed partitions.
void worstFit(int partitions[], int partitionCount, int processes[], int processCount) {
    int i, j, worstIndex;
    int allocation[MAX_PROCESSES]; // Stores index of partition allocated to each process
    int partitionAllocated[MAX_PARTITIONS]; // Marks if a partition has been allocated (1) or not (0)
    
    // Initialize allocations and partition status
    for (i = 0; i < processCount; i++) {
        allocation[i] = -1; // -1 indicates not allocated
    }
    for (i = 0; i < partitionCount; i++) {
        partitionAllocated[i] = 0; // 0 indicates partition is free
    }
    
    // For each process, find the worst fit partition (largest free partition that can hold it)
    for (i = 0; i < processCount; i++) {
        worstIndex = -1;
        for (j = 0; j < partitionCount; j++) {
            if (!partitionAllocated[j] && partitions[j] >= processes[i]) {
                if (worstIndex == -1 || partitions[j] > partitions[worstIndex]) {
                    worstIndex = j;
                }
            }
        }
        // If a suitable partition is found, allocate it to the process
        if (worstIndex != -1) {
            allocation[i] = worstIndex;
            partitionAllocated[worstIndex] = 1; // Mark partition as allocated
        }
    }
    
    // Display the allocation result
    printf("\nProcess No.\tProcess Size\tPartition No.\tPartition Size\tInternal Fragmentation\n");
    for (i = 0; i < processCount; i++) {
        if (allocation[i] != -1) {
            int frag = partitions[allocation[i]] - processes[i];
            // +1 is added to partition index for user-friendly numbering (1-indexed)
            printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n", i + 1, processes[i], allocation[i] + 1, partitions[allocation[i]], frag);
        } else {
            printf("%d\t\t%d\t\t%s\n", i + 1, processes[i], "Not Allocated");
        }
    }
}

int main() {
    int partitions[MAX_PARTITIONS], processes[MAX_PROCESSES];
    int partitionCount, processCount, i;
    
    clrscr(); // Clear the screen (for Turbo C++)
    
    // Input the number of partitions and their sizes
    printf("Enter the number of partitions: ");
    scanf("%d", &partitionCount);
    printf("Enter the size of each partition:\n");
    for (i = 0; i < partitionCount; i++) {
        printf("Partition %d: ", i + 1);
        scanf("%d", &partitions[i]);
    }
    
    // Input the number of processes and their sizes
    printf("\nEnter the number of processes: ");
    scanf("%d", &processCount);
    printf("Enter the size of each process:\n");
    for (i = 0; i < processCount; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d", &processes[i]);
    }
    
    // Allocate memory using Worst Fit
    worstFit(partitions, partitionCount, processes, processCount);
    
    getch(); // Wait for key press
    return 0;
}
