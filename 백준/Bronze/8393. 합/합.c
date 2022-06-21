#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, hap = 0;
	scanf("%d", &a);

	for (int i = 1; i <= a; i++) {
		hap += i;
	}
	printf("%d", hap);
	return 0;
}