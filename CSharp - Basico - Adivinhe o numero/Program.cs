var numeroAletorio = new Random();
int numeroQueNinguemSabe = numeroAletorio.Next(100);
int chute = -1;
int tentativas = 0;
while (chute != numeroQueNinguemSabe)
{
    tentativas = tentativas + 1;
    Console.Clear();
    Console.WriteLine("Chute um número de 0 a 100");
    chute = Int32.Parse(Console.ReadLine());
    if(chute > numeroQueNinguemSabe)
        Console.WriteLine("Tente um número menor!");

    if(chute < numeroQueNinguemSabe) {
        Console.WriteLine("Haha looser...");
        Console.WriteLine("Tente um número maior!");
    }
    
    Console.ReadKey();
}

Console.Clear();
Console.WriteLine($"Parabéns, vc acertou em {tentativas} tentativas");