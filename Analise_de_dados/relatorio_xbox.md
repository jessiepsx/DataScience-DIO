# Objetivo do Projeto
O projeto consiste em analisar dados de assinaturas do Xbox Game Pass e seus complementos (EA Play Season Pass e Minecraft Season Pass) para responder perguntas de negócio e gerar insights sobre faturamento e vendas. Além disso, há um dashboard que resume os principais indicadores.

## Estrutura dos Dados
O arquivo contém quatro abas principais:

Assets: Paleta de cores e elementos visuais (ícones, logos) para padronização do dashboard.
Bases: Base de assinantes com colunas como:

Subscriber ID, Name, Plan (Core, Standard, Ultimate)
Start Date, Auto Renewal (Yes/No)
Subscription Price, Subscription Type (Monthly, Quarterly, Annual)
Indicadores de compra de passes adicionais:

EA Play Season Pass e seu preço
Minecraft Season Pass e seu preço

Coupon Value e Total Value (valor total da assinatura considerando descontos e adicionais)

Cálculos: Respostas às perguntas de negócio com tabelas dinâmicas, por exemplo:

Faturamento total de planos anuais
Faturamento separado por auto renovação
Total de vendas de EA Play e Minecraft Season Pass

Dashboard: Visualização consolidada com indicadores principais (ex.: R$ 600,00 EA Play, R$ 940,00 Minecraft). [0120950e-6...22ed198c69 | Excel]


## Perguntas de Negócio Respondidas

Pergunta 1: Qual o faturamento total de vendas de planos anuais?
Pergunta 2: Qual o faturamento total de planos anuais separado por auto renovação?
Pergunta 3: Total de vendas do EA Play Season Pass.
Pergunta 4: Total de vendas do Minecraft Season Pass. [0120950e-6...22ed198c69 | Excel]


## Instruções para Reprodução
Para reproduzir este projeto no Excel:

### Importar a base de dados:
Certifique-se de que os dados estão organizados em formato de tabela.
Use a aba Bases como fonte principal.

### Criar Tabelas Dinâmicas:
Para responder às perguntas de negócio, insira tabelas dinâmicas:

#### Linhas: Subscription Type ou Plan
#### Valores: Soma de Total Value ou preços dos passes adicionais.
#### Filtros: Auto Renewal quando necessário.

### Aplicar Segmentações de Dados:
Utilize segmentações para filtrar por tipo de plano, período ou auto renovação.

### Construir o Dashboard:
Use gráficos dinâmicos e KPIs com base nas tabelas dinâmicas.
Aplique a paleta de cores definida na aba Assets para manter a identidade visual.

### Atualização dos Dados:

Defina o período de cálculo (ex.: 01/01/2024 a 31/12/2024).
Atualize as tabelas dinâmicas e gráficos conforme novos dados forem inseridos.