#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main() {
    float a, b;
    char c[12];
    float result=0;
    
    printf("Enter Any two numbers(a,b): ");
    scanf("%f,%f", &a,&b);
    printf("Enter operation to be performed: \n 1. divide\n 2. multiply\n 3. add \n 4. subtract\n");
    scanf("%s", c);

    // Operation
     if (strcmp(c, "divide") == 0) {
        if (b == 0) {
            printf("Error: Cannot divide by zero\n");
        } else {
            result = result + (a / b);
            printf("Result is %f\n", result);
        }
     }  
     else if (strcmp(c, "multiply") == 0) {
        result = result + (a * b);
        printf("Result is %f\n", result);
    }
     else if (strcmp(c, "add") == 0) {
        result = result + (a + b);
        printf("Result is %f\n", result);
    }
     else if (strcmp(c, "subtract") == 0) {
        result = result + (abs(a - b));
        printf("Result is %f\n", result);
    } 
     else {
        printf("Invalid operation\n");
    }

    return 0;
}

