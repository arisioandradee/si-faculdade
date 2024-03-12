# Engenharia de Software - Aula 05(Resumo)

## 1. Medicação de software
As chamadas medidas diretas do processo de software possuem custos e trabalho aplicados. O custo e o trabalho necessários para criar o software, além do número de linhas de código produzidas e outras medidas diretas são, de certa forma, fáceis de coletar, desde que de maneira antecipada sejam definidas as convenções para as medições. Porém, a qualidade e a funcionalidade do software ou mesmo a sua eficiência ou manutenção são mais complexas de se avaliar e só podem ser medidas de forma indireta.

De acordo com Pressman e Maxim, ao dividirmos o domínio das métricas de software em processo, projeto e métricas de produto, podemos observar que as métricas de produto privadas para um indivíduo muitas vezes são combinadas para desenvolver métricas de projeto públicas para a equipe de software. As métricas de projeto são, dessa forma, consolidadas para criar métricas que são públicas à organização de software como um todo. Contudo, como uma organização combina métricas que vieram de diferentes indivíduos ou projetos?

## Métricas orientadas a tamanho
Segundo Pressman e Maxim, métricas de softwares orientadas a tamanho são criadas pela normalização das medidas de qualidade e/ou produtividade, levando-se em consideração o tamanho do software produzido. As métricas orientadas a tamanho não são aceitas universalmente como a melhor maneira de medir os processos de software. A maior parte da controvérsia gira em torno do uso de linhas de código como medida principal. Grande parte da discussão se dá pelo uso de linhas de código como medida principal.

LOC significa "Linhas de Código" (em inglês, "Lines of Code"). É uma métrica que quantifica o tamanho de um programa de computador contando o número de linhas de código-fonte escritas para criar o software. É uma das métricas mais antigas e comuns usadas para medir o tamanho e, por extensão, a complexidade de um programa de software. 

Os proponentes da utilização do LOC argumentam que:

O LOC é um "artefato" de todos os projetos de desenvolvimento de software e pode ser facilmente contado;
Que muitos modelos de estimativa de software existentes usam LOC ou KLOC como dado de entrada principal e que já existe uma grande quantidade de literatura e dados baseados em LOC.

Já os oponentes argumentam que:

As medidas LOC são dependentes da linguagem de programação;
Quando é considerada a produtividade, elas penalizam programas bem-projetados, mas menores;
Elas não podem facilmente acomodar linguagens não procedurais;
Seu uso nas estimativas requer um nível de detalhe que pode ser difícil de alcançar (isto é, o planejador deve estimar a LOC a ser produzida bem antes que a análise e o projeto estejam concluídos).

## Métricas Orientadas a Função
As métricas de software orientadas à função utilizam como valor de normalização uma medida da funcionalidade fornecida pela aplicação. A métrica orientada a função mais amplamente usada é a ponto de função (FP, function point). O ponto de função, bem como a medida LOC, são controversos. Os seus proponentes argumentam que:

Essa função é independente da linguagem de programação, tornando-a ideal para aplicações que usam linguagens convencionais e não procedurais, e que é baseada em dados que têm maior probabilidade de serem conhecidos na evolução de um projeto, o que a torna mais atraente como estratégia de estimativa;
Seus oponentes argumentam que:

O método requer um pouco de "jeitinho", porque o cálculo é baseado em dados subjetivos, em vez de objetivos, que as contagens do domínio de informação (e outras dimensões) podem ser difíceis de coletar após o fato é que a FP não tem um significado físico direto - é apenas um número.

## Padrões de processo
De acordo com Pressman e Maxim, a relação entre linhas de código e pontos de função depende da linguagem de programação adotada para implementar o software e da qualidade do projeto. Diversos estudos já tentaram relacionar medidas FP e LOC.

## Métricas Orientadas a Objetos
Métricas de projeto de software convencional (LOC ou FP) podem ser utilizadas para estimar projetos de software orientados a objetos. Porém, essas métricas não fornecem granularidade suficiente para os ajustes de cronograma e de esforço necessários à medida que são feitas iterações por meio de um processo evolucionário ou incremental.

