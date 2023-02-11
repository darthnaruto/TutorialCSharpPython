Console.BackgroundColor = ConsoleColor.DarkRed;
Console.ForegroundColor = ConsoleColor.White;
Console.WriteLine("Qual é o seu nome ?");
var resultadoDaLeitura = Console.ReadLine();
Console.WriteLine($"Olá {resultadoDaLeitura}");
Console.BackgroundColor = ConsoleColor.Black;
Console.ReadKey();