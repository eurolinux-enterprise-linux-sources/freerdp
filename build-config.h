#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "build-config-32.h"
#elif __WORDSIZE == 64
#include "build-config-64.h"
#else
#error "Unknown word size"
#endif
