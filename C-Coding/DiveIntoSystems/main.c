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

    char str[50];

    printf("Enter your name: ");
    scanf("%s", &str);

    printf("Your name is: %s\n", str);

    int x;
    float pi;

    printf("Enter an int and a float: ");
    scanf("%d%g", &x, &pi);
    printf("An int is: %d\nA float is: %g", x, pi);


    return 0;
} 