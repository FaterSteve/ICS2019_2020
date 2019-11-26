
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
				System.out.print("We got N! It's "+n+"\n");
			}
				//Makes sure n is greater than 2
				if(n > 2){
					//Last of the actual debugging, just says the total degrees and what the program says the angle is (plus 180 so it would line up with regular polygon angle calculator websites and make debugging easier)
					if(debug == true){
						System.out.printf("The total of all interior angles is ");
						System.out.println((180.0*(n-2.0)));
						System.out.printf("Each interior angles is "+(angle+180)+" degrees");
					}
					//runs createTurtle. It pulls the angle
					createTurtle(debug, angle, n);
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
			//pulls debug back for more fun if it's true.
			System.out.println("Pease input an integer that is greater than 2");
			getN(debug);
			
		}
	}
	//This defines the turtle that will be used in the recursion loop later
	public static void createTurtle(boolean debug, double angle, int n){
		//make/define a turtle
		Turtle bob;
		bob = new Turtle();
		System.out.println("Running...\n");
		drawSide(debug, angle, n, bob);
	}
	public static void drawSide(boolean debug, double angle, int n, Turtle bob){
		if(n>0){
			bob.speed(15);
			bob.forward(40);
			bob.left(angle);
			n--;
			//just something I wanted for fun, so I put it into the debug mode. It just says this until the program gets stopped, and it doesnt make a new line each time.
			if(debug == true){
				System.out.print("around and ");
			}
			drawSide(debug, angle, n, bob);
		}else{
			if(debug == true){
				System.out.println("around.\n");
			}
			System.out.print("Press enter to exit code");
			Scanner stop = new Scanner(System.in);
			String Stop = stop.nextLine();
			System.exit(0);
		}
	}	
}
