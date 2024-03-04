# Fundamento de Banco de Dados - Módulo 5 (Resumo) 

## Conceitos de modelagem entidade-relacionamento na criação de diagramas entidade-relacionamento
Quando estamos empenhados no desenvolvimento de um sistema para computador (seja de grande ou pequeno porte), devemos planejar todas as suas etapas e dedicar atenção especial ao projeto e à estruturação do banco de dados. Para isso, utilizamos uma técnica chamada modelagem de dados, cujo objetivo é transformar uma ideia conceitual em algo que possa ser traduzido em termos computacionais. Com a modelagem de dados, podemos refinar um modelo conceitual durante as fases que compõem o projeto, eliminando redundâncias ou incoerências que possam inevitavelmente surgir.

- MER(Modelo Entidade Relacionamento): Para Alves, uma das dificuldades encontradas pelos projetistas de banco de dados sempre foi representar toda a semântica que se encontra associada aos dados presentes no minimundo. O Modelo Entidade-Relacionamento (MER) foi criado justamente para acabar essa deficiência. Ele é um modelo de dados de alto nível utilizado na fase de projeto conceitual, ou seja, na concepção do esquema conceitual do banco de dados. Nessa etapa do projeto de um sistema, não são abordados detalhes sobre implementação ou forma de armazenamento, o que torna mais fácil a compreensão do esquema de banco de dados.

a) Modelo Conceitual: É considerado a primeira etapa do projeto, em que se representa a realidade mediante uma visão global e genérica dos dados e dos seus relacionamentos. Seu objetivo é conter todas as informações dessa realidade que serão armazenadas no banco de dados, sem que se retratem aspectos relativos ao banco de dados que será utilizado. 

![Modelo Conceitual](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%202.png)

b) Modelo Lógico: É a segunda etapa do projeto compreende a descrição das estruturas que serão armazenadas no banco de dados e resulta em uma representação gráfica dos dados de maneira lógica, inclusive já nomeando-se os componentes e as ações que exercem um sobre o outro. O Modelo Lógico representa os dados em uma estrutura de armazenamento de dados. Nesse momento, é definida a estrutura de registro do Banco de Dados, os seus registros e números de campos com os seus respectivos tamanhos, conforme a figura a seguir

![Modelo Lógico](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%203.png)

c) Módelo Fisico: Do modelo lógico podemos derivar o modelo físico, no qual se encontram detalhados os componentes de estrutura física do banco de dados, como tabelas, campos, tipos de valores, índices, entre outros. Quando chegarmos a esse ponto, estaremos prontos para a criação propriamente dita do banco de dados, utilizando o sistema gerenciador que mais se adequar às nossas necessidades. Neste momento entram as questões relacionadas ao tipo e tamanho do campo, relacionamento, indexação, restrições e afins. Ele descreve as estruturas físicas de armazenamento, tais como, tabelas, índices, gatilhos (triggers), funções, visões, nomenclaturas e afins.

![Modelo Fisico](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%204.png)

## Entidades e atributos
No modelo Entidade-Relacionamento, os dados são descritos como entidades, atributos e relacionamentos e podem ser exibidos por meio de um formato gráfico denominado Diagrama Entidade-Relacionamento (DER).

a) Atributos simples: Os atributo simples não possuem qualquer característica especial. A maioria dos atributos serão simples. Quando um atributo não é composto, recebe um valor único como nome, por exemplo, e não é um atributo chave, então ele será atributo simples.

c) Atributos compostos: Já os atributos compostos podem ser desmembrados em partes menores, como é o caso do atributo Endereço, que pode ser dividido em Tipo de Logradouro (Rua, Av., Pça. etc.), Nome do logradouro, Número do imóvel e Complemento (apto., sala, loja e afins).

d) Atributos multivalorados: Em alguns casos, um atributo pode ter um conjunto de valores para a mesma entidade, por exemplo, um atributo Cor para um carro ou um atributo Titulação para uma pessoa. Os carros com uma cor têm um valor único, enquanto aqueles com dois tons contêm dois valores para Cor. Da mesma forma, uma pessoa pode não ter um título acadêmico, outra pessoa pode ter um e, uma terceira pessoa, dois ou mais títulos; portanto, pessoas diferentes podem ter números de valores diferentes para o atributo Titulação. Esses atributos são chamados multivalorados. 

## Relacionamentos
Analisando a relação FUNCIONARIO apresentada no nosso sistema exemplo, imagine que surja uma nova entidade no projeto de banco de dados, chamada de SETOR que vincula o funcionário a um setor da empresa. Por exemplo, o funcionário Alves Chagas está lotado no setor de Recursos Humanos (RH), a funcionária Andréia Sampaio está lotada no setor de Contabilidade e assim por diante.

Embora se trate de um atributo que vincula a relação FUNCIONARIO à relação SETOR, no Modelo Entidade-Relacionamento, devemos representar essa ligação por meio de um relacionamento. Esse relacionamento é um conjunto de associações das duas relações ou entidades. A figura a seguir ilustra o relacionamento no Diagrama Entidade-Relacionamento (DER).

![Relacionamento](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%206.png)

a) Relacionamento binário: Um relacionamento pode ser classificado de acordo com o número de entidades que participam dele. No nosso exemplo, temos duas entidades (FUNCIONÁRIO e SETOR), sendo, portanto, um relacionamento binário ou de grau dois. Pode haver relacionamentos com grau maior que dois, embora o mais comum seja o binário.

b) Relacionamento ternário: Um exemplo de relacionamento de grau três, ou ternário, pode ser visto na figura a seguir:
![Relacionamento](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%207.png)

c) Autorrelacionamento: Imagine agora a seguinte situação: uma empresa possui diversos empregados; alguns deles são chefes e outros são subordinados. Ao transportar esse cenário para o Modelo Entidade-Relacionamento, devemos ter um diagrama parecido com o mostrado pela figura a seguir. Esse tipo de relacionamento é chamado de autorrelacionamento e nele os nomes dos papéis desempenhados pelas entidades participantes não são claros.
![Relacionamento](https://ava.unicatolicaquixada.edu.br/mtd/disciplinas/fdb/UA05/images/Figura%208.png)

## Cardinalidade dos relacionamentos
A razão de cardinalidade é uma restrição para um relacionamento binário que determina quantas vezes uma entidade pode participar de um relacionamento. No exemplo dos funcionários que estão lotados nos setores (Figura 6), temos que cada funcionário pode trabalhar apenas em um único setor. Por outro lado, um departamento pode conter vários funcionários. Para o primeiro caso, temos uma razão de cardinalidade 1:N; para o segundo, encontramos a razão de cardinalidade N:1.

Na restrição de participação, a existência de uma entidade depende da existência, também, de outra à qual está relacionada. Podemos ter restrição de participação total ou parcial. No primeiro caso, todas as entidades devem satisfazer a condição imposta. Por exemplo, todos os funcionários devem estar lotados em um departamento, que é a condição para que o funcionário trabalhe na empresa. Isso determina uma restrição total.

Para a restrição parcial, podemos tomar como exemplo o fato de que nem todo empregado é chefe de setor. Isso significa que apenas parte da coleção FUNCIONARIOS participa do relacionamento.

Já a restrição estrutural determina os números mínimo e máximo de participações de uma entidade dentro do relacionamento. Um cliente, por exemplo, pode ter uma, várias ou nenhuma compra efetuada. Assim, a quantidade mínima de instâncias seria 0 e, o número máximo, a quantidade de vezes que ele comprou na loja.


