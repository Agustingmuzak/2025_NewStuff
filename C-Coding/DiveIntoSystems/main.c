#include <stdio.h>

int main(void) {
/*     printf("My name is: %s, Info: \n", "Agustin");
    printf("\tAge: %d \t Ht: %g\n", 20, 5.9);
    printf("\tYear: %d \t Dorm: %s", 4, "East");

    char ch;
    ch = 'A';

    printf("\nch value is %d which is the ASCII value of %c\n", ch, ch);

    ch = 99;
    printf("\nch value is %d which is the ASCII value of %c\n", ch, ch); */

/*     int num1, num2;

    printf("Enter a number: ");
    scanf("%d", &num1);
    printf("\nEnter another number: ");
    scanf("%d", &num2);

    printf("\n%d + %d = %d", num1, num2, (num1+num2)); */

/*     char str[50];

    printf("Enter your name: ");
    scanf("%s", &str);

    printf("Your name is: %s\n", str);

    int x;
    float pi;

    printf("Enter an int and a float: ");
    scanf("%d%g", &x, &pi);
    printf("An int is: %d\nA float is: %g", x, pi);
 */
/* 
    int num1, num2;

    printf("Enter your first number: ");
    scanf("%d", &num1);

    printf("Enter your second number: ");
    scanf("%d", &num2);

    if (num1 > num2) {
        printf("%d is biggest", num1);
        num2 = num1;
    } else if (num2 > num1 || num1 == num2) {
        printf("%d is biggest or %d and %d are the same number", num2, num1, num2);
        num1 = num2;
    } */
    

    int num1, num2;

    /* printf("Enter a number: ");
    scanf("%d", &num1);

    while (num1 < num2) {
        printf("%d\n", num1);
        num1 = num1 + 1;
    } */

    printf("Choose a number: ");
    scanf("%d", &num2);

    for (num1 = 0; num1 < num2; num1++) {
        printf("%d\n", num1);
    }


    return 0;
} 