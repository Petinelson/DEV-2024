programa {
	funcao inicio() {
		real moeda_r, moeda_d, resultado
		inteiro tipo_moeda
		escreva ("Qual a cotação do Dólar? ")
		leia(moeda_d)
		
		escreva ("Escolha: \n")
		escreva ("[1] - Converter Dólar para Real \n")
		escreva ("[2] - Converter Real para Dólar \n")
		
		escreva ("Digite um numero para conversão: ")
		leia(tipo_moeda)
		
		se(tipo_moeda == 1){
			escreva ("Qual o valor em Dólar a ser convertido para Real? ")
			leia(moeda_r)
			resultado = moeda_r * moeda_d
		} senao{
			escreva ("Qual o valor em Real a ser convertido para Dólar? ")
			leia(moeda_r)
			resultado = moeda_r / moeda_d
		}
		escreva ("O valor convertido é: $", resultado))
	}
}
