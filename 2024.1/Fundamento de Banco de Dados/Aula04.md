# Fundamento de Banco de Dados - Módulo 4 (Resumo) 

## Arquiteturas de um Banco de dados
A arquitetura de um sistema de banco de dados é bastante influenciada pelo sistema de computador subjacente em que o sistema de banco de dados é executado, principalmente por aspectos como arquitetura de processador e memória, operação em rede, além de requisitos de paralelismo e distribuição.

- Arquitetura Centralizada: Usar uma unica máquina para executar o processamento principal e de todas as funções do sistema, incluindo os programas aplicativos, programas de interface com o usuário, bem como a funcionalidade dos SGBDs.

- Arquitetura Cliente/Servidor básica: Nesta arquitetura, os programas de interface com o usuário e os de aplicação podem ser executados no lado do cliente.O acesso ao SGBD ocorre através de uma conexão estabelecida entre o programa do cliente e o programa do servidor.O padrão ODBC (Open Database Connectivity) fornece a interface para os programas do lado do cliente se conectarem ao SGBD.Os resultados das consultas são enviados de volta para o programa do cliente para processamento ou exibição.

- Arquitetura Cliente/Servidor de duas camadas: Nesta arquitetura, os componentes do software são distribuídos em dois sistemas: cliente e servidor.O servidor geralmente inclui a parte do software SGBD responsável pelo armazenamento de dados, controle de concorrência, recuperação, buferização, entre outras funções.O cliente normalmente executa a interface do usuário, interagindo diretamente com o usuário final.

- Arquitetura de três camadas para aplicações web: consiste em ter uma estrutura intermediária entre o cliente e o servidor de banco de dados. Essa estrutura intermediária, chamada de servidor de aplicação ou servidor web, armazena as regras de negócio e pode aumentar a segurança do banco de dados, verificando as credenciais dos clientes antes de enviar solicitações ao servidor de banco de dados. Os clientes têm interfaces gráficas e regras de negócio específicas para a aplicação. O servidor intermediário aceita solicitações dos clientes, processa-as e envia comandos de banco de dados ao servidor de banco de dados. Ele também age como um intermediário para passar os dados processados parcialmente do servidor de banco de dados para os clientes. Dessa forma, a interface com o usuário, as regras de aplicação e o acesso aos dados formam as três camadas distintas dessa arquitetura.

## Banco de dados em Sistemas Distribuídos
A arquitetura em um sistema de banco de dados distribuído, o banco de dados é armazenado em nós localizados em sites (nós) separados geograficamente. Os nós em um sistema distribuído se comunicam entre si por meio de diversos meios de comunicação, como redes privadas de alta velocidade ou pela internet. Eles não compartilham memória principal ou discos. A estrutura geral de um sistema distribuído aparece na figura a seguir.
![Foto](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA04/images/Figura%204.png)

Um banco de dados distribuído, consiste em um relação de nós, conforme dito anteriormente, e cada nó desses pode participar na execução de transações que acessam dados em um ou mais nós. Os processadores em um sistema distribuído podem variar em tamanho e função, podendo incluir microcomputadores, estações de trabalho, minicomputadores e sistemas de computadores de uso em geral. Estes processadores são geralmente chamados de nós, dependendo do contexto no qual eles estejam mencionados. 

## Banco de dados em nuvem
No modelo de computação em nuvem, as aplicações de uma empresa são executadas em uma infraestrutura gerenciada por outra empresa, geralmente em um datacenter que hospeda grande número de máquinas usadas por muitas empresas/usuários diferentes. O provedor de serviços pode fornecer não apenas hardware, mas também plataformas de suporte, como bancos de dados e software de aplicação.

## Resumo geral das diferenças de arquiteturas
Na arquitetura centralizada, existe um computador com grande capacidade de processamento, o qual é o hospedeiro do SGBD e emuladores para os vários aplicativos. Esta arquitetura tem como principal vantagem a de permitir que muitos usuários manipulem grande volume de dados. Sua principal desvantagem está no seu alto custo, pois exige ambiente especial para mainframes e soluções centralizadas. Na arquitetura de sistemas de banco de dados centralizados são executados inteiramente em um computador único. Os sistemas de banco de dados projetados para sistemas multiusuário precisam oferecer suporte ao conjunto completo de recursos de transação. Esses sistemas normalmente são projetados como servidores que aceitam solicitações de aplicações por meio de SQL ou de suas próprias APIs. Em contrapartida, um sistema de banco de dados distribuído é uma coleção de sistemas de banco de dados parcialmente independentes que (de forma ideal) compartilham um esquema comum e distribuem o processamento de transações que acessam dados não locais. 

Na cliente-servidor, o cliente (front_end) executa as tarefas do aplicativo, ou seja, fornece a interface do usuário (tela, e processamento de entrada e saída). O servidor (back_end) executa as consultas no DBMS e retorna os resultados ao cliente. Apesar de ser uma arquitetura bastante popular, são necessárias soluções sofisticadas de software que possibilitem: o tratamento de transações, as confirmações de transações (commits), desfazer transações (rollbacks), linguagens de consultas (stored procedures) e gatilhos (triggers). A principal vantagem desta arquitetura é a divisão do processamento entre dois sistemas, o que reduz o tráfego de dados na rede.

A computação em nuvem permite a execução de cargas de trabalho remotamente pela Internet a partir do data center de um fornecedor comercial em um modelo de "nuvem pública".Um banco de dados na nuvem é uma coleção de conteúdo, estruturado ou não estruturado, que reside em uma plataforma de infraestrutura de computação em nuvem privada, pública ou híbrida. Existem dois modelos de ambiente de banco de dados em nuvem: tradicional e banco de dados como serviço (DBaaS).




 