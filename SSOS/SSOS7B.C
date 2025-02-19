#include <stdio.h>
#include <conio.h>

#define MAX 10

struct Process {
    int id;
    int arrivalTime;
    int burstTime;
    int priority;
    int startTime;
    int completionTime;
    int waitingTime;
    int turnaroundTime;
};

int main() {
    struct Process processes[MAX];
    int n, i, j;
    int totalWaitingTime = 0, totalTurnaroundTime = 0;
    int currentTime;
    struct Process temp;

    clrscr();

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter process details (arrival time, burst time, and priority):\n");
    for (i = 0; i < n; i++) {
        printf("Process ID: %d\n", i + 1);
        processes[i].id = i + 1;
        printf("Arrival Time: ");
        scanf("%d", &processes[i].arrivalTime);
        printf("Burst Time: ");
        scanf("%d", &processes[i].burstTime);
        printf("Priority (Lower value = Higher priority): ");
        scanf("%d", &processes[i].priority);
    }

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (processes[i].priority > processes[j].priority) {
                temp = processes[i];
                processes[i] = processes[j];
                processes[j] = temp;
            }
        }
    }

    currentTime = 0;

    for (i = 0; i < n; i++) {
        // If the process arrives after the current time, idle until it arrives
        if (currentTime < processes[i].arrivalTime) {
            currentTime = processes[i].arrivalTime;
        }

        processes[i].startTime = currentTime;
        processes[i].completionTime = currentTime + processes[i].burstTime;

        processes[i].waitingTime = processes[i].startTime - processes[i].arrivalTime;
        processes[i].turnaroundTime = processes[i].completionTime - processes[i].arrivalTime;

        totalWaitingTime += processes[i].waitingTime;
        totalTurnaroundTime += processes[i].turnaroundTime;

        currentTime = processes[i].completionTime;
    }

    printf("\nProcess ID\tArrival Time\tBurst Time\tPriority\tStart Time\tCompletion Time\tWaiting Time\tTurnaround Time\n");
    for (i = 0; i < n; i++) {
        printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n",
               processes[i].id,
               processes[i].arrivalTime,
               processes[i].burstTime,
               processes[i].priority,
               processes[i].startTime,
               processes[i].completionTime,
               processes[i].waitingTime,
               processes[i].turnaroundTime);
    }

    printf("\nAverage Waiting Time: %.2f\n", (float)totalWaitingTime / n);
    printf("Average Turnaround Time: %.2f\n", (float)totalTurnaroundTime / n);

    getch();
    return 0;
}
