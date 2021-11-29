#include <unistd.h>

void	ft_putnbr(int nb)
{
	if (nb > 9)
	{}
}

int	main(int ac, char **av)
{
	(void) av;
	ac--;
	ft_putnbr(ac);
	ft_putchar('\n');
	return (0);
}
