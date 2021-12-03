const int N = 4096;
byte [,] image = new byte[N, N];
public bool isDark() {
    count = 0
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < N; ++i) {
             if (image[j, i] >= 128) {
                count += 1;
            }
        }
   }
   return count < N * N / 2;
}

void sinx(int N, int terms, float* x, float* result)
{
	for (int i=0; i<N; i++)
	{
		float value = x[i];
		float numer = x[i]*x[i]*x[i];
		int denom = 6; // 3!
		int sign = -1;

		for (int j=1; j<=terms; j++)
		{
			value += sign*numer/denom;
			numer *= x[i]*x[i];
			denom *= (2*j+2) * (2*j+3);
			sign *= -1;
		}
	}

	result[i] = value;
}

void sinx(int N, int terms, float* x, float* result)
{
	for (int i=0; i<N; i++)
	{
		float value = x[i];
		float value_square = value*value;
		float numer = value_square*value;
		int denom = 6; // 3!
		int sign = -1;

		for (int j=1; j<=terms; j++)
		{
			value += sign*numer/denom;
			numer *= value_square;
			int double_j = 2*j;
			denom *= (double_j+2) * (double_j+3);
			sign *= -1;
		}
	}

	result[i] = value;
}