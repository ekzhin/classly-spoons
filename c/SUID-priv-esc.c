#include <stdio.h>
#include <unistd.h>

int main()
{
	setuid(0);
	setgid(0);
	char *newargv[] = { NULL, "/bin/sh", NULL };
	execve("/bin/sh", newargv, NULL);
}
