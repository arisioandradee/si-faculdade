# Fundamento de Banco de Dados - Módulo 3 (Resumo) 

## Características de um Banco de dados 
- Estrutura/Esquema: Um esquema de banco de dados representa a configuração lógica de todo ou parte de um banco de dados relacional. Ele pode existir tanto como uma representação visual quanto como um conjunto de fórmulas conhecidas como restrições de integridade que governam um banco de dados. Essas fórmulas são expressas em uma linguagem de definição de dados, como SQL. Como parte de um dicionário de dados, o esquema indica como as entidades que compõem o banco de dados se relacionam entre si, incluindo tabelas, visualizações, procedimentos armazenados e muito mais. 

- Estado: O estado de um banco de dados corresponde ao conjunto de dados armazenados no banco de dados num determinado momento do tempo. O estado de um banco de dados obedece a sua estrutura. Ao longo do tempo, à medida que o “Mini-Mundo” correspondente ao banco de dados evoluir (mudar de estado) em função dos eventos (fatos, interações) nele ocorridos, o estado do banco de dados deverá evoluir, ou seja, correspondente ao banco de dados é o estado vazio, sem nenhum dado. O banco de dados mudará o seu estado de vazio para inicial, quando o mesmo for populado ou carregado com alguns dados iniciais.

- Comportamento: O comportamento do banco de dados corresponde ao comportamento dos elementos do mini-mundo correspondente. Especificamente em um banco de dados, seu comportamento é uma abstração das mudanças de estado que ele sofre ao longo do tempo. Em outras palavras, as mudanças de estado de um banco de dados definem o seu comportamento.

- Transação: Segundo Silberschatz, Korth e Sudarshan, coleções de operações que formam uma única unidade lógica de trabalho são chamadas transações. Mudanças de estado em um Banco de dados são efetuadas por transações. Uma transação é um conjunto de operações que levam o banco de dados de um estado consistente a outro estado consistente. As mudanças de estado de um banco de dados representam o comportamento desse banco de dados.

## Propriedades ACID
A seguir, serão apresentados os conceitos básicos de processamento de transações, mais especificamente as propriedades de Atomicidade, Consistência, Isolamento e Durabilidade.

- Atomicidade: Como uma transação é indivisível, ela é executada em sua totalidade ou não é executada. Assim, se uma transação começa a ser executada, mas falha por um motivo qualquer, quaisquer mudanças no banco de dados que a transação possa ter feito são desfeitas. Esse requisito é mantido independentemente de a transação em si ter falhado (por exemplo, se houve uma divisão por zero), de o sistema operacional ter falhado ou de o próprio computador ter deixado de funcionar.

- Consistência: As transações são uma forma ideal de estruturar a interação com um banco de dados. Isso nos leva a impor um requisito sobre as próprias transações. Uma transação precisa preservar a consistência do banco de dados se uma transação for executada atomicamente de forma isolada (será definido a seguir), começando de um banco de dados consistente, o banco de dados precisa novamente estar consistente no final da transação.

- Isolamento: Como uma transação é uma unidade única, as suas ações não podem parecer estar separadas por outras operações do banco de dados que não fazem parte da transação. Portanto, o sistema de banco de dados precisa tomar ações especiais para garantir que as transações operem corretamente, sem interferência de comandos de banco de dados executando simultaneamente. Essa propriedade é conhecida como isolamento.

- Durabilidade: Mesmo que o sistema garanta a execução correta de uma transação atômica, consistente e isolada, isso tem pouco propósito se o sistema mais tarde falhar e, como resultado, o sistema se “esquecer” da transação. Assim, as ações de uma transação precisam persistir entre as falhas. Resumindo, Depois que uma transação for completada com sucesso, as mudanças que ela fez no banco de dados persistem, mesmo se houver falhas no sistema.

 