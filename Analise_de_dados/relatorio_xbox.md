## 🎮 Projeto de Análise de Assinaturas Xbox Game Pass 📈

Este projeto visa analisar dados de assinaturas do **Xbox Game Pass** e complementos (EA Play Season Pass, Minecraft Season Pass) para fornecer **insights de negócio** sobre faturamento e vendas, culminando em um **Dashboard** de indicadores principais.

---

### 📂 Estrutura dos Dados

O arquivo de dados (Excel) está organizado em quatro abas principais:

* **Assets:** Contém a paleta de cores e elementos visuais (ícones, logos) para a **padronização visual** do Dashboard.
* **Bases:** É a **fonte principal** de dados de assinantes com as seguintes colunas-chave:
    * **Identificação:** `Subscriber ID`, `Name`.
    * **Assinatura Principal:** `Plan` (Core, Standard, Ultimate), `Start Date`, `Auto Renewal` (Yes/No), `Subscription Price`, `Subscription Type` (Monthly, Quarterly, Annual).
    * **Passes Adicionais:** Indicadores de compra e preços de `EA Play Season Pass` e `Minecraft Season Pass`.
    * **Financeiro Total:** `Coupon Value` (desconto), `Total Value` (valor total da assinatura, incluindo descontos e adicionais).
* **Cálculos:** Aba utilizada para responder às **perguntas de negócio** usando **tabelas dinâmicas** (ex: Faturamento total de planos anuais; Faturamento separado por auto renovação; Total de vendas de passes).
* **Dashboard:** **Visualização consolidada** dos principais indicadores e *insights* (ex: R$ 600,00 EA Play, R$ 940,00 Minecraft).

---

### ❓ Perguntas de Negócio Respondidas

As análises visam responder às seguintes questões de faturamento e vendas:

* **Pergunta 1:** Qual o **faturamento total** de vendas de **planos anuais**?
* **Pergunta 2:** Qual o **faturamento total** de planos anuais separado por **auto renovação**?
* **Pergunta 3:** Qual o **total de vendas** do **EA Play Season Pass**?
* **Pergunta 4:** Qual o **total de vendas** do **Minecraft Season Pass**?

---

### 🛠️ Instruções para Reprodução (Excel)

Para replicar a análise e o Dashboard:

#### 1. Importar a Base de Dados
* Certifique-se de que os dados da aba **Bases** estejam organizados em **formato de tabela** no Excel, facilitando a criação de Tabelas Dinâmicas.

#### 2. Criar Tabelas Dinâmicas
* Insira **Tabelas Dinâmicas** na aba **Cálculos** para responder a cada pergunta de negócio.
    * **Campos de Linhas:** Utilizar `Subscription Type` (para perguntas anuais) ou `Plan` (para visão geral).
    * **Campos de Valores:** Utilizar a **Soma** de `Total Value` (para faturamento de planos) ou a **Soma** dos preços dos passes adicionais (para vendas dos passes).
    * **Campos de Filtros:** Utilizar `Auto Renewal` (quando a segmentação for necessária, como na Pergunta 2).

#### 3. Aplicar Segmentações de Dados
* Utilize **Segmentações de Dados** (Slicers) conectadas às Tabelas Dinâmicas para permitir a filtragem interativa por:
    * Tipo de plano (`Plan`).
    * Período (`Start Date`).
    * Auto renovação (`Auto Renewal`).

#### 4. Construir o Dashboard
* Na aba **Dashboard**, construa a visualização consolidada utilizando:
    * **Gráficos Dinâmicos** e **KPIs (Key Performance Indicators)** que se baseiam diretamente nos resultados das Tabelas Dinâmicas criadas na aba **Cálculos**.
    * Aplique a **paleta de cores** e elementos visuais definidos na aba **Assets** para garantir a consistência e a **identidade visual**.

#### 5. Atualização dos Dados
* **Defina o período de cálculo** (ex: 01/01/2024 a 31/12/2024) para as análises.
* Configure as Tabelas Dinâmicas e Gráficos para serem **atualizados** conforme novos dados de assinatura forem inseridos na aba **Bases**.
