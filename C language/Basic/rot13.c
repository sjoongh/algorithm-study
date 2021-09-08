#include <unistd.h>
#include <stdbool.h>

bool	upper(char c)
{
	return (c >= 'A' && c <= 'Z');
}

bool	lower(char c)
{
	return (c >= 'a' && c <= 'z');
}

char	add13(char c)
{
	unsigned char ch;
	char max;

	if (lower(c))
		max = 'z';
	else
		max = 'Z';
	ch = c + 13;
	if (ch > max)
		ch -= 26;
	return (ch);
}

void	rot13(char *str)
{
	while (*str)
	{
		if (lower(*str) || upper(*str))
			*str = add13(*str);
		write(1, str, 1);
		str++;
	}
}

int	main(int argc, char *argv[])
{
	if (argc == 2)
		rot13(argv[1]);
	write(1, "\n", 1);
}
