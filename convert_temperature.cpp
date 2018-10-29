#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

class	Convert
{
public:
	Convert();
	~Convert();
	int	convertFahrenheitToCelsius(void);
	int	convertCelsiusToFahrenheit(void);
	int	parseString(std::string str);
	float		temperature;
	std::string	scale;
};

Convert::Convert()
{}

Convert::~Convert()
{}

int	Convert::parseString(std::string str)
{
	std::size_t	value;

	temperature = std::stof(str);
	value = str.find("Celsius");
	if (value != std::string::npos)
		scale = "Celsius";
	value = str.find("Fahrenheit");
	if (value != std::string::npos)
		scale = "Fahrenheit";
	return 0;
}

int	Convert::convertFahrenheitToCelsius(void)
{
	double	res = 0;

	res = 5.0 / 9.0 * (temperature - 32);
	std::cout << std::setw(16) << std::fixed << std::setprecision(3) <<
		res << std::setw(16) << "Celsius" << std::endl;
	return 0;
}

int	Convert::convertCelsiusToFahrenheit(void)
{
	float	res = 0;

	res = temperature * 9.0 / 5.0 + 32;
	std::cout << std::setw(16) << std::fixed << std::setprecision(3) <<
		res << std::setw(16) << "Fahrenheit" << std::endl;
	return 0;
}

int	main()
{
	Convert conv;
	std::string line;

	while (getline(std::cin, line)) {
		conv.parseString(line);
		if(conv.scale == "Celsius")
			return (conv.convertCelsiusToFahrenheit());
		if(conv.scale == "Fahrenheit")
			return (conv.convertFahrenheitToCelsius());
		else
			return 0;
	}
	return 0;
}
