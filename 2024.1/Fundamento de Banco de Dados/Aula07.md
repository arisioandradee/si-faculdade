# Fundamento de Banco de Dados - Aula 07(Resumo)

## 1. Entidade Relacionamento Estendido (EER)
O ER-Estendido (EER) é uma técnica complementar da modelagem de dados que trata do mecanismo de herança de relações e de atributos. Essa técnica permite incluir na modelagem características mais avançadas do modelo de dados.

Segundo Elmasri e Navathe1, o modelo EER foi proposto como um aprimoramento do tradicional modelo ER com a inclusao de novos recursos semânticos. Essa notação acrescenta os conceitos de super-classe/subclasse, especialização/generalização e herança, além de apresentar um conjunto semântico mais preciso do que o modelo ER visando atender a sistemas de bancos de dados com um conjunto mais complexo de requisitos. Além disso, esta é uma forma de modelagem extremamente importante no projeto de banco de dados relacionais, sendo uma das mais largamente utilizadas juntamente à notação UML.

## 1.2 Associação
A associação descreve vínculos entre classes, seja binária (entre duas classes), unária (uma classe vinculada a si mesma) ou N-ária (entre mais de duas classes). As associações são representadas por linhas conectando as classes envolvidas, podendo ter setas indicando a navegabilidade da associação. As associações também podem resultar na migração da chave primária de uma tabela para outra, formando chaves estrangeiras, e se a associação implica uma dependência existencial, a chave estrangeira deve fazer parte da chave primária da tabela associada.

a) Associações 1-para-1 ou 0..1-para-1:

- Associação 1..1 (um-para-um): Indica que cada objeto de uma classe está associado a exatamente um objeto da outra classe, e vice-versa. Não há objetos adicionais não relacionados.
Exemplo: Um cliente tem um único endereço residencial, e cada endereço pertence a apenas um cliente.

- Associação 0..1 (zero-para-um): Indica que um objeto da classe pode estar associado a no máximo um objeto da outra classe, mas não é obrigatório. Pode haver objetos sem associação.
Exemplo: Um cliente pode ou não ter um endereço de cobrança associado.

b) Associações 1-para-muitos ou 0..1-para-muitos:

- Associação 1..* (um-para-muitos): Indica que um objeto de uma classe está associado a um ou mais objetos da outra classe, mas cada objeto da segunda classe está associado a no máximo um objeto da primeira classe.
Exemplo: Um departamento tem vários funcionários, mas cada funcionário pertence a apenas um departamento.

- Associação 0..* (zero-para-muitos): Indica que um objeto da classe pode não ter associação ou pode estar associado a muitos objetos da outra classe.
Exemplo: Um autor pode ter escrito zero ou mais livros.

c) Associações muitos-para-muitos:

- Associação *..* (muitos-para-muitos ou M..N): Indica que muitos objetos de uma classe podem estar associados a muitos objetos da outra classe. Isso geralmente é mapeado para uma tabela intermediária (tabela de associação) que armazena os relacionamentos.
Exemplo: Muitos alunos podem se matricular em muitos cursos, e vice-versa. Isso é representado por uma tabela de matrícula que relaciona alunos e cursos.

## 1.2 Agregação
A agregação é um conceito utilizado na modelagem de dados para representar relacionamentos entre um objeto e suas partes componentes. Ela é especialmente útil quando queremos unir diversos relacionamentos em um único bloco para facilitar a compreensão e representação do modelo.

- **Casos de Uso:**
1. Agregação dos valores do atributo de um objeto para formar o objeto como um todo.
2. Representação de um relacionamento de agregação como um relacionamento comum.
3. Combinação de objetos relacionados por uma instância de relacionamento específica em um objeto agregado de alto nível.

- **Uso na Modelagem de Dados:** A agregação é usada para unir relacionamentos independentes em um único bloco, facilitando a representação do modelo. Isso é especialmente útil quando os objetos agregados estão relacionados a outros objetos.

## 1.3 Generalização/Especialização
Especialização: A especialização é o processo de definir subclasses dentro de uma superclasse mais geral. Isso é feito identificando os atributos e relacionamentos exclusivos das subclasses. Por exemplo, consideremos uma superclasse "Animal" e suas subclasses "Cachorro", "Gato" e "Pássaro". Cada uma dessas subclasses terá atributos e comportamentos exclusivos (por exemplo, o tipo de som que fazem, se têm asas, etc.).

Generalização: A generalização é o inverso da especialização, é o processo de agrupar subclasses semelhantes sob uma superclasse mais geral. Em outras palavras, é a abstração de características comuns de várias subclasses em uma única superclasse. Continuando com o exemplo anterior, "Animal" seria a superclasse geral que abrange todas as subclasses de animais específicos.

Generalização/Especialização Total e Parcial:

- Generalização/Especialização Total: Cada entidade da superclasse deve ser membro de pelo menos uma subclasse. Em outras palavras, não há entidades na superclasse que não sejam também membros de alguma subclasse.

- Generalização/Especialização Parcial: Algumas entidades da superclasse podem não ser membros de nenhuma subclasse. Em outras palavras, a especialização é opcional.

## 2. Diagrama entidaded relacionamento estendido (DEER)
Até agora você viu os conceitos do Modelo Entidade Relacionamento Estendido (EER), porém, alguns aspectos importantes devem ser levados em consideração na hora de modelar (criar o Diagrama via UML).

O primeiro passo é pegar o Modelo Conceitual e identificar em quais entidades você pode usar os conceitos de extensão. Para isso, existem algumas técnicas (regras para a utilização) que serão discutidas adiante.

## 2.1 Uso de associação
Como visto anteriormente, associação é ter um objeto como atributo de outro. O fator principal para a utilização desse conceito passa quanto à obrigatoriedade dos elementos de uma entidade participarem, ou não, no relacionamento com outra entidade. Porém, deve-se prestar muita atenção quando se ver em situações que pretende utilizar entidades associativas.

Uma entidade associativa nada mais é que a redefinição de um relacionamento, que passa a ser tratado como se fosse uma entidade. Portanto, a sua utilização surge quando há necessidade de associar uma entidade a um relacionamento já existente.

## 2.2 Uso de agregação
Restrição: A agregação só deve ser empregada quando o relacionamento entre as entidades é muitos-para-muitos (M:N). Se cada objeto estiver associado a apenas um objeto da outra classe, então a agregação não é necessária e as entidades podem ser relacionadas diretamente.

Lembre-se sempre de quando existir um relacionamento muitos para muitos e houver um relacionamento com dependência deste relacionamento que deverá ser usada a Agregação para representar tal dependência. Porém, nunca devemos usar Agregação com relacionamentos um para muitos.

## 2.3 Uso dde generalização/especialização
O uso da Generalização é indicado quando existe algum atributo que seja aplicável a mais de uma entidade no Modelo Entidade Relacionamento. Se existe, devemos usar a Generalização e criar uma entidade mãe que contenha os atributos comuns as outras entidades especializadas.

Uso da Especialização é indicado quando temos atributos específicos para um determinado subconjunto de ocorrências dentro de uma Entidade. Por exemplo, na entidade CLIENTES, temos clientes que são empresas e outros clientes são pessoas físicas. Os clientes que são empresas possuem atributos específicos como CNPJ e Inscrição Estadual. Neste caso, podemos promover uma especialização e criar a entidade CLIENTE-EMPRESA que especializa a entidade CLIENTE e que possui atributos específicos de uma empresa.