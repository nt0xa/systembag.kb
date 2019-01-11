#include <stdint.h>

#include "IOKit.h"
#include "AppleEffaceableStorage.h"

int AppleEffaceableStorage__getLocker(uint32_t lockerId, uint8_t *buffer, size_t len) {
    uint64_t outScalar = 0;
    uint32_t one = 1;
    uint64_t inScalar = lockerId;

    return IOKit_call("AppleEffaceableStorage",
            kAppleEffaceableStorageGetLocker,
            &inScalar,
            1,
            NULL,
            0,
            &outScalar,
            &one,
            buffer,
            &len);
}
