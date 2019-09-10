#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_DOUBLES 	5.0

// ieee754 rpresentations of the double numbers we want
#define TARGET_QUOTIENT  	0x5e2ef31e17a186eb
#define SHELLCODE_SUM		0x5e535300601500bc

/*
	Sum of shellcode bytes = 0x5e535300601500bc
	Sum of the shellcode bytes + 2.4130147898742321e+143 = 0x5e5357f2cec526e1

	Divided by 6: 0x5e2ef31e17a1d7ce

	Target quotient: 0x5e2ef31e17a18eeb
*/

// resets a double's value by setting its IEEE754 representation
void set_double(double *d, unsigned long long new_double);

// prints the IEEE754 representation of the double value to the screen
void show_double(double d);

int main(void)
{
	double shellcode_sum = 0;

	set_double(&shellcode_sum, SHELLCODE_SUM);
	printf("\nSum of shellcode bytes: \n");
	show_double(shellcode_sum);

	// set the target quotient and the sum we want
	double new_quotient = 0;
	double new_sum = 0;
	set_double(&new_quotient, TARGET_QUOTIENT);
	printf("\nTarget quotient: \n");
	show_double(new_quotient);

	new_sum = new_quotient * NUMBER_OF_DOUBLES;
	printf("\nTarget sum: \n");
	show_double(new_sum);

	// subtract the oldsum from the newsum
	double next_double = new_sum - shellcode_sum;
	printf("\nNext double: \n%e\n", next_double);
	show_double(next_double);

	// verifying we can get the target quotient back
	double q = (next_double + shellcode_sum) / NUMBER_OF_DOUBLES;
	printf("\nVerifying target quotient: \n");
	show_double(q);

	return 0;
}

void set_double(double *d, unsigned long long new_double)
{
	*(unsigned long long *)d = new_double;
}

void show_double(double d)
{
	printf("[IEEE754 Representation]: 0x%lx\n", *(unsigned long long *)&d);
}
