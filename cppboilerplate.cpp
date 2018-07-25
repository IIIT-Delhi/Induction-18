#include <bits/stdc++.h>
using namespace std;

// the image cannot be larger than 2000 x 2000 pixels
#define sz 2005

int red[sz][sz], green[sz][sz], blue[sz][sz];
int width, height;

void main_fun()
{
    //=========================
    // Write filter logic here
    //=========================
    for(int i=0; i<height; i++)
    {
        for(int j=0; j<width; j++)
        {
            red[i][j] = red[i][j];
            blue[i][j] = blue[i][j];
            green[i][j] = green[i][j];
        }
    }
    //=========================
    // Filter logic ends
    //=========================
}

void input_arr(int arr[][sz])
{
    // boring function to take an array as an input
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
    // boring function to output an array
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
    // First line will contain height then width
    cin>>height>>width;

    // input in the order red / green  / blue
    input_arr(red);
    input_arr(green);
    input_arr(blue);
    
    // call your filter to do it's magic !
    main_fun();
    
    // First line will contain height then width
    // output in the order red / green  / blue
    cout<<height<<" "<<width<<"\n";
    print_arr(red);
    print_arr(green);
    print_arr(blue);
    return 0;
}
