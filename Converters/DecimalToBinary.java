/*Simple java function to convert decimal to Binary*/
public class decimalToBinary{
	public static void main(String args[]){
		int n = 5;
		System.out.print("Equivalent Binary: "+calcBinary(n));
	}

	private static String calcBinary(int n){
		StringBuilder binaryString = new StringBuilder();
		while(n!=0){
		binaryString.append(n%2);
		n=n/2;
	}
	binaryString = binaryString.reverse();
	return binaryString.toString();
	}
}