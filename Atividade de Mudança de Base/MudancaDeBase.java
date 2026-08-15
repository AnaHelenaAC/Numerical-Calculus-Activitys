public class MudancaDeBase {

    private static final String SIMBOLOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Algoritmo 1: Base β para Base 10
    public static long paraDecimal(String numero, int beta) {
        if (beta < 2 || beta > 36) {
            throw new IllegalArgumentException("Base deve estar entre 2 e 36.");
        }

        String texto = numero.toUpperCase();
        boolean ehNegativo = false;

        if (texto.startsWith("-")) {
            ehNegativo = true;
            texto = texto.substring(1); 
        }

        long resultado = 0;

        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            int valor = SIMBOLOS.indexOf(c);

            if (valor == -1 || valor >= beta) {
                throw new IllegalArgumentException("Dígito '" + c + "' é inválido para a base " + beta);
            }

            resultado = resultado * beta + valor;
        }

        if (ehNegativo) {
            resultado = resultado * -1;
        }

        return resultado;
    }

    // Algoritmo 2: Base 10 para Base β
    public static String deDecimal(long n, int beta) {
        if (beta < 2 || beta > 36) {
            throw new IllegalArgumentException("Base deve estar entre 2 e 36.");
        }

        if (n == 0) { 
            return "0"; 
        }

        StringBuilder resultado = new StringBuilder();

        while (n > 0) {
            int resto = (int) (n % beta);            
            resultado.append(SIMBOLOS.charAt(resto)); 
            n /= beta;                               
        }

        return resultado.reverse().toString();
    }
}