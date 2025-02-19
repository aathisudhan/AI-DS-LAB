#include <stdio.h>
#include <conio.h>

void waitingtime(int n, int burst_time[], int wait_time[]) {
    int i;
    wait_time[0] = 0;

    for (i = 1; i < n; i++) {
        wait_time[i] = burst_time[i - 1] + wait_time[i - 1];
    }
}

void turnaroundtime(int n, int burst_time[], int wait_time[], int tat[]) {
    int i;
    for (i = 0; i < n; i++) {
        tat[i] = burst_time[i] + wait_time[i];
    }
}

void avgtime(int n, int burst_time[]) {
    int wait_time[10], tat[10];  
    int total_wt = 0, total_tat = 0;  
    int i;  

    waitingtime(n, burst_time, wait_time);

    turnaroundtime(n, burst_time, wait_time, tat);

    printf("Processes  Burst Time  Waiting Time  Turnaround Time\n");

    for (i = 0; i < n; i++) {
        total_wt += wait_time[i];
        total_tat += tat[i];
        printf("   %d \t\t %d \t\t %d \t\t %d\n", i + 1, burst_time[i], wait_time[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", (float)total_wt / n);
    printf("\nAverage Turnaround Time = %.2f", (float)total_tat / n);
}

int main() {
    int n = 3;
    int burst_time[] = {5, 8, 12};

    clrscr();
    avgtime(n, burst_time);

    getch();
    return 0;
}
