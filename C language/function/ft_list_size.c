#include "ft_list.h"

void		

int	main(int argc, char const *argv[])
{
	int i;
	int j;

	i = 0;
	j = 0;
	if (argc == 2)
	{
		while (argv[2][j])
		{
			if (argv[1][i] == argv[2][j++])
				i++;
			if (!argv[1][i])
				ft_putstr(argv[1]);
		}
	}
}
