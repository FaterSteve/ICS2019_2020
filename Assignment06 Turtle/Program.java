
import java.lang.*;
import java.util.Scanner;

public class Program{
	//Main Program runner. It is also used to get user input for enabling debug
	public static void main(String[] args){
		//This scanner is for debug info
		Scanner in = new Scanner(System.in);
		//Default debug is false
		boolean debug = false;
		//Asks if you want to run in debug mode
		System.out.println("Would you like to run in debug mode? Y/N");
		//Recieves a character input
		Character bugger = in.next().charAt(0);
		//If character input is Y or y debug is changed to true
		if((bugger.equals('Y'))||(bugger.equals('y'))){
			debug = true;
		}
		//States what the debug state is (True/False)
		System.out.printf("boolean debug is ");
		System.out.println(debug);
		//Goes into getN and brings boolean debug with it
		getN(debug);
	}
	//Gets the n variable (number of sides the polygon will have) and calculates the angle
	public static void getN(boolean debug){
		//A try so that if something goes wrong, I've got a recursion loop to meet the requirements of the assignment!
		try{
			//I'm not sure if I needed a new scanner, but I made one anyways and it is named something different. That makes it ok.
			Scanner in = new Scanner(System.in);
			//ask for and recieve the number of sides, will throw an exception if not an int. I used nextInt, so things like "7 is a lucky number!" work. I just do stuff like that for fun when I am testing.
			System.out.printf("\nThe number of sides to the regular polygon will be: ");
			int n = in.nextInt();
			//calculate the angle the turtle must turn each time. It is a double.
			double angle = (180-((180.0*(n-2.0))/n));
			//hopefully prints the same number you typed in if in debug mode 
			if(debug == true){
				System.out.printf("We got N! It's ");
				System.out.println(n);
			}
				//Makes sure n is greater than 2
				if(n > 2){
					//Last of the actual debugging, just says the total degrees and what the program says the angle is (plus 180 so it would line up with regular polygon angle calculator websites and make debugging easier)
					if(debug == true){
						System.out.printf("The total of all interior angles is ");
						System.out.println((180.0*(n-2.0)));
						System.out.printf("Each interior angles is ");
						System.out.println(angle+180);
					}
					//runs drawSide. It pulls the angle.
					drawSide(debug, angle);
				}
				//If n is less than or equal to 2 it throws an exception, hits the catch, and does some recursion
				else{
					throw new Exception();
				}
		}
		catch(Exception e){
			//While I was debugging I just dicided to run with this, then I added the second part later.
			if(debug == true){
				System.out.println("\nHouston, we have a problem.");
			}
			//RECURSION LOOP IF INT NOT ENTERED OR IF INT IS LESS THAN OR EQUAL TO 2 also pulls debug back for more fun in the sun.
			System.out.println("Pease input an integer that is greater than 2");
			getN(debug);
			
		}
	}
	//This draws a regualr polygon with n sides
	public static void drawSide(boolean debug, double angle){
		//I only made this so I could compile, it makes the program think it can escape the while loop. Remember, there is a recursion loop above, it is just kind of optional.
		boolean oneSide = false;
		//make/define a turtle
		Turtle bob;
		bob = new Turtle();
		//Draw a turtle side over and over over and over and over...
		System.out.println("Running...");
		while(true){
			bob.speed(15);
			bob.forward(40);
			bob.left(angle);
			//just something I wanted for fun, so I put it into debug mode. It just says this until the program gets stopped, and it doesnt make a new line each time.
			if(debug == true){
				System.out.printf("around and ");
			}
				if (oneSide == true)
					break;
		}
	}
}
