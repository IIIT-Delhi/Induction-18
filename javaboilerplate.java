import java.util.Scanner;

public class javaboilerplate {
	
	static int red[][];
	static int green[][];
	static int blue[][];
	static int width;
	static int height;
	static Scanner s;

	public static void filter()
	{
		// write your code below :
		for(int i=0; i<javaboilerplate.height; i++)
		{
			for(int j=0; j<javaboilerplate.width; j++)
			{
				javaboilerplate.red[i][j] = javaboilerplate.red[i][j];
				javaboilerplate.green[i][j] = javaboilerplate.green[i][j];
				javaboilerplate.blue[i][j] = javaboilerplate.blue[i][j];
			}
		}
	}
	
	public static void input_arr(int arr[][])
	{
		for(int i=0; i<javaboilerplate.height; i++)
		{
			for(int j=0; j<javaboilerplate.width; j++)
			{
				arr[i][j] = javaboilerplate.s.nextInt();
			}
		}
	}
	
	public static void print_arr(int arr[][])
	{
		for(int i=0; i<javaboilerplate.height; i++)
		{
			for(int j=0; j<javaboilerplate.width; j++)
			{
				System.out.print(arr[i][j]+" ");
			}
			System.out.println("");
		}
	}

	public static void main(String[] args) {
		javaboilerplate.s = new Scanner(System.in);
		red = new int[2005][2005];
		green = new int[2005][2005];
		blue = new int[2005][2005];
		
		// First line of input contains height then width
		javaboilerplate.height = javaboilerplate.s.nextInt();
		javaboilerplate.width = javaboilerplate.s.nextInt();
		
		// take input in the order red / green / blue
		javaboilerplate.input_arr(red);
		javaboilerplate.input_arr(green);
		javaboilerplate.input_arr(blue);
		
		// call your magical filter function !
		javaboilerplate.filter();
		
		// First line of output contains height then width
		System.out.println(javaboilerplate.height+ " "+javaboilerplate.width);
		
		// output the pixel values in the order red / green / blue
		javaboilerplate.print_arr(red);
		javaboilerplate.print_arr(green);
		javaboilerplate.print_arr(blue);
	}

}
