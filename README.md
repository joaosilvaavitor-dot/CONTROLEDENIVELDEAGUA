# Controle de Níveis de Água 

Este é um sistema simples de monitoramento de reservatório de água executado diretamente no terminal. O objetivo do projeto é exibir mensagens de alerta personalizadas com cores diferentes para representar o nível atual da água e o progresso de risco do reservatório.

O projeto foi desenvolvido como uma atividade técnica para praticar conceitos essenciais de programação em Python, como listas, funções, loops e a utilização de bibliotecas externas.

---

##  Funcionalidades

- **Mapeamento por Níveis:** Armazena e gerencia cinco níveis de capacidade do reservatório utilizando listas.
- **Alertas Coloridos:** Altera a cor do texto do terminal dinamicamente conforme a gravidade da situação.
- **Simulação Automatizada:** Executa uma simulação contínua passando por todos os níveis do reservatório (do crítico ao alerta máximo).
- **Reset de Estilo:** Garante a restauração do padrão visual do terminal após a exibição das mensagens.

---

##  Tabela de Níveis e Cores

O sistema segue a seguinte progressão de risco conforme especificado na atividade:

| Nível do Reservatório | Situação | Cor Sugerida |
| :---: | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho |
| **Nível 2** | Baixo | 🟡 Amarelo |
| **Nível 3** | Médio | 🟢 Verde |
| **Nível 4** | Alto | 🔵 Ciano |
| **Nível 5** | Muito alto (alerta) | 🔵 Azul |

---

##  Tecnologias Utilizadas

- **Python**
