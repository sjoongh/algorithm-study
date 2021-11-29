#include <unistd.h>

int	main(int argc, char *argv[])
{
	int i;
	char ch;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			ch = argv[1][i];
			if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
				ch = 'Z' - argv[1][i] + 'A';
			if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
				ch = 'z' - argv[1][i] + 'a';
			write(1, &ch, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
