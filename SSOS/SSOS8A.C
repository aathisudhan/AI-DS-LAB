#include <stdio.h>
#include <conio.h>

int main() {
    int incomingStream[] = {4, 1, 2, 4, 5};
    int pageFaults = 0;
    int frames = 3;
    int m, n, s, pages;
    int temp[3];

    clrscr();

    pages = sizeof(incomingStream) / sizeof(incomingStream[0]);

    printf("Incoming \t Frame 1 \t Frame 2 \t Frame 3\n");

    for (m = 0; m < frames; m++) {
        temp[m] = -1;
    }

    for (m = 0; m < pages; m++) {
        s = 0;

        for (n = 0; n < frames; n++) {
            if (incomingStream[m] == temp[n]) {
                s = 1; // Page hit
                break;
            }
        }

        if (s == 0) {
            temp[pageFaults % frames] = incomingStream[m];
            pageFaults++;
        }

        printf("%d\t\t", incomingStream[m]);
        for (n = 0; n < frames; n++) {
            if (temp[n] != -1)
                printf("%d\t\t", temp[n]);
            else
                printf("-\t\t");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults: %d\n", pageFaults);

    getch();
    return 0;
}
