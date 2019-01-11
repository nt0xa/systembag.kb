#include <stdio.h>
#include <stdint.h>

#include "AppleEffaceableStorage.h"

void print_hex(uint8_t *buf, size_t len) {
    for (size_t i = 0; i < len; i++) {
        printf("%02x", buf[i]);
    }
    printf("\n");
}

int main() {
    struct BAG1Locker bag1_locker = { 0 };

    int err = AppleEffaceableStorage__getLocker(LOCKER_BAG1,
            (uint8_t*)&bag1_locker,
            sizeof(struct BAG1Locker));

    if (err) {
        fprintf(stderr, "Error: %08x", err);
        return 1;
    }

    printf("iv = ");
    print_hex(bag1_locker.iv, sizeof(bag1_locker.iv));
    printf("key = ");
    print_hex(bag1_locker.key, sizeof(bag1_locker.key));

    return 0;
}
