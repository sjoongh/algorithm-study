#include <stdlib.h>

int	*ft_range(int start, int end)
{
	int i;
	int *ch;

	if (min >= max)
		return (0);
	if ((ch = (int*)malloc(sizeof(int) * (max - min))) == 0)
		return (0);
	i = 0;
	while (min < max)
	{
		ch[i] = min;
		min++;
		i++;
	}
	return (ch);
}
