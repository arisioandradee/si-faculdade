# Engenharia de Software - Aula 04 (Resumo)

## 1. Um modelo de processo genérico
Segundo Pressman e Maxim,uma metodologia de processo genérica no contexto da engenharia de software define cinco atividades metodológicas: comunicação, planejamento, modelagem, construção e entrega. Além de um conjunto de atividades de apoio que é aplicado no decorrer do processo, como forma de acompanhamento e controle do projeto, a administração de riscos, a garantia da qualidade, o gerenciamento das configurações, as revisões técnicas, entre outras.

Um ponto importante do processo de software é conhecido como fluxo de processo. O Fluxo de processo descreve como são organizadas as atividades metodológicas, além das ações e tarefas que ocorrem dentro de cada atividade em relação à sequência e ao tempo. 

- Um fluxo de processo linear executa cada uma das cinco atividades metodológicas em sequência: comunicação, planejamento, modelagem, construção e entrega;
- Um fluxo de processo iterativo repete uma ou mais das atividades antes de seguir para a seguinte;
- Um fluxo de processo evolucionário executa as atividades de maneira “circular”. Cada volta pelas cinco atividades conduz a uma versão mais completa do software;
- Um fluxo de processo paralelo executa uma ou mais atividades em paralelo com as demais atividades.

## 2. Definição de uma atividade metodológica
Para executar as atividades do processo de software de forma eficiente, é essencial que a equipe tenha informações adequadas. Pressman e Maxim destacam uma questão crucial: determinar quais ações são apropriadas para uma atividade metodológica, considerando a natureza do problema, as características das pessoas envolvidas e os requisitos do projeto.

Para ilustrar, em um pequeno projeto de software com requisitos simples e uma única pessoa demandando o serviço, a atividade de comunicação pode ser resumida a um telefonema ou um e-mail. As ações necessárias incluem contatar o envolvido, discutir requisitos e gerar anotações, organizar essas anotações em uma lista de requisitos e enviar um e-mail para revisão e aprovação.

Em projetos mais complexos, com mais envolvidos, a atividade de comunicação pode exigir seis ações distintas: concepção, levantamento, elaboração, negociação, especificação e validação. Cada uma dessas ações envolve várias tarefas e gera uma variedade de artefatos específicos da engenharia de software.

## 3. Identificação de um conjunto de tarefas
Cada ação de engenharia de software, como por exemplo, a ação de levantamento, que é associada à atividade de comunicação, pode ser representada por vários e diferentes conjuntos de tarefas formados por uma sucessão de tarefas de trabalho de engenharia de software, artefatos relacionados, fatores de garantia da qualidade e marcos do projeto.

É necessário escolher um conjunto de tarefas que sejam mais adequadas às demandas do projeto e às características da equipe. De acordo com Pressman e Maxim, isso significa que uma ação de engenharia de software aplicada nesse contexto pode ser adaptada às especificidades do projeto de software e às características da equipe.

## 4. Padrões de processo
Em termos abstratos, um padrão de processo define um modelo, ou seja, um método no qual são descritas soluções de problemas no contexto do processo de software. Os padrões podem ser definidos em qualquer nível de abstração. Em determinados momentos, um padrão poderia ser utilizado para descrever um problema, além de sua solução associada ao modelo de processo completo como por exemplo, utilizando a prototipação. Em outras situações, os padrões podem ser usados para descrever um problema junto de sua solução associado a uma atividade metodológica como, por exemplo, o planejamento ou uma ação dentro de uma atividade metodológica como, por exemplo, estimativa de custos do projeto.

Ambler propôs um modelo para descrever um padrão de processo, no quadro a seguir estão apresentados os tópicos sugeridos:

- Nome do padrão: O padrão deve receber um nome que o descreva no contexto do processo de software (por exemplo, RevisõesTécnicas).

- Forças: Ambiente onde se encontram o padrão e as questões que tornam visível o problema e que poderiam afetar sua solução.	

- Tipo: É especificado o tipo de padrão.

- Padrão de estágio: Define um problema associado a uma atividade metodológica para o processo. Como uma atividade metodológica envolve várias ações e tarefas de trabalho, um padrão de estágio engloba vários padrões de tarefas relevantes ao estágio. Um exemplo de padrão de estágio poderia ser EstabelecimentoDeComunicação. Esse padrão poderia incorporar o padrão de tarefas LevantamentoDeRequisitos e outros.

