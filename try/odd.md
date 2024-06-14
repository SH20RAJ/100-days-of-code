shaswatraj@Sh try % ollama run llama2                                               
>>> create an article of printing odd no 10 diff ways in c
Sure, here are 10 different ways to print odd numbers in C:



1. Using `printf()` function:
```c
#include <stdio.h>

int main() {
    int x = 1; // odd number
    printf("The value of x is %d\n", x);
    return 0;
}
```
2. Using `scanf()` function:
```c
#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x); // input odd number
    printf("The value of x is %d\n", x);
    return 0;
}
```
3. Using `atoi()` function:
```c
#include <stdio.h>

int main() {
    int x = atoi("10"); // odd number
    printf("The value of x is %d\n", x);
    return 0;
}
```
4. Using `strtol()` function:
```c
#include <string.h>

int main() {
    char str[] = "10"; // odd number as string
    int x = strtol(str, NULL, 10);
    printf("The value of x is %d\n", x);
    return 0;
}
```
5. Using `getchar()` function:
```c
#include <stdio.h>

int main() {
    int x = getchar(); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
6. Using `fread()` function:
```c
#include <stdio.h>

int main() {
    int x = fread(&x, sizeof(int), 1, stdin); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
7. Using `scanf_s()` function:
```c
#include <stdio.h>

int main() {
    int x;
    scanf_s("%d", &x, sizeof(x)); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
8. Using `getche()` function:
```c
#include <stdio.h>

int main() {
    int x = getche(); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
9. Using `fgetc()` function:
```c
#include <stdio.h>

int main() {
    int x = fgetc(stdin); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
10. Using `getw()` function:
```c
#include <stdio.h>

int main() {
    int x = getw(); // reads an odd number from standard input
    printf("The value of x is %d\n", x);
    return 0;
}
```
These are just a few examples of how you can print odd numbers in C. There are many other ways to do it, and the best approach will depend
on your specific use case.

>>> create an article of printing list of  odd no 10 diff ways in c