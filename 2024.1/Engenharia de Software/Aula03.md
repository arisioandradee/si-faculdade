# Engenharia de Software - Aula 03 (Resumo)

## 1. O que é processo ágil?
Segundo Pressman e Maxim1, qualquer processo ágil de software é caracterizado de modo que lide com uma série de processos-chave referente à maioria dos projetos de software:

1. É difícil antecipar quais requisitos de software perduram e quais sofrerão algum tipo de alteração. É igualmente difícil visualizar a forma como as prioridades do cliente sofrerão mudanças conforme o projeto avança.

2. Em muitos modelos de software, o projeto e a construção são intercalados. As duas atividades devem ser construídas em conjunto para que os modelos de projeto sejam aprovados conforme são criados. É complexo antecipar a quantidade de trabalho de projeto, sendo necessário que a sua realização seja executada para avaliar o projeto.

3. A Análise, o Projeto, a Construção e os Testes não são tão pronunciáveis (do ponto de vista de planejamento) quanto desejaríamos que fossem.

## 1.1 Princípios da agilidade
A Agile Alliance estabelece 12 princípios para alcançar a agilidade, a saber:

1. A maior prioridade é satisfazer o cliente com entrega adiantada e contínua de software funcionando.

2. Aceite bem os pedidos de alterações, mesmo com o desenvolvimento adiantado. Os processos ágeis se aproveitam das mudanças para a vantagem competitiva do cliente.

3. Entregue software em funcionamento frequentemente, de algumas semanas a alguns meses, dando preferência a intervalos mais curtos.

4. O pessoal do comercial e os desenvolvedores devem trabalhar em conjunto diariamente ao longo de todo o projeto.

5. Construa projetos em torno de pessoas motivadas. Dê a elas o ambiente e o apoio necessários e acredite que elas farão o trabalho corretamente.

6. O método mais eficiente e efetivo de transmitir informações para e dentro de uma equipe de desenvolvimento é uma conversa aberta, presencial.

7. Software em funcionamento é a principal medida de progresso.

8. Os processos ágeis promovem desenvolvimento sustentável. Proponentes, desenvolvedores e usuários devem estar aptos a manter um ritmo constante indefinidamente.

9. Atenção contínua para com a excelência técnica e para com bons projetos aumenta a agilidade.

10. Simplicidade – a arte de maximizar o volume de trabalho não realizado – é essencial.

11. As melhores arquiteturas, os requisitos e os projetos surgem de equipes auto-organizadas.

12. Em intervalos regulares, a equipe se avalia para ver como pode se tornar mais eficiente, então, sintoniza e ajusta seu comportamento de acordo.

## 1.2 A politica do desenvolvimento fácil
O autor Jim Highsmith (em tom de piada) estabelece posições distintas ao caracterizar o sentimento do grupo pró-agilidade (“os agilistas”). “Os metodologistas tradicionais são um bando de ‘pés na lama’ que preferem produzir documentação sem falhas em vez de um sistema que funcione e atenda às necessidades do negócio”2. Em um contraponto, ele apresenta (mais uma vez em tom de piada) a posição do grupo da engenharia de software tradicional: “Os metodologistas de pouco peso, quer dizer, os metodologistas ‘ágeis’, são um bando de hackers pretensiosos que vão acabar tendo uma grande surpresa ao tentarem transformar os seus brinquedinhos em software de porte empresarial”.

## 2. Scrum
Scrum é um método de desenvolvimento ágil de software concebido por Jeff Sutherland e sua equipe de desenvolvimento no início dos anos 1990. Mais recentemente, Schwaber e Beedle realizaram desenvolvimentos adicionais nos métodos Scrum.

O Scrum ressalta o uso de um conjunto de padrões de processos de software, padrões esses que provaram ser eficazes em projetos com prazos de entrega apertados, requisitos mutáveis e urgência do negócio. No quadro a seguir, será apresentado um conjunto de atividades de desenvolvimento

- Backlog: Uma lista com prioridades dos requisitos ou funcionalidades do projeto que fornecem valor comercial ao cliente. Os itens podem ser adicionados a esse registro a qualquer momento (é assim que as alterações são introduzidas). O gerente de produto avalia o registro e atualiza as prioridades conforme solicitado.

- Sprints: Consistem em unidades de trabalho solicitadas para atingir um requisito estabelecido no (backlog) e que precisa ser ajustado dentro de um prazo já fechado (janela de tempo)10 (tipicamente 30 dias). Portanto, o sprint permite que os membros de uma equipe trabalhem em um ambiente de curto prazo, porém, estável.

- Reunião Scrum: São reuniões curtas (tipicamente 15 minutos), realizadas diariamente pela equipe Scrum.

- Demos: Entrega do incremento de software ao cliente para que a funcionalidade implementada possa ser demonstrada e avaliada por ele. É importante notar que a demo pode não ter toda a funcionalidade planejada, mas sim funções que possam ser entregues no prazo estipulado

## 3. Método de desenvolvimento de Sistemas DIN MICOS(DSDM)
O Método de Desenvolvimento de Sistemas Dinâmicos (DSDM, Dynamic Systems Development Method) é uma metodologia de desenvolvimento de software ágil.

De acordo com Pressman e Maxim, esse consórcio definiu um modelo de processos ágeis, chamado ciclo de vida DSDM, que começa com um estudo de viabilidade, o qual estabelece os requisitos básicos e as restrições do negócio, e é seguido por um estudo do negócio, o qual identifica os requisitos de função e informação. O DSDM estabelece três diferentes ciclos iterativos:

