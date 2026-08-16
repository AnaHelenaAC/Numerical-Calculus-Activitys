public class MudancaDeBase {
 
    private static final String SIMBOLOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // --------------- Algoritmo 1: Base β para Base 10 (Decimal) ---------------
    public static long BetaParaDecimal(String numero, int beta) {
        // Tratamento de acordo com as condições do enunciado (base [β] entre 2 e 36)
        if (beta < 2 || beta > 36) {
            throw new IllegalArgumentException("Base deve estar entre 2 e 36.");
        }

        // Tratamento de acordo com as condições do enunciado (número não nulo)
        if (numero == null || numero.isEmpty()) {
            throw new IllegalArgumentException("Número não pode ser nulo ou vazio.");
        }

        // Tratamento de acordo com as condições do enunciado (número negativo)
        String texto = numero.toUpperCase();
        boolean ehNegativo = false;

        // Tratamento de acordo com as condições do enunciado (número negativo)
        if (texto.startsWith("-")) {
            ehNegativo = true;
            texto = texto.substring(1); 
        }

        long resultado = 0;

        // Conversão do número da base β para Base 10 (Decimal)
        for (int i = 0; i < texto.length(); i++) {
            // Obtém o valor do dígito atual na base β
            char c = texto.charAt(i);
            int valor = SIMBOLOS.indexOf(c);

            // Tratamento de acordo com as condições do enunciado (dígito inválido para a base)
            if (valor == -1 || valor >= beta) {
                throw new IllegalArgumentException("Dígito '" + c + "' é inválido para a base " + beta);
            }

            // Cálculo do valor decimal acumulado (expansão polinomial da base)
            resultado = resultado * beta + valor;
        }

        // Ajusta o resultado se o número for negativo
        if (ehNegativo) {
            resultado = resultado * -1;
        }

        return resultado;
    }

    // --------------- Algoritmo 2: Base 10 para Base β ---------------
    public static String DecimalParaBeta(long n, int beta) {
        // Tratamento de acordo com as condições do enunciado (base [β] entre 2 e 36)
        if (beta < 2 || beta > 36) {
            throw new IllegalArgumentException("Base deve estar entre 2 e 36.");
        }

        // Tratamento de acordo com as condições do enunciado (número não nulo)
        if (n == 0) { 
            return "0"; 
        }

        // Tratamento de acordo com as condições do enunciado (número negativo)
        if (n < 0) {
            throw new IllegalArgumentException("Número não pode ser negativo.");
        }   
        StringBuilder resultado = new StringBuilder();

        // Conversão do número decimal para a base β (Usando divisões sucessivas)
        while (n > 0) {
            int resto = (int) (n % beta);            
            resultado.append(SIMBOLOS.charAt(resto)); 
            n /= beta;                               
        }

        // Inverte a string para obter o número na base correta
        return resultado.reverse().toString();
    }
}