Sugerido por Lorenz e Kidd, esses são o conjunto de métricas para projetos orientados a objeto.

- Número de scripts de cenário: Um script de cenário (análogo a um caso de uso) é uma sequência detalhada de passos que descrevem a interação entre o usuário e a aplicação. Cada script é organizado em trios da forma {iniciador, ação, participante} Em que iniciador é o objeto que solicita algum serviço (que inicia uma mensagem), ação é o resultado da solicitação e participante é o objeto servidor que atende à solicitação. O número de scripts de cenário está correlacionado diretamente ao tamanho da aplicação e ao número de casos de testes que devem ser desenvolvidos para exercitar o sistema depois que ele é construído.


- Número de classes-chave: Classes-chave são os “componentes altamente independentes” definidos logo no início em análise orientada a objetos. Como as classes-chave são essenciais ao domínio do problema, a quantidade dessas classes é uma indicação da quantidade de esforço necessário para desenvolver o software e também uma indicação do potencial de reutilização a ser aplicado durante o desenvolvimento do sistema.


- Número de classes de apoio: Classes de apoio são necessárias para implementar o sistema, mas não estão imediatamente relacionadas ao domínio do problema. Como exemplo, podemos citar as classes de interface de usuário (UI), classes de acesso e manipulação de bancos de dados e classes de cálculo. Além disso, podem ser desenvolvidas classes de apoio para cada uma das classes-chave. As classes de apoio são definidas interativamente ao longo de um processo evolucionário. O número de classes de apoio é uma indicação da quantidade de esforço necessário para desenvolver o software e também uma indicação do potencial de reutilização a ser aplicado durante o desenvolvimento do sistema.

- Número médio de classes de apoio para cada classe-chave: Se o número médio de classes de apoio para cada classe-chave fosse conhecido para determinado domínio de problema, a estimativa (baseada no número total de classes) seria muito simplificada.

- Número de subsistemas: Um subsistema é uma agregação de classes que apoia uma função que é visível para o usuário final de um sistema. Uma vez identificados os subsistemas, é mais fácil elaborar um cronograma adequado no qual o trabalho, nos subsistemas, é dividido entre o pessoal de projeto.
Para serem usadas de modo eficaz em um ambiente de engenharia de software orientado a objetos, métricas similares àquelas mencionadas acima devem ser coletadas juntamente às medidas de projeto, tais como o esforço gasto, erros e defeitos descobertos e modelos ou páginas de documentação produzidas. À medida que o banco de dados cresce (após completar um grupo de projetos), as relações entre as medidas orientadas a objetos e as medidas de projeto fornecerão métricas que podem ajudar nas estimativas do projeto.

## Métricas Orientadas a casos de uso
Os casos de uso são frequentemente utilizados para descrever requisitos de software no nível dos clientes ou no domínio de negócio, sugerindo suas características e funções. Assim como as métricas de Linhas de Código (LOC) e Pontos de Função (FP), os casos de uso podem ser usados como uma medida de normalização para estimativas no início do processo de desenvolvimento de software. Eles descrevem funções visíveis ao usuário e são independentes da linguagem de programação. No entanto, devido à sua natureza abstrata e variabilidade na criação, não há um tamanho padrão para os casos de uso, o que torna sua aplicação como medida de normalização suspeita. Os pontos de casos de uso (UCPs) foram propostos como uma forma de estimar o trabalho de projeto e outras características, sendo uma função do número de atores e transações nos casos de uso, semelhante aos Pontos de Função.

## Métricas de projeto de Webapp
O objetivo dos projetos de WebApps é fornecer conteúdo e funcionalidade aos usuários. Métricas específicas são necessárias para medir o progresso e a qualidade desses projetos, diferindo das métricas tradicionais de engenharia de software. Pressman e Maxim propõem uma série de medidas para avaliar WebApps, como número de páginas estáticas e dinâmicas, links internos, objetos de dados persistentes, interfaces de sistemas externos, entre outros. Essas métricas podem ser correlacionadas com medidas de projeto, como esforço gasto e erros descobertos, para fornecer indicadores que auxiliam na estimativa e gerenciamento do projeto de desenvolvimento de WebApps.