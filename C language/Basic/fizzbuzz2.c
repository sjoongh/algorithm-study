#include <unistd.h>

int	write_num(int num)
{
	if (num > 9)
		write_num(num / 10);
	write(1, &"0123456789"[num % 10], 1);
}

int	main()
{
	int num;

	num = 1;
	while (num <= 100)
	{
		if (num % 3 == 0 && num % 5 == 0)
			write(1, "fizzbuzz", 8);
		else if (num % 3 == 0)
			write(1, "fizz", 4);
		else if (num % 5 == 0)
			write(1, "buzz", 4);
		else
			write_num(num);
		write(1, "\n", 1);
		num++;
	}
}
