#include "unistd.h"
#include "stdlib.h"
#include "stdio.h"

/**
 * infinite_while - function that runs forever and returns nothing
 * Return: 0 in the end
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry to a program that creates zombies
 * Return: 0
 */
int main(void)
{
	int child = 0;
	pid_t pid;

	while (child < 5)
	{
		pid = fork();
		if (pid == 0)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		child++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