- Padrão de tarefas: Define um problema associado a uma ação de engenharia de software ou tarefa de trabalho relevante para a prática de engenharia de software bem-sucedida (por exemplo, LevantamentoDeRequisitos é um padrão de tarefas).		

- Padrão de fases: Define a sequência das atividades metodológicas que ocorrem dentro do processo, mesmo quando o fluxo geral de atividades é iterativo por natureza. Um exemplo de padrão de fases seria ModeloEspiral ou Prototipação.

- Contexto inicial: Descreve as condições sob as quais o padrão se aplica. Antes do início do padrão: (1) Que atividades organizacionais ou relacionadas à equipe já ocorreram? (2) Qual é o estado inicial do processo? (3) Qual informação de engenharia de software ou de projeto já existe? Por exemplo, o padrão Planejamento (um padrão de estágio) exige que: (1) clientes e engenheiros de software tenham estabelecido uma comunicação colaborativa; (2) tenha ocorrido a finalização bem-sucedida de uma série de padrões de tarefas [especificados] para o padrão Comunicação; e (3) sejam conhecidos o escopo e as restrições do projeto, bem como os requisitos básicos do negócio.	

- Problema: O problema específico a ser resolvido pelo padrão. Descreva como implementar o padrão de forma bem-sucedida. Essa seção descreve como o estado inicial do processo (que existe antes de o padrão ser implementado) é modificado como consequência do início do padrão. 

- Solução: Descreve também como as informações de engenharia de software ou de projeto que se encontram à disposição antes do início do padrão são transformadas como consequência da execução bem-sucedida do padrão.

- Contexto resultante: Descreve as condições que resultarão assim que o padrão tiver sido implementado com êxito. Após a finalização do padrão: (1) Quais atividades organizacionais ou relacionadas à equipe devem ter ocorrido? (2) Qual é o estado de saída do processo? (3) Quais informações de engenharia de software ou de projeto foram desenvolvidas?

- Padrões relativos: Fornecem uma lista de todos os padrões de processo que estão diretamente relacionados ao processo em questão. Essa lista pode ser representada de forma hierárquica ou em alguma outra forma com diagramas. Por exemplo, o padrão de estágio Comunicação envolve os padrões de tarefas: EquipeDeProjeto, DiretrizesColaborativas, IsolamentoDoEscopo, LevantamentoDeRequisitos, DescriçãoDasRestrições e CriaçãoDeCenários.

- Usos conhecidos e exemplos: Indicam as instâncias específicas a que o padrão é aplicável. Por exemplo, Comunicação é obrigatória no início de todo projeto de software, é recomendável ao longo de todo o projeto de software e é obrigatória assim que a atividade Entrega estiver em andamento.

## 5. Avaliação e aperfeiçoamento de processos
Apesar de possuir um processo de software, isso não garante que o software seja entregue dentro do prazo estabelecido, nem que estará conforme as necessidades do cliente ou mesmo que apresentará características técnicas que resultarão em qualidade a longo prazo. Nesse contexto, é indicado que os padrões de processo sejam combinados com uma prática de engenharia de software confiável. Dessa maneira, o próprio processo pode ser avaliado para que esteja conforme um conjunto de critérios de processo básicos, comprovados como essenciais para uma engenharia de software bem-sucedida.

- SCAMPI: Fornece um modelo de avaliação do processo de cinco etapas, contendo cinco fases: início, diagnóstico, estabelecimento, atuação e aprendizado. O método SCAMPI usa o CMMI da SEI como base para avaliação [SEI00].

- CBA IPI: Fornece uma técnica de diagnóstico para avaliar a maturidade relativa de uma organização de software; usa a CMM da SEI como base para a avaliação [Dun01].

- SPICE (ISO/IEC15504):	Padrão que define um conjunto de requisitos para avaliação do processo de software. A finalidade do padrão é auxiliar as organizações no desenvolvimento de uma avaliação objetiva da eficácia de um processo qualquer de software [ISO08].

- ISO 9001:2000 para Software: Padrão genérico aplicável a qualquer organização que queira aperfeiçoar a qualidade global de produtos, sistemas ou serviços fornecidos. Portanto, o padrão é aplicável diretamente a organizações e empresas de software [Ant06].
			