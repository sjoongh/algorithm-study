int	main(int *tab, unsigned int len)
{
	int	i;
	int	j;

	if (!tab)
		return (0);
	i = 0;
	while (len--)
	{
		if (tab[i] > tab[i + 1])
			j = tab[i];
		i++;
	}
	return (j);
}
