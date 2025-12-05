# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS
Data: 05 de Dezembro de 2025 
Empresa: Abstergo Industries 
Responsável: Jessica

## Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por sua equipe de análise. O objetivo do projeto foi elencar 3 serviços AWS que foram estudados e que têm a finalidade de realizar diminuição de custos imediatos na plataforma virtual de farmácia.

## Descrição do Projeto
O projeto de otimização de custos foi dividido em 3 etapas, focadas em eliminar gastos com recursos ociosos, capacidade desnecessária e armazenamento de dados frios.

Etapa 1: Eliminação de Custos de Computação Ociosa
Nome da ferramenta: AWS Lambda

Foco da ferramenta: Computação Serverless (Pagamento por Uso).

Descrição de caso de uso: Migrar microserviços de backend (como a API para consulta de estoque e o processamento assíncrono de pedidos) que atualmente rodam em instâncias EC2 24/7 para Funções Lambda. O custo é pago apenas pelo tempo de execução do código, resultando em uma economia imediata significativa ao eliminar o pagamento por servidores ociosos durante a madrugada e períodos de baixo tráfego.

Etapa 2: Otimização da Capacidade de Servidores
Nome da ferramenta: EC2 Auto Scaling (com Scaling Dinâmico)

Foco da ferramenta: Correspondência de Capacidade à Demanda.

Descrição de caso de uso: Aplicar o Auto Scaling às instâncias EC2 que hospedam o frontend e a lógica de aplicação da farmácia. Configurar o grupo de escalabilidade para um número mínimo de instâncias fora do horário comercial (ex: 2) e escalar automaticamente para o pico de tráfego (ex: 8) durante o horário comercial. Isso garante que a Abstergo Industries só pague pela capacidade necessária em tempo real, evitando o custo de manter a capacidade máxima durante períodos de baixo acesso.

Etapa 3: Redução de Custos de Armazenamento de Dados Frios
Nome da ferramenta: Amazon S3 (Gerenciamento de Ciclo de Vida e Classes de Armazenamento)

Foco da ferramenta: Otimização de Custos de Armazenamento por Frequência de Acesso.

Descrição de caso de uso: Implementar políticas de ciclo de vida no Amazon S3 para mover automaticamente dados de alto volume e baixo acesso (como logs de auditoria, históricos de pedidos com mais de 1 ano e backups antigos de imagens de produtos) da classe S3 Standard (mais cara) para a classe S3 Standard-IA (Infrequent Access) ou S3 Glacier. A mudança imediata para classes de armazenamento mais baratas para dados que não são acessados diariamente gera uma redução imediata na fatura mensal de armazenamento.

## Conclusão
A implementação das ferramentas na empresa Abstergo Industries tem como esperado a otimização inteligente da infraestrutura e a eliminação de gastos com recursos não utilizados, o que resultará em uma diminuição de custos imediata e um aumento na eficiência operacional (escalabilidade automática).


Assinatura do Responsável pelo Projeto:
Jessica