import java.util.Scanner;

public class JavaBoilerPlate {
	
	// stores the width of the image being processed
	private int width;
	// stores the height of the image being processed
	private int height;

	// stores the red component of pixels of the image.
	// will = new int[height][width]
	private int red[][];

	// similar to above but for green component
	private int green[][];

	// similar to above but for blue component
	private int blue[][];

	private Scanner s;

	public JavaBoilerPlate() {
		this.s = new Scanner(System.in);
		
		// First line of input contains height then width
		this.height = s.nextInt();
		this.width = s.nextInt();

		// takes input in order red, green, blue
		this.red = input_arr();
		this.green = input_arr();
		this.blue = input_arr();
	
	}


	public void filter() {
		/**
		 * Write your code here:
		 * 
		 * Inputs: 
		 * 
		 * int red[][] - stores red component of the image
		 * int green[][] - stores green component of the image
		 * int blue[][] - stores blue component of the image
		 * int height - height of the image
		 * int width - width of the image
		 * 
		 * Outputs:
		 * 
		 * Modify `red`, `green` and `blue` itself.
		 * 
		 * 
		 * Note: The current code leaves the image unchanged
		 */

		//=========================
        // Write filter logic here
        //=========================
		for(int i=0; i<height; i++){
			for(int j=0; j<width; j++){
				red[i][j] = red[i][j];
				green[i][j] = green[i][j];
				blue[i][j] = blue[i][j];
			}
		}
		//=========================
        // Filter logic ends here
        //=========================
	}
	
	public int[][] input_arr() {

		int arr[][] = new int[height][width];

		for(int i=0; i<height; i++){
			for(int j=0; j<width; j++){
				arr[i][j] = s.nextInt();
			}
		}

		return arr;
	}
	
	public void print_arr(int arr[][]) {
		for(int i=0; i< height; i++) {
			for(int j=0; j< width; j++){
				System.out.print(arr[i][j]+" ");
			}
			System.out.println("");
		}
	}

	public void print_all(){
		print_arr(red);
		print_arr(green);
		print_arr(blue);
	}

	public static void main(String[] args) {

		// You need not worry about this
		// This will take in the input from console 
		// and allocate the arrays red[][], green[][] and blue[][] 
		// with proper pixel values as given in the console.
		JavaBoilerPlate obj = new JavaBoilerPlate();
		
		/**
		 * Call your magical filter function!
		*/
		obj.filter();
		
		//DO NOT REMOVE ANYTHING BELOW. The output is used for forming and displaying the image
	
		// First line of output contains height then width
		System.out.println(obj.height+ " "+obj.width);
		
		// output the pixel values in the order red / green / blue
		obj.print_all();
		
	}

}
