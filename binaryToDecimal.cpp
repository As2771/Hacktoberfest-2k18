#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int binaryToDecimal(string binary){

	int decimal = 0;
	int len = binary.length() - 1;
	
	for(int i = 0; binary[i] != '\0'; i++){
		if(binary[i] == '1')decimal += pow(2, len-i);
	}
	
	return decimal;

}

int main(){

	string binary;
	int decimal;
	
	cout << "Enter Binary String : ";
	cin >> binary;
	
	cout << binaryToDecimal(binary) << endl;
	
	return 0;

}
