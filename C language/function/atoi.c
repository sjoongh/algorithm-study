int	ft_atoi(char *str)
{
	int n;
	int minus;

	n = 0;
	minus = 1;
	while ((*str >= 9 && *str <= 13) || *str == ' ')
		str++;
	while (*str == '+' || *str == '-')
	{
		if (*str++ == '-')
			minus *= -1;
	}
	while (*str)
	{
		if (!(*str >= '0' && *str <= '9'))
			return (n);
		n = ((n * 10) + (minus * ((*str++) - '0')));
	}
	return (n);
}

///////////////////////////////////////////////
int	ft_atoi(char *str)
{
	int i;
	int minus;

	i = 0;
	minus = 1;
	while ((*str >= 9 && *str <= 13) || *str == ' ')
		str++;
	if (*str++ == '-')
		minus *= -1;
	while (*str)
	{
		while (!(*str >= '0' && *str <= '9'))
			return (i);
		i = (i * 10) + (minus * (*str++) - '0');
	}
	return (i);
}
