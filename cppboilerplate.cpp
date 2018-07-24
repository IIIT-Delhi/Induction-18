#include <bits/stdc++.h>
using namespace std;

#define sz 2005

int red[sz][sz], green[sz][sz], blue[sz][sz];
int width, height;

void main_fun()
{
	// Write your code below:
	for(int i=0; i<height; i++)
	{
		for(int j=0; j<width; j++)
		{
			red[i][j] = 255 - red[i][j];
			blue[i][j] = 255 - blue[i][j];
			green[i][j] = 255 - green[i][j];
		}
	}
}

void input_arr(int arr[][sz])
{
	for(int i=0; i<height; i++)
	{
		for(int j=0; j<width; j++)
		{
			cin>>arr[i][j];
		}
	}
	
}
void print_arr(int arr[][sz])
{
	for(int i=0; i<height; i++)
	{
		for(int j=0; j<width; j++)
		{
			cout<<arr[i][j]<<" ";
		}
		cout<<"\n";
	}
}

int main()
{
	cin>>height>>width;
	// cerr<<height<<" "<<width;

	input_arr(red);
	input_arr(blue);
	input_arr(green);
	
	main_fun();
	
	cout<<height<<" "<<width<<"\n";
	print_arr(red);
	print_arr(blue);
	print_arr(green);
	return 0;
}
