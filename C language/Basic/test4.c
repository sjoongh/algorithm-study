#include <stdio.h>
#include <string.h>

int	main()
{
	int num, count = 0;
	
	int alpha[101];
	
	int ch[101] = 0;

	scanf_s("%d", &num);

	ch = ((*char)malloc(sizeof(char) * num));
	
	for (int i = 0; i < num; i++)
	{
		scanf("%s", &alpha);
		strcat(ch, alpha);
	}
	
	for (int i = 0; i < ch; i++)
	{
		printf("%s", ch);
	}
	return 0;
}
