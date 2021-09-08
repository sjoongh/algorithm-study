#include <unistd.h>

char	*rev_print(char *str)
{
	int i;
	int size;

	i = 0;
	while (str[size])
		size++;
	while (i < size)
	{
		write(1, &str[size - i - 1], 1);
		i++;
	}
	return (str);
}

#include <stdio.h>

int	main()
{
	char a[10] = "abcd";
	char b;
	b = *rev_print(a);
	printf("%d", b);
}
