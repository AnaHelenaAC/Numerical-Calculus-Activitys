public class MudancaDeBase {
    private static final String SIMBOLOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Converte a base para decimal
    public static long paraDecimal(String numero, int beta) {
        // Tratamento dos casos de borda
        if (beta < 2 || beta > 36) {
            throw new IllegalArgumentException("Base deve estar entre 2 e 36.")
        }

        long resultado = 0;
        String texto = numero.toUpperCase();

        // Percorrendo os dígitos da string (do mais para o menos significativo)
        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            int valor = SIMBOLOS.indexOf(c); // Transforma a letra/dígito em número

            if (valor == -1 || valor >= beta) { ...} // Valida se o dígito existe na base

            // EXPANSÃO POLINOMIAL E ACÚMULO DO RESULTADO
            // A cada passo, multiplicamos o que já temos pela base e somamos o novo dígito.
            resultado = resultado * beta + valor;
        }

        return resultado;
    }

    // Converte de decimal para base beta
    public static String deDecimal(long n, int beta) {
        // 1. Tratamento de erro
        if (beta < 2 || beta > 36) { ... }

        // 2. Tratando corretamente o caso N = 0 (Exigência do enunciado)
        if (n == 0) { return "0"; }[cite: 1]

        StringBuilder resultado = new StringBuilder();

        // Divisões Inteiras Sucessivas
        while (n > 0) {
            // Guarda o resto da divisão por beta
            int resto = (int) (n % beta);
            // Converte o resto no símbolo correspondente e guarda na string
            resultado.append(SIMBOLOS.charAt(resto));
            // Atualiza o valor de N dividindo por beta
            n /= beta;
        }

        // 4. Montando a string final na ordem correta
        // Como os restos são obtidos de trás para frente, precisamos inverter a string no final
        return resultado.reverse().toString();
    }

}