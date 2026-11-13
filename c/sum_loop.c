#include <stdio.h>

int main(void) {
    int numbers[] = {1, 2, 3, 4, 5};
    int n = 5;                 // must track length yourself
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += numbers[i];
    }

    printf("%d\n", total);     // 15
    return 0;
}
