#include <stdio.h>
#include <conio.h>  // Required for getch()

#define MAX_PARTITIONS 10
#define MAX_PROCESSES 10

// Function to allocate memory using Best Fit method for fixed partitions.
void bestFit(int partitions[], int partitionCount, int processes[], int processCount) {
    int allocation[MAX_PROCESSES]; // Stores index of partition allocated to each process
    int used[MAX_PARTITIONS]; // Marks if a partition is allocated (1) or free (0)
    int i, j, bestIdx, frag;

    // Initialize allocations and partition usage status
    for (i = 0; i < processCount; i++) {
        allocation[i] = -1; // -1 indicates not allocated
    }
    for (i = 0; i < partitionCount; i++) {
        used[i] = 0; // 0 indicates partition is free
    }

    // For each process, find the best fit partition
    for (i = 0; i < processCount; i++) {
        bestIdx = -1;

        // Scan through all partitions to find the smallest partition that is big enough
        for (j = 0; j < partitionCount; j++) {
            if (!used[j] && partitions[j] >= processes[i]) {
                if (bestIdx == -1 || partitions[j] < partitions[bestIdx]) {
                    bestIdx = j;
                }
            }
        }

        // If a suitable partition is found, allocate it to the process and mark it as used
        if (bestIdx != -1) {
            allocation[i] = bestIdx;
            used[bestIdx] = 1;
        }
    }

    // Display the allocation results
    printf("\nProcess No.\tProcess Size\tPartition No.\tPartition Size\tInternal Fragmentation\n");
    for (i = 0; i < processCount; i++) {
        if (allocation[i] != -1) {
            frag = partitions[allocation[i]] - processes[i];
            // Adding 1 to partition index for user-friendly (1-indexed) numbering
            printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n",
                   i + 1, processes[i], allocation[i] + 1, partitions[allocation[i]], frag);
        } else {
            printf("%d\t\t%d\t\t%s\n", i + 1, processes[i], "Not Allocated");
        }
    }
}

int main() {
    int partitions[MAX_PARTITIONS], processes[MAX_PROCESSES];
    int partitionCount, processCount, i;

    clrscr();  // Clear the screen (for Turbo C++)
    
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

    // Allocate memory using Best Fit
    bestFit(partitions, partitionCount, processes, processCount);

    getch();  // Wait for user input before closing the program
    return 0;
}
