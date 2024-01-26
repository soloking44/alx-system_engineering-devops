#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - It sets up an infinite while loop.
 *
 * Return: Always 0.
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
 * create_process - It generates a new process and \
 * outputs the PID of the new process.
 */
void create_process(void)
{
	int rc = fork();

	if (rc == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	create_process();
	create_process();
	create_process();
	create_process();
	create_process();
	return (infinite_while());
}
