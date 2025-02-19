#include <stdio.h>
#include <conio.h>

#define MAX_FRAMES 3
#define MAX_PAGES 10

int main() {
    int referenceString[MAX_PAGES] = {4, 7, 6, 1, 7, 6, 1, 2, 7, 2};
    int frames[MAX_FRAMES];
    int recent[MAX_FRAMES];
    int pageFaults = 0;
    int i, j, step, currentPage, pageFound, leastUsed, replaceIndex;

    clrscr();

    for (i = 0; i < MAX_FRAMES; i++) {
        frames[i] = -1;
        recent[i] = -1;
    }

    for (step = 0; step < MAX_PAGES; step++) {
        currentPage = referenceString[step];
        pageFound = 0;

        for (i = 0; i < MAX_FRAMES; i++) {
            if (frames[i] == currentPage) {
                pageFound = 1;
                recent[i] = step;
                break;
            }
        }

        if (!pageFound) {
            pageFaults++;

            leastUsed = recent[0];
            replaceIndex = 0;
            for (i = 1; i < MAX_FRAMES; i++) {
                if (recent[i] < leastUsed) {
                    leastUsed = recent[i];
                    replaceIndex = i;
                }
            }

            frames[replaceIndex] = currentPage;
            recent[replaceIndex] = step;
        }

        printf("Step %d\tReference %d\tFrames: [", step + 1, currentPage);
        for (i = 0; i < MAX_FRAMES; i++) {
            if (frames[i] != -1)
                printf("%d", frames[i]);
            else
                printf("-");
            if (i < MAX_FRAMES - 1)
                printf(", ");
        }
        printf("]\t%s\n", pageFound ? "No Page Fault" : "Page Fault");
    }

    printf("\nTotal Page Faults: %d\n", pageFaults);

    getch();
    return 0;
}
