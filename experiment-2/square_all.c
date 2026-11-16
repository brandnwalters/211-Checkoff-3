#include <stddef.h>

void square_all(double *values, size_t count)
{
    for (size_t i = 0; i < count; i++)
    {
        values[i] *= values[i];
    }
}