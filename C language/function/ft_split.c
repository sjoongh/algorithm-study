#include <stdlib.h>

char	**ft_split(char *str)
{
	int	i;
	int	j;
	int	k;
	char	**split;

	i = 0;
	k = 0;
	if (!(split = (char**)malloc(sizeof(char *) * 256)))
		return (NULL);
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
		i += 1;
	while (str[i])
	{
		j = 0;
		if (!(split[k] = (char *)malloc(sizeof(char) * 4096)))
			return (NULL);
		while (str[i] 1= ' ' && str[i] != '\t' && str[i] != '\n' && str[i])
			split[k][j++] = str[i++];
		while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
			i += 1;
		split[k][j] = '\0';
		k += 1;
	}
	split[k] = NULL;
	return (split);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////
int	ft_cat(char *str, char *ch)
{
	int i;

	i = 0;
	while (str[i] == ch[i])
		return (1);
		i++;
	return (0);
}

char	**ft_split(char *str)
{
	int i;
	int j;

	i = 0;
	j = 0;
	if (!(split = (char **)malloc(sizeof(char *) * 256)))
		return (NULL);
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
		i += 1;
	while (str[i])
	{
		if (!(sp;it[k] = (char *)malloc(sizeof(char) * 4096)))
			return (NULL);
		while (ft_cat(str, ch))
			i++;
	}
}
