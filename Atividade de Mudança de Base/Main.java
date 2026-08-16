import java.util.Scanner;

public class Main {

    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);

        //---------------------------------------------------------
        // Teste Seção 5, converter da base x para decimal

        System.out.println("\n------ Teste do Algoritmo 1 (Base beta para Decimal) ------");

        // Teste 1: Converter (1101)_2 para decimal
        long res1_1 = MudancaDeBase.paraDecimal("1101", 2);
        String status1_1 = (res1_1 == 13) ? "PASSOU |" : "FALHOU |";
        System.out.println(status1_1 + " Teste (1101)_2   | Esperado: 13" + "  | Resultado: " + res1_1);

        // Teste 2: Converter (2F)_16 para decimal
        long res1_2 = MudancaDeBase.paraDecimal("2F", 16);
        String status1_2 = (res1_2 == 47) ? "PASSOU |" : "FALHOU |";
        System.out.println(status1_2 + " Teste (2F)_16    | Esperado: 47" + "  | Resultado: " + res1_2);

        // Teste 3: Converter (377)_8 para decimal
        long res1_3 = MudancaDeBase.paraDecimal("377", 8);
        String status1_3 = (res1_3 == 255) ? "PASSOU |" : "FALHOU |";
        System.out.println(status1_3 + " Teste (377)_8    | Esperado: 255" + " | Resultado: " + res1_3);

        // Teste 4: Converter (Z)_36 para decimal
        long res1_4 = MudancaDeBase.paraDecimal("Z", 36);
        String status1_4 = (res1_4 == 35) ? "PASSOU |" : "FALHOU |";
        System.out.println(status1_4 + " Teste (Z)_36     | Esperado: 35" + "  | Resultado: " + res1_4);

        // Teste 5: Converter (0)_5 para decimal
        long res1_5 = MudancaDeBase.paraDecimal("0", 5);
        String status1_5 = (res1_5 == 0) ? "PASSOU |" : "FALHOU |";
        System.out.println(status1_5 + " Teste (0)_5      | Esperado: 0" + "   | Resultado: " + res1_5);


        //---------------------------------------------------------
        // Teste Seção 5, converter de decimal para a base x

        System.out.println("\n------ Teste do Algoritmo 2 (Decimal para Base beta) ------");

        // Teste 1: Converter 45 para base 2
        String res2_1 = MudancaDeBase.deDecimal(45, 2);
        String status2_1 = (res2_1.equals("101101")) ? "PASSOU |" : "FALHOU |";
        System.out.println(status2_1 + " Teste 45 (Beta = 2)   | Esperado: 101101" + " | Resultado: " + res2_1);

        // Teste 2: Converter 255 para base 16
        String res2_2 = MudancaDeBase.deDecimal(255, 16);
        String status2_2 = (res2_2.equals("FF")) ? "PASSOU |" : "FALHOU |";
        System.out.println(status2_2 + " Teste 255 (Beta = 16) | Esperado: FF" + "     | Resultado: " + res2_2);

        // Teste 3: Converter 0 para base 7
        String res2_3 = MudancaDeBase.deDecimal(0, 7);
        String status2_3 = (res2_3.equals("0")) ? "PASSOU |" : "FALHOU |";
        System.out.println(status2_3 + " Teste 0 (Beta = 7)    | Esperado: 0" + "      | Resultado: " + res2_3);

        // Teste 4: Converter 1000 para base 36
        String res2_4 = MudancaDeBase.deDecimal(1000, 36);
        String status2_4 = (res2_4.equals("RS")) ? "PASSOU |" : "FALHOU |";
        System.out.println(status2_4 + " Teste 1000 (Beta = 36)| Esperado: RS" + "     | Resultado: " + res2_4);


        //---------------------------------------------------------
        // Sugestão da Seção 5, converter usando os mesmos números

        System.out.println("\n------ Teste em Composição (Seção 5) ------");

       long numeroOriginal = 1000;
        int base = 36;

        String emBase36 = MudancaDeBase.deDecimal(numeroOriginal, base);
        long deVoltaParaDec = MudancaDeBase.paraDecimal(emBase36, base);
        
        String statusComp = (numeroOriginal == deVoltaParaDec) ? "PASSOU |" : "FALHOU |";
        
        System.out.println(statusComp + " Original: " + numeroOriginal + " -> Base " + base + ": " + emBase36 + " -> Voltou para Dec: " + deVoltaParaDec + "\n");

        scanner.close();
    }
}