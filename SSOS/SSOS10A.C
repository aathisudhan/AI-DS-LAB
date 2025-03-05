#include <stdio.h>
#include <conio.h>
#define MAX_PARTITIONS 10
#define MAX_PROCESSES 10

// Function to allocate memory to processes using First Fit
void firstFit(int partitions[], int partitionCount, int processes[], int processCount) {
    int i, j;
    int allocation[MAX_PROCESSES];
    
    // Initially, all processes are not allocated memory
    for (i = 0; i < processCount; i++) {
        allocation[i] = -1;
    }
    
    // Assign processes to partitions
    for (i = 0; i < processCount; i++) {
        for (j = 0; j < partitionCount; j++) {
            // Find the first partition that can accommodate the process
            if (partitions[j] >= processes[i]) {
                allocation[i] = j; // Allocate the partition to the process
                partitions[j] -= processes[i]; // Reduce the partition size
                break; // Move to the next process
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
    int partitionCount, processCount, i;
    
    clrscr();
    
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
    
    // Call the first fit function to allocate memory
    firstFit(partitions, partitionCount, processes, processCount);
    
    getch();
    return 0;
}
