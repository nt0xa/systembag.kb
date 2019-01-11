#include "IOKit.h"

IOReturn IOKit_getConnection(const char* serviceName, io_connect_t *conn) {
    IOReturn ret;

    CFMutableDictionaryRef dict = IOServiceMatching(serviceName);
    io_service_t dev = IOServiceGetMatchingService(kIOMasterPortDefault, dict);

    if (!dev) {
        return kIOReturnError;
    }

    ret = IOServiceOpen(dev, mach_task_self(), 0, conn);

    IOObjectRelease(dev);

    return ret;
}

IOReturn IOKit_call(const char      *serviceName,
                    uint32_t        selector,
                    const uint64_t  *input,
                    uint32_t        inputCnt,
                    const void      *inputStruct,
                    size_t          inputStructCnt,
                    uint64_t        *output,
                    uint32_t        *outputCnt,
                    void            *outputStruct,
                    size_t          *outputStructCnt) {
    IOReturn ret;
    io_connect_t conn = 0;

    ret = IOKit_getConnection(serviceName, &conn);

    if (ret != kIOReturnSuccess) {
        return ret;
    }

    ret = IOConnectCallMethod(conn,
                              selector,
                              input,
                              inputCnt,
                              inputStruct,
                              inputStructCnt,
                              output,
                              outputCnt,
                              outputStruct,
                              outputStructCnt);

    return ret;
}
