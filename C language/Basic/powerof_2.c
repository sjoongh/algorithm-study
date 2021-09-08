int	is_power_of_w(unsigned int n)
{
	return ((n & (-n)) == n ? 1 : 0);
}
