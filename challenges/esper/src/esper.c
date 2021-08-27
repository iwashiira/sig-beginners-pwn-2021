#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int func(){
	puts("hum...");
	sleep(3);
	return 0;
}

int check(int a, int b, int c)
{
	char string[30] = "local variable spaces";
	int number = 0;
	int ans = a*b*c + (a-b-c)*c + (a+b-c)*a*b*c*c - a*c;
	scanf("%d", &number);
	func();
	if (number!=ans) {puts("Bye"); return 1;}
	return 0;
}

int main()
{
	int a = 11, b = 100;
	int number;
	puts("This is the first step!");
	puts("Are you Esper?");
	scanf("%d", &number);
	if (number != a*b) {puts("Bye");return 0;}
	puts("This is the second step!");
	puts("Do you know Logical Operation?");
	scanf("%d", &number);
	if (number != (a&9998)+(a|129873)) {puts("Bye"); return 0;}
	puts("This is the last step!");
	puts("One more Esper check!");
	int x = 11, y = 20, z = 33;
	number = check(x, y, z);
	if (number != 0) {puts("Bye"); return 0;}
	puts("You are good at using radare2!");
	system("/bin/sh");
	return 0;
}
