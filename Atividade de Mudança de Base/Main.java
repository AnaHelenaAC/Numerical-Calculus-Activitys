import java.util.Scanner;

public class Main {

    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);

        //---------------------------------------------------------
        // Teste Seção 5, converter da base x para decimal

        System.out.println("=== Teste do Algoritmo 1 (Base β -> Decimal) ===");

        long res1_1 = MudancaDeBase.paraDecimal("1101", 2);
        System.out.println("Teste (1101)_2   -> Resultado: " + res1_1 + " | Esperado: 13");

        long res1_2 = MudancaDeBase.paraDecimal("2F", 16);
        System.out.println("Teste (2F)_16    -> Resultado: " + res1_2 + " | Esperado: 47");

        long res1_3 = MudancaDeBase.paraDecimal("377", 8);
        System.out.println("Teste (377)_8    -> Resultado: " + res1_3 + " | Esperado: 255");

        long res1_4 = MudancaDeBase.paraDecimal("Z", 36);
        System.out.println("Teste (Z)_36     -> Resultado: " + res1_4 + " | Esperado: 35");

        long res1_5 = MudancaDeBase.paraDecimal("0", 5);
        System.out.println("Teste (0)_5      -> Resultado: " + res1_5 + " | Esperado: 0");


        //---------------------------------------------------------
        // Teste Seção 5, converter de decimal para a base x

        System.out.println("\n=== Teste do Algoritmo 2 (Decimal -> Base β) ===");

        String res2_1 = MudancaDeBase.deDecimal(45, 2);
        System.out.println("Teste 45 (β=2)   -> Resultado: " + res2_1 + " | Esperado: 101101");

        String res2_2 = MudancaDeBase.deDecimal(255, 16);
        System.out.println("Teste 255 (β=16) -> Resultado: " + res2_2 + " | Esperado: FF");

        String res2_3 = MudancaDeBase.deDecimal(0, 7);
        System.out.println("Teste 0 (β=7)    -> Resultado: " + res2_3 + " | Esperado: 0");

        String res2_4 = MudancaDeBase.deDecimal(1000, 36);
        System.out.println("Teste 1000 (β=36)-> Resultado: " + res2_4 + " | Esperado: RS");


        //---------------------------------------------------------
        // Sugestão da Seção 5, converter usando os mesmos números

        System.out.println("\n=== Teste em Composição (Seção 5) ===");

        long numeroOriginal = 1000;
        int base = 36;

        String emBase36 = MudancaDeBase.deDecimal(numeroOriginal, base);
        long deVoltaParaDec = MudancaDeBase.paraDecimal(emBase36, base);

        System.out.println("Original: " + numeroOriginal + " -> Base " + base + ": " + emBase36 + " -> Voltou para Dec: " + deVoltaParaDec);

        scanner.close();
    }
}