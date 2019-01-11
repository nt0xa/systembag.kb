#include <IOKit/IOKit.h>

IOReturn IOKit_getConnection(const char *serviceName, io_connect_t *conn);

IOReturn IOKit_call(const char      *serviceName,
                    uint32_t        selector,
                    const uint64_t  *input,
                    uint32_t        inputCnt,
                    const void      *inputStruct,
                    size_t          inputStructCnt,
                    uint64_t        *output,
                    uint32_t        *outputCnt,
                    void            *outputStruct,
                    size_t          *outputStructCnt);
