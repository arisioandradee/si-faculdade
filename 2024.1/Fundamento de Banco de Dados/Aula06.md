# Fundamento de Banco de Dados - Aula 06 (Resumo)

## 1. Modelo Relacional de Banco de Dados
O modelo relacional foi criado por Edgar F. Codd, nos anos 70, e começou a ser usado com o surgimento dos bancos de dados relacionais, nos anos 80. A ideia de modelo relacional se baseia no princípio de que as informações em uma base de dados podem ser consideradas como relações matemáticas (algo como uma tabela de valores) e que podem ser representadas, de maneira igual, através do uso de tabelas nas quais as linhas representam as ocorrências de uma entidade e as colunas representam os atributos de uma entidade do modelo conceitual. Ao definir o modelo relacional, Codd estabeleceu 12 regras para a determinação de um banco de dados relacional. Essas regras são usadas, portanto, para se verificar a fidelidade de um banco de dados ao modelo relacional.

1. Toda informação num banco de dados relacional é apresentada a nível lógico na forma de tabelas;
2. Todo dado em um banco de dados relacional tem a garantia de ser logicamente acessível, recorrendo-se a uma combinação do nome da tabela, um valor de chave e o nome da coluna;
3. Tratamento sistemático de valores nulos (ausência de informação);
4. O dicionário de dados, catálogo, do banco de dados, é baseado no modelo relacional;
5. Há uma uma linguagem não procedural para a definição, a manipulação e o controle dos dados;
6. Tratamento das atualizações de visões dos dados;
7. Tratamento de alto nível para inserção, atualização e eliminação de dados;
8. Independência física dos dados (mudança na memória e no método de acesso, criação de um novo índice, criação de uma nova coluna);
9. Independência lógica dos dados (mudança no tamanho de uma coluna);
10. Restrição de Integridade (Identidade, Referencial e Domínio);
11. Independência de Distribuição dos dados;
12. Não subversão das regras de integridade ou restrições quando se usa uma linguagem hospedeira.

Segundo ElmasrI e Navathe, no modelo relacional, cada linha na tabela representa um fato que corresponde a uma entidade ou relacionamento do mundo real. O nome da tabela e os nomes das colunas são usados para ajudar na interpretação do significado dos valores em cada linha.

Na terminologia do modelo relacional formal, uma linha é chamada tupla, um cabeçalho de coluna é conhecido como atributo e a tabela é chamada relação. O tipo de dado que descreve os tipos de valores que podem aparecer em cada coluna é representado pelo domínio de valores possíveis. Definimos, agora, esses termos (domínio, tupla, atributo e relação) de forma mais precisa.

## 1.1 1.1 DOMÍNIOS, ATRIBUTOS, TUPLAS E RELAÇÕES

1. Dominio - Para Elmasr e Navathe, um domínio D é um conjunto de valores atômicos. Por atômico é dito que cada valor no domínio é indivisível no que diz respeito ao modelo relacional. Um método comum para a especificação de um domínio é definir um tipo de dado do qual os valores de dados que formam o domínio sejam retirados. ex: nomes, idade_funcionario...

2. Relação - O modelo relacional para gerência de bases de dados (SGBD) é baseado em lógica e na teoria de conjuntos, representando o banco de dados como uma coleção de relações, semelhantes a tabelas. Cada relação consiste em entidades caracterizadas por dados coletados, representando uma tabela. O modelo é construído sobre dois conceitos principais: entidade e relação, onde uma entidade é identificada pelos dados coletados e uma relação determina como os registros de uma tabela se relacionam com registros de outras tabelas. 

3. Atributo - Os atributos são características ou propriedades que descrevem as entidades em uma relação. Cada atributo representa uma coluna em uma tabela relacional e descreve uma característica específica dos objetos representados por essa tabela.

4. Tuplas - De forma mais simplificada, temos que uma tupla é um conjunto de atributos que são ordenados em pares de domínio e valor. Uma relvar (variável relacional) é um conjunto de pares ordenados de domínio e nome que serve como um cabeçalho para uma relação. Uma relação é um conjunto desordenado de tuplas. Uma relação é similar ao conceito de tabela e uma tupla é similar ao conceito de linha.

## 1.2 Restrições do modelo relacional
a) Restrição de Chaves: Garante que as tuplas de uma relação sejam únicas, identificando um conjunto mínimo de atributos chamado chave candidata, que deve satisfazer requisitos específicos.

b) Restrição de Entidade: Estabelece que nenhum valor da chave primária pode ser nulo, pois a chave primária é utilizada para identificar as tuplas individuais em uma relação.

c) Restrição de Integridade Referencial: Assegura a consistência da informação entre diferentes relações, especificando uma restrição envolvendo ambas as relações, geralmente através de chaves estrangeiras que fazem referência à chave primária de outra relação.

## 2. Modelo Relacional x Modelo Entidade Relacionamento
O Modelo Entidade Relacionamento (MER) é adequado para representar um projeto de banco de dados em alto nível. Uma vez pronto o esquema da base de dados em MER, é preciso converter esse esquema para o esquema de banco de dados a ser usado, geralmente no modelo relacional. Para isso, existe um conjunto de regras que direcionam o usuário nesta atividade, tratando, inclusive, restrições que não foram cobertas no esquema conceitual. Essas regras serão discutidas a seguir, abrangendo os principais elementos do MER.

## 2.1 Conjunto de Entidade
Um conjunto entidade, que chamaremos pela sigla CE, é mapeado no modelo relacional com uma relação. Os atributos dessa relação serão os mesmos do CE, bem como os seus respectivos domínios. Da mesma forma, a chave primária também é mantida.

## 2.2 Conjuntos relacionamento
a) Conjuntos relacionamento sem Restrições: Neste caso, o CR é mapeado para uma nova relação, onde a chave primária de cada entidade envolvida no relacionamento se torna chave estrangeira nessa nova relação. A chave primária da nova relação é composta pelas chaves estrangeiras das entidades participantes do relacionamento.

a) Conjuntos relacionamento com Restrições: Existem duas opções para esse mapeamento. A primeira é criar uma nova relação para representar o CR, com chaves estrangeiras para as entidades envolvidas. A segunda opção é incorporar o CR em uma das relações das entidades envolvidas, adicionando atributos descritivos e uma chave estrangeira para referenciar a outra entidade. A segunda opção é mais vantajosa em termos de desempenho, mas pode resultar em tuplas com atributos de relacionamento vazios.