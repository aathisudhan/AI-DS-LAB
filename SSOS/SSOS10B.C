#include <stdio.h>
#include <conio.h>

#define MAX_PARTITIONS 10
#define MAX_PROCESSES 10

// Function to allocate memory to processes using Next Fit
void nextFit(int partitions[], int partitionCount, int processes[], int processCount) {
    int allocation[MAX_PROCESSES];
    int lastAllocated;
    int i, j, found;
    
    lastAllocated = -1; // Tracks the last allocated partition
    
    // Initially, all processes are not allocated memory
    for (i = 0; i < processCount; i++) {
        allocation[i] = -1;
    }
    
    // Assign processes to partitions using Next Fit
    for (i = 0; i < processCount; i++) {
        found = 0;
        
        // Start the search from the last allocated partition
        for (j = lastAllocated + 1; j < partitionCount; j++) {
            if (partitions[j] >= processes[i]) {
                allocation[i] = j; // Allocate the partition to the process
                partitions[j] -= processes[i]; // Reduce the partition size
                lastAllocated = j; // Update the last allocated partition
                found = 1;
                break;
            }
        }
        
        // If no partition was found, loop back to the beginning
        if (!found) {
            for (j = 0; j <= lastAllocated; j++) {
                if (partitions[j] >= processes[i]) {
                    allocation[i] = j;
                    partitions[j] -= processes[i];
                    lastAllocated = j;
                    break;
                }
            }
        }
    }
    
    // Display the allocation results
    printf("\nProcess No.\tProcess Size\tPartition No.\tPartition Size Left\n");
    for (i = 0; i < processCount; i++) {
        if (allocation[i] != -1) {
            printf("%d\t\t%d\t\t%d\t\t%d\n", i + 1, processes[i], allocation[i] + 1, partitions[allocation[i]]);
        } else {
            printf("%d\t\t%d\t\tNot Allocated\n", i + 1, processes[i]);
        }
    }
}

int main() {
    int partitions[MAX_PARTITIONS], processes[MAX_PROCESSES];
    int partitionCount, processCount;
    int i;
    
    clrscr(); // Clear screen for Turbo C++
    
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
    
    // Call the Next Fit function to allocate memory
    nextFit(partitions, partitionCount, processes, processCount);
    
    getch(); // Wait for user input before exiting
    return 0;
}