- Iteração de modelos funcionais: Produz um conjunto de protótipos incrementais que demonstram funcionalidade para o cliente. Durante esse ciclo iterativo, o objetivo é reunir requisitos adicionais ao se obter feedback dos usuários, à medida que eles testam o protótipo.

- Iteração de projeto e desenvolvimento: Revê os protótipos desenvolvidos durante a iteração de modelos funcionais para assegurar-se de que cada um tenha passado por um processo de engenharia para capacitá-los a oferecer, aos usuários, valor de negócio em termos operacionais. Em alguns casos, a interação de modelos funcionais e a iteração de projeto e desenvolvimento ocorrem ao mesmo tempo.

- Implementação: Coloca a última versão do incremento de software (um protótipo “operacionalizado”) no ambiente operacional. Deve-se notar que: (1) o incremento pode não estar 100% completo ou (2) alterações podem vir a ser solicitadas conforme o incremento seja alocado.

# 4. Modelagem ágil: 
Em diversas situações, engenheiros de software têm de desenvolver sistemas grandes e críticos para o negócio. Nesse contexto, podemos observar três pontos relevantes em que o escopo e a complexidade desses sistemas devem ser modelados, abaixo estão apresentados estes tópicos:

- Todas as partes envolvidas possam entender melhor quais requisitos devem ser atingidos;
- O problema possa ser subdividido eficientemente entre as pessoas que têm de solucioná-lo;
- A qualidade pode ser avaliada enquanto se está projetando e desenvolvendo o sistema.

Para Scott Ambler a modelagem ágil consiste em um conjunto de valores, princípios e práticas voltados para a modelagem do software que podem ser aplicados a um projeto de desenvolvimento de software de forma leve e eficiente. Os modelos ágeis são mais eficientes do que os tradicionais pelo fato de serem simplesmente bons, pois não têm a obrigação de ser perfeitos.

Para Pressmam e Maxim a filosofia da Modelagem Ágil reconhece que uma equipe ágil deve ter a coragem de tomar decisões que podem vir a causar a rejeição de um processo e sua refatoração. O grupo também deve ter humildade para reconhecer que os profissionais de tecnologia não possuem todas as respostas e que os experts em negócios e outros envolvidos devem ser respeitados e integrados ao processo.

PRINCÍPIOS DE MODELAGEM	DESCRIÇÃO
- Modelar com um objetivo: O desenvolvedor que utilizar a AM deve ter um objetivo antes de criar o modelo, mas uma vez identificado o objetivo, ficará mais evidente o tipo de notação a ser utilizado e o nível de detalhamento necessário.

- Usar vários modelos:	Há muitos modelos e notações diferentes que podem ser usados para descrever software. Para a maioria dos projetos, somente um subconjunto é essencial. A AM sugere que, para propiciar a percepção necessária, cada modelo deve apresentar um aspecto diferente do sistema e devem ser usados somente aqueles que valorizem esses modelos para o público pretendido.

- Viajar leve: Conforme o trabalho de engenharia de software prossegue, conserve apenas aqueles modelos que terão valor no longo prazo e se desfaçam do restante. Todo artefato mantido deve sofrer manutenção à medida que mudanças ocorram. Isso representa trabalho que retarda a equipe. Ambler [Amb02a] observa que “Toda vez que se opta por manter um modelo, troca-se a agilidade pela conveniência de ter aquela informação acessível para a equipe de uma forma abstrata (já que, potencialmente, aumenta a comunicação dentro da equipe, assim como com os envolvidos no projeto)”.

- Conteúdo é mais importante do que a representação: A modelagem deve transmitir informações para seu público pretendido. Um modelo sintaticamente perfeito que transmita pouco conteúdo útil não possui tanto valor quanto aquele com notações falhas que, no entanto, fornece conteúdo valioso para seu público-alvo.

- Conhecer os modelos e as ferramentas utilizadas para criá-los: Compreenda os pontos fortes e fracos de cada modelo e as ferramentas usadas para criá-lo.

- Adaptar localmente: A modelagem deve ser adaptada às necessidades da equipe ágil.

# 5. Processo unificado ágil
De acordo com Pressman e Maxim, o Processo Unificado Ágil (AUP, Agile Unified Process) adota uma filosofia “serial para o que é amplo” e “iterativa para o que é particular” no desenvolvimento de sistemas computadorizados. No quadro, será apresentado cada iteração AUP tratando das seguintes atividades:

- Modelagem: Representações UML do universo do negócio e do problema são criadas. Entretanto, para permanecerem ágeis, esses modelos devem ser “suficientemente bons e adequados” para possibilitar que a equipe prossiga.

- Implementação: Os modelos são traduzidos em código-fonte.

- Testes: Como a XP, a equipe projeta e executa uma série de testes para descobrir erros e assegurar que o código-fonte se ajuste aos requisitos.

- Entrega: Nesse contexto, a entrega se concentra no fornecimento de um incremento de software e na obtenção de feedback dos usuários.

- Configuração e gerenciamento de projeto: No contexto do AUP, gerenciamento de configuração refere-se a gerenciamento de alterações, de riscos e de controle de qualquer artefato persistente que seja produzido por uma equipe. O gerenciamento de projeto monitora e controla o progresso de uma equipe e coordena as suas atividades.

Gerenciamento do ambiente: Coordena a infraestrutura de processos que inclui padrões, ferramentas e outras tecnologias de suporte disponíveis para a equipe.