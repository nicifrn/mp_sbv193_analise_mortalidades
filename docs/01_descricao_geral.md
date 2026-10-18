# Plano de trabalho - Onde o 193 SBV faria mais diferença? Análise de dados públicos de mortalidade no RN

**Estudante:** Anderson (@sirdom003-hub) - Técnico Integrado em Informática

**Orientadores:** Prof. Bruno Gomes (@brunogomesifrn) e Entony (@franciscoentony) - NIC/IFRN

**Repositório:** https://github.com/nicifrn/mp_sbv193_analise_mortalidades

**Período:** 16/10/2026 a 10/12/2026: 8 sprints de 1 semana (de sexta a quinta-feira). As duas primeiras são de aprendizado de Python.

**Projeto pai:** 193 SBV, plataforma digital para mobilização de socorristas voluntários no RN (resumo em [`docs/projeto_193sbv.md`](projeto_193sbv.md)).

**Trabalho escrito:** um **artigo**, no modelo de artigo do NIC que eu compartilho com você (parecido com o do TCC, mais simples), seguindo as normas de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

> **Leia este documento inteiro antes de começar a Sprint 1.** Ele é a referência completa do seu trabalho: tudo o que você vai estudar, programar, pesquisar e escrever está aqui, sprint por sprint. As *issues* do GitHub são o resumo de cada semana e sempre apontam para a seção correspondente deste documento. Se uma *issue* e este documento parecerem dizer coisas diferentes, **vale este documento**.

---

## Sumário

- [1. Como usar este documento e o quadro de tarefas](#como-usar)
- [2. A ideia do trabalho](#ideia)
- [3. Decisões já tomadas](#decisoes)
- [4. Cronograma](#cronograma)
- [5. Como trabalhar no repositório (fluxo do NIC)](#fluxo-git)
- [6. A estrutura de pastas que você vai construir](#estrutura)
- [7. Combinados que valem para todas as sprints](#combinados)
- [8. Como escrever o artigo](#escrita-geral)
- [Sprint 1 - Aprender Python, parte 1](#sprint-1-dev)
- [Sprint 2 - Aprender Python, parte 2](#sprint-2-dev)
- [Sprint 3 - Os dados do TABNET e do IBGE](#sprint-3-dev)
- [Sprint 4 - A limpeza dos dados, com testes](#sprint-4-dev)
- [Sprint 5 - A junção das tabelas e as taxas](#sprint-5-dev)
- [Sprint 6 - Os gráficos e a conferência com a fonte](#sprint-6-dev)
- [Sprint 7 - A conferência das taxas e a reprodutibilidade](#sprint-7-dev)
- [Sprint 8 - README, recomendação e fechamento](#sprint-8-dev)
- [9. Quadro-resumo](#quadro-resumo)
- [10. Riscos e planos B](#riscos)
- [11. Se sobrar tempo](#extras)
- [12. Referências mínimas do artigo](#referencias-minimas)

---

<a id="como-usar"></a>
## 1. Como usar este documento e o quadro de tarefas

### As *issues* e o quadro (kanban)

Eu cadastrei as suas tarefas como *issues* no repositório. Toda semana tem:

- **uma *issue* com a etiqueta `Desenvolvimento`**: o que você vai estudar, programar e testar;
- **uma *issue* com a etiqueta `Escrita`**: o que você vai pesquisar e escrever no artigo. Em seis semanas ela é a entrega de uma parte do texto. Em duas semanas (Sprints 1 e 6) não há entrega de seção nova, e a *issue* é uma tarefa menor: na Sprint 1, preparar o documento e fichar leituras; na Sprint 6, colocar no documento as tabelas e os gráficos com os dados das Sprints 5 e 6. Essas tarefas pequenas existem para o texto não ficar parado, porque **quem deixa os Resultados para o fim não entrega**.

As *issues* de uma semana estão agrupadas em um **marco** (*milestone*) com o nome e a data da sprint, por exemplo `Sprint 05 - Junção e taxas (13/11 a 19/11)`. A página **Milestones** do repositório mostra quanto de cada sprint já foi concluído.

O **quadro do projeto** (aba *Projects* do repositório) tem quatro colunas:

| Coluna | Quando o card fica aqui |
|---|---|
| **A fazer** | a tarefa ainda não começou |
| **Em andamento** | você está trabalhando nela. **Mova o card assim que começar** |
| **Em revisão** | você terminou e avisou os orientadores |
| **Concluído** | os orientadores aprovaram e fecharam a *issue* |

### Como cada sprint está organizada neste documento

Cada sprint tem duas partes, **Desenvolvimento** e **Escrita**, e cada uma tem um endereço próprio (`#sprint-4-dev`, `#sprint-4-escrita`), que é para onde as *issues* apontam.

A parte de desenvolvimento tem sempre os mesmos blocos:

- **O que você vai entregar**: em uma frase, o que precisa estar funcionando no fim da semana;
- **Divida a semana assim**: uma sugestão de distribuição dos passos pelos dias;
- **Passo a passo**: a lista numerada do que fazer, na ordem. Siga na ordem, sem pular;
- **Como saber que deu certo**: o que você deve ver na tela ou no arquivo. Se não vir isso, ainda não terminou;
- **Entrega da sprint**: a lista de conferência que também está na *issue*;
- **Erros comuns**: os problemas mais prováveis da semana e como resolver.

**Neste documento eu não dou os programas prontos.** Eu digo o que cada programa precisa fazer, em que ordem, quais funções usar e o que pesquisar. Quem escreve o código é você, e é isso que faz o trabalho ser seu. As fórmulas aparecem completas, porque são o objeto de estudo e vão para o artigo. Os trechos de Python são **peças**: uma chamada de função que não dá para adivinhar, um esqueleto com comentários. Quando uma peça aparece inteira, é porque ela esconde uma armadilha técnica que eu já conferi e que não vale a pena você descobrir sozinho.

### Como entregar

**Desenvolvimento:**

1. abra um *pull request* (PR) da *branch* da sprint para a `develop`, seguindo a [seção 5](#fluxo-git), com `Closes #N` na descrição (o número N de cada sprint está indicado na própria sprint);
2. comente na *issue*: `@brunogomesifrn @franciscoentony entrega da Sprint N pronta para revisão - PR #X`;
3. mova o card para **Em revisão**.

Quando um de nós aprovar e fizer o *merge* do PR, a *issue* fecha sozinha e o card vai para **Concluído**. Se pedirmos ajustes, faça os ajustes na mesma *branch* (o PR se atualiza sozinho) e comente de novo.

**Escrita:**

1. escreva no documento do Google Drive (veja a [seção 8](#escrita-geral));
2. nomeie a versão no histórico do Drive (*Arquivo → Histórico de versões → Nomear versão atual*), por exemplo `Entrega 1 - Introdução - 29/10`;
3. comente na *issue*: `@brunogomesifrn @franciscoentony Introdução pronta para revisão - versão "Entrega 1 - Introdução - 29/10"`;
4. mova o card para **Em revisão**.

Nós comentamos no próprio documento do Drive. Quando a seção estiver aprovada, fechamos a *issue*.

### Regras de ouro

- **Entregue no prazo, mesmo incompleto.** Trabalho pela metade dá para revisar; trabalho que não chega, não. Na *issue*, diga o que ficou faltando.
- **Terminou antes? Não comece a próxima sprint.** Use o tempo para refazer os exercícios que achou difíceis, para entender melhor o que fez e para adiantar a escrita.
- **Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Comente na *issue* da semana, marcando nós dois, com: o que estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada** (não um resumo, nem um print cortado). Neste trabalho isso é ainda mais importante: uma linha de "Total" esquecida na tabela, um município que sumiu na junção ou um ano a mais no período **não geram mensagem de erro**, só um número errado. Pedir ajuda depois de 40 minutos não é desistir, é administrar o tempo.

---

<a id="ideia"></a>
## 2. A ideia do trabalho

### O problema

O projeto 193 SBV parte de uma afirmação: **o socorro nos primeiros minutos salva vidas**. Em uma parada cardíaca, cada minuto sem massagem cardíaca reduz muito a chance de a pessoa sobreviver, e a ambulância quase nunca chega nesses primeiros minutos. Por isso o projeto quer acionar voluntários treinados que estejam perto da vítima.

Mas o RN tem 167 municípios. **Em quais deles esse problema pesa mais?** É ali que faz mais sentido começar a captar voluntários.

Os dados para responder existem e são públicos:

- o **DATASUS**, do Ministério da Saúde, publica quantas pessoas morreram, por causa e por município, no **Sistema de Informações sobre Mortalidade (SIM)**, consultado pela ferramenta **TABNET**;
- o **IBGE** publica a população de cada município.

O problema é que **os números absolutos enganam**. Natal sempre terá mais óbitos que qualquer outro município, simplesmente porque tem mais gente. Para comparar municípios de tamanhos diferentes de forma justa, é preciso calcular uma **taxa**: quantos óbitos houve para cada 100 mil habitantes.

A pergunta que o seu trabalho responde é:

> **Em quais municípios do Rio Grande do Norte a mortalidade por causas em que o socorro imediato faz diferença é maior, quando se compara de forma justa, pela taxa por 100 mil habitantes?**

### O que você vai construir

Um programa em Python, com a biblioteca `pandas`, que:

1. **lê e limpa** os arquivos baixados do TABNET e do IBGE (linhas de título e de rodapé, linha de "Total", o código grudado no nome do município, valores ausentes marcados com `-`);
2. **junta** as duas tabelas pelo **código do município** (e não pelo nome, e você vai descobrir por quê);
3. **calcula a taxa** de mortalidade por 100 mil habitantes de cada município;
4. **gera a lista dos 10 municípios** com maior taxa e os **gráficos de barras** com o Matplotlib.

### O que vai ser medido (é isso que faz o trabalho ser um artigo, e não um relatório)

| O que | Como |
|---|---|
| **Absoluto contra taxa** | Quanto muda a lista dos "piores" municípios quando se troca o número de óbitos pela taxa |
| **Municípios prioritários** | Os 10 municípios com maior taxa, e onde eles ficam no estado |
| **Conferência com a fonte** | Para 10 municípios, os totais do programa comparados com os que o próprio TABNET mostra. Meta: **100% iguais** |
| **Conferência das taxas** | Para 5 municípios, a taxa calculada à mão em uma planilha comparada com a do programa. Meta: **100% iguais** |
| **Reprodutibilidade** | O programa rodado de novo, em outra pasta, a partir só dos arquivos guardados no repositório, dá **os mesmos números** |
| **Estabilidade** | Quanto a taxa de um município pequeno varia de um ano para o outro, comparada com a de um município grande |

### O que este trabalho **não** é

**Não é o aplicativo 193 SBV.** O aplicativo é o **contexto** que justifica a pergunta. O objeto do artigo é a **análise dos dados**, feita por um programa testado e conferido. Você não mexe no código do aplicativo. Escreva isso na Introdução.

**Não é um estudo médico.** Você não vai dizer por que as pessoas morreram nem quantas mortes o 193 SBV evitaria. Você vai mostrar **onde** os óbitos por essas causas pesam mais, com dados oficiais, e com um processo que qualquer pessoa pode repetir.

**Não usa dados de pessoas.** Os dados do TABNET e do IBGE são públicos e **agregados** (contagens por município): não há nome, endereço nem nenhum dado que identifique alguém. Por isso o trabalho não precisa passar pelo Comitê de Ética em Pesquisa. As entrevistas com profissionais do Corpo de Bombeiros, previstas na Meta I do projeto, ficam como trabalho futuro.

---

<a id="decisoes"></a>
## 3. Decisões já tomadas

Para você não perder tempo escolhendo:

| Item | Decisão |
|---|---|
| Linguagem | **Python 3** (3.10 ou mais novo) |
| Onde você trabalha | **computadores do laboratório (Windows)**. Não é possível instalar programas, mas o `pip install` e o Git funcionam |
| Editor | **VS Code** |
| Como aprender Python | **Curso de Python 3 do Curso em Vídeo** (gratuito), nas Sprints 1 e 2, com exercícios deste plano |
| Fonte dos óbitos | **DATASUS, TABNET, Sistema de Informações sobre Mortalidade (SIM)**, "Mortalidade geral", abrangência Rio Grande do Norte, **óbitos por residência** |
| Causas | **I21 (infarto agudo do miocárdio)** e **I46 (parada cardíaca)**, da CID-10. A justificativa da escolha é sua, no Referencial Teórico (Sprint 3) |
| Período | **2020 a 2024**: os cinco anos mais recentes com **dados finais** no TABNET. Os anos de 2025 e 2026 aparecem no TABNET, mas são **preliminares** (ainda mudam) e **não entram** |
| Fonte da população | **IBGE, Censo Demográfico 2022**, tabela 4709 do SIDRA |
| Taxa | **taxa média anual por 100 mil habitantes** (fórmula abaixo) |
| Download | **manual**, pelo navegador, com cada clique registrado em um protocolo (`docs/protocolo_download.md`). Os arquivos baixados ficam no repositório, **sem nenhuma alteração**, em `dados/brutos/` |
| Bibliotecas | `pandas`, `matplotlib`, `requests` (só nos exercícios) e `pytest`. Todas pelo `pip` |
| Validação | conferência com o TABNET (10 municípios), conferência das taxas em planilha (5 municípios), testes com `pytest` e reprodutibilidade |
| Repositório | `nicifrn/mp_sbv193_analise_mortalidades`, só seu, seguindo a política de desenvolvimento do NIC ([seção 5](#fluxo-git)) |
| Texto | **artigo**, no modelo do NIC, em um documento do Google Drive que eu compartilho com você |
| O que **não** entra | banco de dados, Django, aplicativo, mapas, aprendizado de máquina, dados de pessoas, entrevistas e questionários |

### A fórmula da taxa

Você vai somar os óbitos dos cinco anos e dividir pela população do Censo de 2022 multiplicada por cinco:

```
                          óbitos de 2020 a 2024 (I21 + I46)
taxa média anual  =  ---------------------------------------  ×  100 000
                          população do Censo 2022  ×  5
```

Por que assim:

- **por que somar cinco anos:** em um município pequeno, um ano pode ter 1 óbito e o seguinte, 8. Somando cinco anos, a taxa fica mais estável. Na Sprint 7 você vai medir essa instabilidade;
- **por que a população de 2022:** 2022 é o **ano do meio** do período (2020, 2021, **2022**, 2023, 2024), e o Censo é a contagem mais confiável da população. Usar a população do meio do período é a forma usual de calcular uma taxa de vários anos;
- **por que multiplicar a população por 5:** cada habitante "esteve exposto" durante cinco anos. Sem o 5, a taxa seria de cinco anos juntos, e não poderia ser comparada com taxas anuais de outros trabalhos;
- **por que 100 mil:** é a convenção para causas de morte. A taxa por habitante daria números como 0,00059, difíceis de ler.

Exemplo com números inventados: um município com 30 000 habitantes e 45 óbitos nos cinco anos tem taxa de 45 / (30 000 × 5) × 100 000 = **30,0 óbitos por 100 mil habitantes por ano**.

### Uso de inteligência artificial

- **Pode:** usar uma ferramenta de IA para entender uma mensagem de erro ou um conceito, como faria com um colega.
- **Não pode:** pedir para a IA escrever os programas, os exercícios ou o texto do artigo. O código e o texto têm de ser seus, e você precisa saber explicar cada linha na apresentação. Nas duas semanas de aprendizado isso vale em dobro: exercício resolvido pela IA é aula perdida.
- **Nunca:** colocar no artigo uma referência que você não abriu e leu. Ferramentas de IA inventam referências com naturalidade e, nesta área, inventam também números de óbitos e códigos da CID-10.

---

<a id="cronograma"></a>
## 4. Cronograma

Cada sprint vai de **sexta a quinta-feira**. O prazo de tudo é a **quinta-feira** que fecha a sprint.

| Sprint | Período | Desenvolvimento | Escrita |
|---|---|---|---|
| 1 | 16/10 a 22/10 | Aprender Python, parte 1 (Git, ambiente e o básico) | Preparar o documento e fichar as leituras da Introdução |
| 2 | 23/10 a 29/10 | Aprender Python, parte 2 (listas, `pandas`, gráfico, `pytest`) | **Entrega 1:** Introdução e Objetivo geral |
| 3 | 30/10 a 05/11 | Os dados do TABNET e do IBGE: download e exploração | **Entrega 2:** Referencial 2.1 e 2.2 |
| 4 | 06/11 a 12/11 | A limpeza dos dados, com testes | **Entrega 3:** Referencial 2.3 e 2.4 |
| 5 | 13/11 a 19/11 | A junção das tabelas e as taxas | **Entrega 4:** Metodologia |
| 6 | 20/11 a 26/11 | Os gráficos e a conferência com o TABNET | Tarefa curta: tabelas e gráficos no documento |
| 7 | 27/11 a 03/12 | A conferência das taxas, a estabilidade e a reprodutibilidade | **Entrega 5:** Resultados e Discussão |
| 8 | 04/12 a 10/12 | README, recomendação e fechamento | **Entrega 6:** Conclusão, Objetivos específicos, Resumo e Título |

**Tudo termina em 10/12.**

**Feriados:** 02/11 (segunda, Sprint 3) e 20/11 (sexta, primeiro dia da Sprint 6). Nenhum prazo cai em feriado, mas nessas duas semanas o laboratório fica fechado um dia: **a semana tem um dia útil a menos**, então comece cedo.

**Três avisos sobre o cronograma:**

1. **A Sprint 1 começa na sexta, 16/10, mas você começa na segunda, 19/10.** A semana é mais curta: siga a divisão por dias da própria sprint, que já leva isso em conta.
2. **Os Resultados vencem em 03/12, na mesma semana das últimas conferências.** Por isso a Sprint 6 já manda colocar no documento as tabelas e os gráficos que existirem, e a Sprint 7 manda terminar as tabelas e os gráficos novos **até segunda-feira, 30/11**: a terça fica para a reprodutibilidade (que só confere o que já existe), e a quarta e a quinta ficam para escrever.
3. **A última semana é cheia.** A Conclusão precisa estar escrita até **segunda-feira, 07/12**, para sobrar a terça, a quarta e a quinta para o Resumo, o Título e a revisão final.

---

<a id="fluxo-git"></a>
## 5. Como trabalhar no repositório (fluxo do NIC)

O NIC tem uma política de desenvolvimento que vale para todos os projetos. Abaixo está o que ela significa no seu trabalho.

### 5.1 As *branches*

| *Branch* | Para que serve | Quem mexe |
|---|---|---|
| `main` | versão estável e aprovada | só os orientadores, no fim do trabalho |
| `develop` | onde as sprints aprovadas vão se juntando. É a *branch* padrão do repositório | ninguém envia direto: só entra por PR aprovado |
| `feature/...` | **uma por sprint**, onde você trabalha | você |

Os nomes das *branches* das sprints já estão definidos em cada sprint (por exemplo, `feature/limpeza-dados`). Se precisar corrigir algo de uma sprint que já foi aprovada, use `fix/` (por exemplo, `fix/linha-total`).

### 5.2 O ciclo de cada sprint

**No começo da sprint** (sexta-feira), crie a *branch* da semana a partir da `develop` atualizada e envie para o GitHub:

```
git checkout develop
git pull
git checkout -b feature/nome-da-sprint
git push -u origin feature/nome-da-sprint
```

O `git pull` traz para a sua máquina o que foi aprovado na sprint anterior. **Se o PR da sprint anterior ainda não foi aprovado** quando a sprint nova começar, crie a *branch* nova a partir da *branch* da sprint anterior (troque `develop` por ela no primeiro comando) e avise na *issue*.

**Ao fim de cada dia**, envie o trabalho. Código que só existe na máquina do laboratório não foi entregue, e a máquina pode ser formatada:

```
git status
git add (os arquivos que você mexeu)
git commit -m "feat: adiciona cálculo da taxa por 100 mil habitantes"
git push
```

**Antes de todo `git add`, olhe o `git status`.** Se aparecer `.venv/` ou `__pycache__/`, o `.gitignore` está errado: corrija antes de continuar. **Nunca use `git add .` sem olhar o `git status` antes.**

Se você trabalhar em mais de uma máquina do laboratório, comece sempre com `git pull` na *branch* da sprint, para trazer o que enviou da outra máquina.

**No fim da sprint**, abra o PR (seção 5.4).

### 5.3 Mensagens de *commit*

Os *commits* devem ser **pequenos, objetivos e frequentes**: pelo menos 3 por semana. Use o padrão abaixo, com a mensagem em português e o verbo no presente:

```
feat: adiciona leitura do arquivo do TABNET
fix: remove a linha de total antes da soma
docs: registra o protocolo de download do TABNET
test: adiciona testes da limpeza dos dados
refactor: move as funções de limpeza para mortalidade.py
```

| Prefixo | Quando usar |
|---|---|
| `feat:` | algo novo funcionando (um exercício, um script, uma função, uma coluna nova) |
| `fix:` | correção de algo que estava errado |
| `docs:` | documentação, diário, `README.md`, protocolo, prints, tabelas e gráficos de resultado |
| `test:` | testes |
| `refactor:` | reorganizar código sem mudar o que ele faz |

Os arquivos baixados do TABNET e do IBGE entram com `docs:` ou `feat:`, por exemplo: `feat: adiciona arquivos brutos do TABNET e do IBGE`.

**Mensagens proibidas pela política do NIC:** `ajustes`, `mudanças`, `update`, `correções`. Se você não consegue dizer em uma frase o que o *commit* faz, ele está grande demais.

### 5.4 O *pull request* do fim da sprint

1. Confira se tudo foi enviado (`git status` deve dizer `nothing to commit`).
2. Rode os testes (a partir da Sprint 2): `python -m pytest`. Todos precisam passar.
3. No GitHub, abra o repositório. Vai aparecer uma faixa amarela com o botão **Compare & pull request**. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a *branch* da sprint**.
4. Preencha a descrição. O repositório já traz um modelo com os campos que a política do NIC exige:
   - **Objetivo:** o que esta sprint entrega, em uma ou duas frases;
   - **O que foi feito:** a lista do que foi implementado;
   - **Possíveis impactos:** o que muda para quem roda o projeto (um script novo, uma pasta nova, uma biblioteca nova);
   - **Evidências de teste:** a saída do `pytest` e dos scripts (copiadas do terminal), as tabelas e os gráficos;
   - **Issue:** `Closes #N`, com o número indicado na sprint.
5. Em **Reviewers**, marque `brunogomesifrn` e `franciscoentony`.
6. Comente na *issue* e mova o card para **Em revisão** (veja a [seção 1](#como-usar)).

**Você não faz o *merge* do próprio PR**: a política do NIC exige que um revisor aprove antes da integração, e os revisores somos nós. **Um PR por sprint**: não acumule duas sprints no mesmo PR.

### 5.5 Testes

A política do NIC pede que toda funcionalidade tenha testes compatíveis com a sua complexidade. No seu trabalho, as funções de limpeza e de cálculo ficam em `mortalidade.py` e os testes ficam na pasta `tests/`, usando a biblioteca **`pytest`**. Um teste é uma função cujo nome começa com `test_` e que usa o comando `assert`:

```python
def test_taxa_por_100_mil():
    assert calcular_taxa(45, 30000, 5) == pytest.approx(30.0)
```

Se a condição do `assert` for **verdadeira**, o teste passa. Se for **falsa**, o `pytest` mostra qual teste falhou, o valor esperado e o valor obtido. O `pytest.approx` serve para comparar números decimais com uma tolerância, porque contas com decimais no computador não são exatas.

Rode sempre **a partir da raiz do repositório**, com o `.venv` ativo, assim:

```
python -m pytest
```

(Com `python -m` na frente, o Python enxerga os arquivos da raiz, e o `from mortalidade import ...` dos testes funciona.)

**Os testes não usam os arquivos de verdade nem a internet.** Eles testam as funções com tabelas pequenas que você inventa (3 municípios, 2 anos) e com um arquivo "de mentirinha" no formato do TABNET, com poucas linhas. É isso que deixa o teste rápido e confiável: você sabe de cabeça qual é a resposta certa.

### 5.6 Segurança

Nunca envie para o repositório senhas, *tokens*, chaves ou arquivos `.env`. Neste trabalho você não precisa de nenhum deles: o TABNET, o SIDRA e a API do IBGE não pedem cadastro.

Os arquivos de `dados/brutos/` **podem e devem** ir para o repositório: são dados públicos, agregados por município, sem nenhuma informação de pessoas, e pequenos (poucos kB). Sem eles, ninguém consegue repetir o seu trabalho.

---

<a id="estrutura"></a>
## 6. A estrutura de pastas que você vai construir

Você não precisa criar tudo de uma vez: cada sprint cria a sua parte. Esta é a figura final, para você saber aonde está indo. Tudo fica **na raiz do repositório** `mp_sbv193_analise_mortalidades/`:

```
mp_sbv193_analise_mortalidades/
├── .github/
│   └── pull_request_template.md     ← já existe (modelo do PR)
├── aprendizado/
│   ├── exemplo_municipios.csv       ← já existe (dados para os exercícios da Sprint 2)
│   ├── semana1/                     ← exercícios da Sprint 1
│   └── semana2/                     ← exercícios da Sprint 2
├── dados/
│   ├── brutos/                      ← os arquivos do TABNET e do IBGE, sem mexer (Sprints 3 e 6)
│   ├── obitos_limpos.csv            ← Sprint 4
│   ├── populacao_limpa.csv          ← Sprint 4
│   ├── obitos_i21_limpos.csv        ← Sprint 5
│   ├── obitos_i46_limpos.csv        ← Sprint 5
│   ├── regioes.csv                  ← Sprint 6
│   ├── conferencia_tabnet.csv       ← digitado por você (Sprint 6)
│   └── conferencia_planilha.csv     ← exportado da planilha (Sprint 7)
├── resultados/                      ← tabelas de resultado (Sprints 5 a 7)
├── graficos/                        ← gráficos do artigo (Sprints 6 e 7)
├── tests/
│   ├── tabnet_mini.csv              ← arquivo pequeno de teste (Sprint 4)
│   └── test_mortalidade.py          ← Sprints 4 e 5
├── docs/
│   ├── 01_descricao_geral.md        ← este documento (já existe)
│   ├── projeto_193sbv.md            ← já existe
│   ├── orientacoes_escrita_tcc.md   ← já existe
│   ├── ambiente.md                  ← Sprint 1
│   ├── diario.md                    ← Sprint 1 em diante
│   ├── leituras.md                  ← Sprint 1 em diante
│   ├── protocolo_download.md        ← Sprint 3
│   ├── recomendacao.md              ← Sprint 8
│   └── evidencias/                  ← prints de tela
├── mortalidade.py                   ← as funções de limpeza e de cálculo (Sprints 4 e 5)
├── verificar_ambiente.py            ← Sprint 1
├── explorar_dados.py                ← Sprint 3
├── limpar_dados.py                  ← Sprint 4
├── experimento_nomes.py             ← Sprint 5
├── analisar.py                      ← Sprints 5 e 6
├── graficos.py                      ← Sprint 6
├── regioes.py                       ← Sprint 6
├── conferir_tabnet.py               ← Sprint 6
├── conferir_planilha.py             ← Sprint 7
├── estabilidade.py                  ← Sprint 7
├── .gitignore
├── requirements.txt
└── README.md
```

A ideia da organização: **as funções** (ler o arquivo do TABNET, separar código e nome, calcular a taxa...) ficam todas em `mortalidade.py`, que é o arquivo testado pelo `pytest`. **Os scripts** (`limpar_dados.py`, `analisar.py`, `graficos.py`...) leem os arquivos, chamam as funções e gravam os resultados. Separar "fazer a conta" de "ler e gravar arquivo" é o que permite testar as contas com tabelas pequenas.

**Os arquivos de `dados/brutos/` nunca são editados**, nem para "consertar" uma linha. Toda limpeza é feita pelo programa. É isso que permite a qualquer pessoa repetir o trabalho a partir do mesmo arquivo baixado.

---

<a id="combinados"></a>
## 7. Combinados que valem para todas as sprints

- **Rode tudo a partir da raiz do repositório:** `python analisar.py`, e não de dentro de outra pasta. Todos os caminhos dos programas (`dados/`, `resultados/`, `graficos/`) partem da raiz.
- **Diário (`docs/diario.md`):** no fim de cada sprint, escreva 3 linhas: o que funcionou, o que deu errado e o que aprendeu. Leva cinco minutos e vai escrever a Conclusão por você no fim do trabalho. Use este formato:

  ```
  ## Sprint 4 - 06/11 a 12/11
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ```

  Além das três linhas, o diário guarda as **anotações técnicas** que cada sprint pede (contagens de linhas, totais, observações sobre os arquivos). Elas viram texto do artigo.

- **Confira os totais.** Este é um trabalho de contagem. Toda vez que uma tabela mudar de forma (limpeza, junção), confira se a **soma dos óbitos** e o **número de municípios** continuam os mesmos. Se mudaram e você não sabe explicar por quê, tem erro no código, mesmo sem mensagem de erro.
- **Anote todo erro e toda surpresa.** Neste trabalho, **surpresa é resultado**. Se um município pequeno apareceu no topo da lista, se uma cidade grande ficou abaixo da média do estado, isso vai para o artigo.
- **Prints (`docs/evidencias/`):** sempre que algo funcionar (ou falhar de um jeito interessante), tire um print (`Win + Shift + S`). Dê nomes que digam o que é: `s03_tabnet_formulario.png`.
- **Acompanhamento semanal:** no começo de cada sprint, você mostra aos orientadores o que fez na anterior, **rodando na tela**. A partir da Sprint 4, "está funcionando" não basta: tem que ter número.

---

<a id="escrita-geral"></a>
## 8. Como escrever o artigo

### 8.1 Onde escrever: o documento compartilhado no Google Drive

Na Sprint 1 eu compartilho com você um documento do Google Drive que **já está no modelo de artigo do NIC**: parecido com o do TCC, mas mais simples. Não há limite de páginas: escreva o necessário para explicar bem, sem enrolar. Você não cria arquivo novo nem trabalha em cópia local.

- **Escreva sempre no documento compartilhado.** Nada de escrever no Word e colar depois: o histórico do Drive é o que nos permite ver o que mudou de uma semana para outra.
- **Não crie cópias** ("Artigo v2", "Artigo final"). O Drive já guarda tudo em **Arquivo → Histórico de versões**.
- **Marque cada entrega no histórico:** *Arquivo → Histórico de versões → Nomear versão atual*, com um rótulo como `Entrega 1 - Introdução - 29/10`.
- **Avise na *issue* quando entregar**, como explicado na [seção 1](#como-usar).
- **Comentário se responde, não se apaga.** Responda a cada comentário dizendo o que fez e só então marque como resolvido.
- **Resolva todos os comentários da entrega anterior antes de avisar sobre a próxima.**
- **Figuras e tabelas** vão dentro do documento, no lugar certo, com a identificação em cima e a fonte embaixo.
- **Não dê acesso ao documento a outras pessoas.**

### 8.2 As normas

Todas as regras de escrita e de ABNT estão em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras, tabelas, formatação e linguagem. **Leia esse arquivo inteiro na Sprint 1.** Ele foi escrito para o TCC e vale para o artigo do mesmo jeito; a diferença é que o artigo é mais curto e tem menos subseções. Este plano não repete as regras da ABNT; ele diz **o que pesquisar e o que escrever** em cada seção.

> **Importante:** o que está neste plano são **orientações**, não o texto pronto. Não copie estas frases para o artigo. Elas dizem sobre o que é cada parágrafo; o texto tem de ser escrito por você, com as suas palavras e com as referências que leu.

### 8.3 A estrutura do artigo

```
1 INTRODUÇÃO
1.1 Objetivo geral
1.2 Objetivos específicos
2 REFERENCIAL TEÓRICO
2.1 Parada cardíaca, Suporte Básico de Vida e o tempo de resposta
2.2 O Sistema de Informações sobre Mortalidade e a CID-10
2.3 Indicadores de mortalidade: números absolutos e taxas
2.4 Trabalhos relacionados
3 METODOLOGIA
3.1 Classificação da pesquisa
3.2 Fontes de dados e ferramentas
3.3 Etapas do processamento
3.4 Validação
4 RESULTADOS E DISCUSSÃO
4.1 Os dados obtidos
4.2 Números absolutos e taxas
4.3 Os municípios com maiores taxas
4.4 Validação e reprodutibilidade
4.5 Limitações
5 CONCLUSÃO
REFERÊNCIAS
```

O artigo junta "Metodologia" e "Materiais e Métodos" em uma seção só (a 3). Tudo o que o [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) diz sobre as duas vale para ela.

### 8.4 As três perguntas de pesquisa

O trabalho gira em torno de três perguntas, que saem da pergunta principal da [seção 2](#ideia). Elas aparecem na Introdução, organizam os Resultados e são respondidas na Conclusão:

1. **quais municípios** do RN têm as maiores taxas de mortalidade por infarto agudo do miocárdio e parada cardíaca, de 2020 a 2024?
2. a lista dos municípios prioritários **muda** quando se troca o número absoluto de óbitos pela taxa por 100 mil habitantes? Quanto?
3. o resultado é **confiável**: confere com a fonte, as contas estão certas, o processo se repete, e quão estável é a taxa dos municípios pequenos?

### 8.5 Regras que valem para o texto inteiro

- **Toda afirmação técnica precisa de referência.**
- **Não empilhe citações.** Explique com as suas palavras e amarre ao seu trabalho.
- **Documentação oficial** (DATASUS, IBGE, documentação do `pandas`) serve para descrever a fonte de dados e as ferramentas, não para fundamentar conceito. Para conceito, use livro ou artigo.
- **Nada de blog, Stack Overflow ou site sem autoria** nas Referências. Você vai usar muito esse material para resolver problema técnico, e isso é normal, mas ele não entra na lista.
- **Nunca cite uma referência que você não leu.**
- **Crie a seção "Referências" no primeiro dia** e acrescente cada obra assim que ler.
- **Meta:** de 12 a 18 referências, equilibradas entre o lado da saúde e o lado técnico (lista mínima na [seção 12](#referencias-minimas)).
- **Fichamento:** tudo o que você ler vai para `docs/leituras.md`, no formato abaixo. É ele que transforma leitura em texto:

  ```
  ## LARSEN et al. (1993)
  - Referência completa (ABNT): ...
  - Onde achei: (endereço)
  - Ideia principal, com as minhas palavras: ...
  - Trecho que posso citar (com página): "..." (p. X)
  - Vou usar na seção: 2.1
  ```

---

# Sprint 1: 16/10 a 22/10/2026

<a id="sprint-1-dev"></a>
## Sprint 1 · Desenvolvimento: aprender Python, parte 1

**Branch:** `feature/aprendizado-semana1` · **No PR:** `Closes #1`

**O que você vai entregar:** o Git configurado, o repositório clonado, o ambiente virtual com as bibliotecas, o programa que confere o ambiente e **seis exercícios de Python**, todos sobre óbitos, população e taxas.

**Esta semana e a próxima são de aprendizado.** Você não precisa saber Python para começar: precisa assistir às aulas indicadas, digitar os exemplos junto com o professor e fazer os exercícios. Os exercícios são pequenos de propósito, e cada um é uma versão em miniatura de algo que o seu programa vai fazer nas Sprints 3 a 8.

**Divida a semana assim** (você começa na segunda):

| Dia | O que fazer |
|---|---|
| segunda, 19/10 | passos 1 a 4 (leitura do plano, Git, convite, clone e *branch*) |
| terça, 20/10 | passos 5 e 6 (ambiente, pastas, `verificar_ambiente.py`); começar as aulas do Mundo 1 |
| quarta, 21/10 | passo 7 (aulas do Mundo 1 até condições) e exercícios 1 a 3 |
| quinta, 22/10 | aulas de repetição (Mundo 2), exercícios 4 a 6, diário, *commits* e PR; a escrita da semana |

A semana é curta. Se não der tempo de assistir a todas as aulas de repetição, faça os exercícios 4 a 6 com o que já viu e termine as aulas na sexta, 23/10, antes de começar a Sprint 2.

### Passo a passo

**1. Leia as seções 1 a 8 deste documento inteiras.** Depois aprenda o básico de Git e GitHub: assista às aulas iniciais do Curso de Git e GitHub do Curso em Vídeo (https://www.cursoemvideo.com/curso/curso-de-git-e-github/), até a parte em que o repositório é enviado para o GitHub. Releia a [seção 5](#fluxo-git) depois das aulas.

**2. Configure o Git** na máquina do laboratório (uma vez só por máquina), com o mesmo e-mail da sua conta do GitHub. Abra o Prompt de Comando (tecla `Win`, digite `cmd`, Enter):

```
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-do-github@exemplo.com"
```

**3. Aceite o convite do repositório.** Você recebeu por e-mail um convite para o `nicifrn/mp_sbv193_analise_mortalidades`. Aceite (ou abra https://github.com/nicifrn/mp_sbv193_analise_mortalidades/invitations). Aceite também o convite do quadro do projeto, que chega no mesmo e-mail.

**4. Clone o repositório e crie a *branch* da sprint:**

```
cd %USERPROFILE%
git clone https://github.com/nicifrn/mp_sbv193_analise_mortalidades.git
cd mp_sbv193_analise_mortalidades
git checkout -b feature/aprendizado-semana1
git push -u origin feature/aprendizado-semana1
```

Na primeira vez que o Git falar com o GitHub, abre uma janela do navegador pedindo login. Entre com a sua conta e autorize. Abra a pasta `mp_sbv193_analise_mortalidades` no VS Code (*File → Open Folder*). A partir de agora, **é sempre essa pasta que você abre**.

**5. Crie o ambiente virtual e instale as bibliotecas.** O ambiente virtual é uma "caixa" só deste projeto, onde as bibliotecas ficam instaladas sem bagunçar o Python da máquina. Na raiz do repositório, **no Prompt de Comando** (e não no PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
pip install pandas matplotlib requests pytest
pip freeze > requirements.txt
```

Depois de ativar, o começo da linha passa a mostrar `(.venv)`. **Se não mostrar, o ambiente não está ativo**, e o que você instalar vai para o lugar errado. Toda vez que abrir um terminal novo, ative de novo.

Para que serve cada biblioteca:

| Biblioteca | Para quê |
|---|---|
| `pandas` | ler, limpar, juntar e calcular as tabelas. É a ferramenta principal do trabalho |
| `matplotlib` | fazer os gráficos de barras |
| `requests` | consultar a API do IBGE (nos exercícios e na Sprint 6) |
| `pytest` | rodar os testes automatizados |

O `requirements.txt` guarda a lista das bibliotecas **com as versões exatas** que você instalou. Na Sprint 7 ele vai ser essencial: é com ele que outra pessoa instala exatamente as mesmas versões e obtém os mesmos números.

> No terminal do VS Code (`` Ctrl + ` ``), abra o seletor de terminal (setinha ao lado do `+`) e escolha **Command Prompt**. No PowerShell, o `activate` costuma dar erro de "execução de scripts desabilitada".
>
> Se o comando `python` não for reconhecido, tente `py`. Se o `py` funcionar, use `py` no lugar de `python` em todos os comandos deste documento, e anote isso no diário.

**6. Crie as pastas, o `.gitignore` e o programa que confere o ambiente.**

1. Crie as pastas `aprendizado\semana1`, `aprendizado\semana2`, `dados\brutos`, `resultados`, `graficos`, `tests` e `docs\evidencias` (veja a [seção 6](#estrutura)). *Pesquise:* o comando `mkdir` no Windows. O Git não guarda pastas vazias; por isso, coloque dentro de cada pasta vazia um arquivo vazio chamado `.gitkeep`.
2. Crie o arquivo `.gitignore` na raiz, com este conteúdo:

   ```
   .venv/
   __pycache__/
   *.pyc
   .pytest_cache/
   ```

   Repare que **não** há `*.csv` no `.gitignore`: os arquivos CSV deste trabalho são pequenos, públicos e precisam ir para o repositório.

3. Escreva `verificar_ambiente.py`, o seu primeiro programa. Ele mostra, um por linha, a versão do Python e a versão de cada biblioteca instalada. É curto (umas 8 linhas). Ele precisa:
   1. importar o módulo `sys` e mostrar `sys.version`;
   2. importar `pandas`, `matplotlib`, `requests` e `pytest`;
   3. mostrar, para cada uma, o nome e a versão, que fica guardada em `nome_da_biblioteca.__version__`.

   *Pesquise:* o comando `import` e a função `print` com vários valores separados por vírgula. Rode com `python verificar_ambiente.py`. Se der `ModuleNotFoundError`, o ambiente virtual não está ativo.

4. Crie `docs/ambiente.md` com a configuração da máquina (tecla `Win`, digite "Sobre o seu PC": anote "Processador", "RAM instalada", "Edição" e "Versão" do Windows) e a saída do `verificar_ambiente.py`.

**7. Assista às aulas de Python.** Use o **Curso de Python 3 do Curso em Vídeo** (gratuito, com o professor Gustavo Guanabara):

- **Mundo 1** (https://www.cursoemvideo.com/curso/python-3-mundo-1/): das aulas iniciais até as **condições** (primeiros comandos, tipos primitivos, operadores aritméticos, módulos, **manipulação de texto** e condições);
- **Mundo 2** (https://www.cursoemvideo.com/curso/python-3-mundo-2/): as aulas de **condições aninhadas** e de **repetição** (`for` e `while`).

**Digite os exemplos junto com as aulas**, no VS Code, em vez de só assistir. É digitando e errando que se aprende. Os exercícios do próprio curso são ótimos, mas não são obrigatórios: os obrigatórios são os seis abaixo.

**8. Faça os seis exercícios** em `aprendizado\semana1\`, um arquivo por exercício. Para cada um há **o que o programa faz**, **o que pesquisar** e **um teste**: rode com os valores do teste e confira se a saída bate.

| Exercício | O que o programa faz | Pesquise | Teste |
|---|---|---|---|
| `ex01_taxa.py` | pede o número de óbitos e a população de um município e mostra a taxa por 100 mil habitantes: `óbitos / população × 100000` | `input`, `int`, `float`, `print` | 45 óbitos e 30000 habitantes → 150.0 |
| `ex02_cinco_anos.py` | pede o número de óbitos de cada um dos 5 anos (um `input` por ano) e mostra o **total** e a **média por ano** | operadores aritméticos | 8, 7, 1, 2 e 2 → total 20 e média 4.0 |
| `ex03_comparar.py` | pede a taxa de um município e a taxa do estado e mostra `acima da taxa do estado`, `abaixo da taxa do estado` ou `igual à taxa do estado` | `if`, `elif` e `else` | 80 e 60 → acima; 40 e 60 → abaixo; 60 e 60 → igual |
| `ex04_lista_anos.py` | um município do RN teve, de 2020 a 2024, os óbitos da lista `[383, 362, 490, 429, 354]`. Escreva as listas `anos = [2020, 2021, 2022, 2023, 2024]` e `obitos = [...]` no código e mostre, com um `for`, o **total**, o **maior** valor e **em que ano** ele aconteceu, e **em quantos anos** houve mais de 400 óbitos | listas, `for`, `range(len(...))`, contador, acumulador | total 2018; maior 490, em 2022; 2 anos acima de 400 |
| `ex05_codigo.py` | pede o código IBGE de um município (7 dígitos, lido como **texto**) e mostra os **6 primeiros dígitos** e o **último dígito** separadamente. Se o código não tiver 7 caracteres, mostra `código inválido` | fatiamento de texto (`texto[0:6]`, `texto[6]`), `len` | 2408102 → 240810 e 2; 24081 → código inválido |
| `ex06_varios_municipios.py` | com um `while`, pede repetidamente o nome, os óbitos e a população de um município, mostra a taxa de cada um e para quando o nome digitado for `fim`. No final, mostra **qual município teve a maior taxa** | `while`, `break`, guardar o maior valor visto até agora | A (10 óbitos, 20000 hab.) → 50.0; B (3 óbitos, 2000 hab.) → 150.0; C (40 óbitos, 100000 hab.) → 40.0; maior: B |

> **Dois exercícios não são à toa.** O exercício 5 é a armadilha principal do trabalho: o IBGE identifica os municípios com **7 dígitos**, e o DATASUS, com **6** (sem o último dígito, que é um dígito verificador). Na Sprint 5 você vai juntar as duas tabelas, e é esse fatiamento que vai permitir. O exercício 6 mostra, em miniatura, o resultado que você vai encontrar: o município B tem **o menor número de óbitos** e **a maior taxa**.

**9. Diário e PR.** Crie `docs/diario.md` com as três linhas da semana ([seção 7](#combinados)). Anote também qualquer erro que apareceu nos exercícios e como você resolveu. Faça os *commits* (pelo menos 3: o ambiente, os exercícios 1 a 3, os exercícios 4 a 6) e abra o PR para a `develop` com `Closes #1`, colando em **Evidências de teste** a saída do `verificar_ambiente.py` e a saída dos exercícios 4 e 6 com os valores do teste.

### Como saber que deu certo

- O terminal mostra `(.venv)` no começo da linha.
- `python verificar_ambiente.py` mostra a versão do Python e das quatro bibliotecas.
- Os seis exercícios estão em `aprendizado/semana1/`, e todos dão a saída do teste.
- O `git status` **não** mostra `.venv/` nem `__pycache__/`.

### Entrega da sprint

- [ ] Git configurado e repositório clonado, na *branch* `feature/aprendizado-semana1`.
- [ ] Ambiente virtual com as quatro bibliotecas e `requirements.txt` enviado.
- [ ] Estrutura de pastas e `.gitignore`.
- [ ] `verificar_ambiente.py` funcionando e `docs/ambiente.md` preenchido.
- [ ] Os seis exercícios em `aprendizado/semana1/`, conferidos com os testes.
- [ ] `docs/diario.md` com as três linhas da semana.
- [ ] PR aberto para a `develop`, com `Closes #1`.

### Erros comuns

- **`'python' não é reconhecido`:** use `py` (veja o passo 5).
- **O `activate` não funciona:** você está no PowerShell. Troque para o Command Prompt.
- **`TypeError: unsupported operand type(s) for /: 'str' and 'int'`:** o `input` devolve texto. Converta com `int(...)` ou `float(...)` antes de fazer contas. No exercício 5 é o contrário: o código tem de continuar texto, para poder ser fatiado.
- **`IndentationError`:** o Python usa os espaços no começo da linha para saber o que está dentro do `if`, do `for` e do `while`. Use 4 espaços, sempre.
- **O `while` não para:** a condição de parada nunca fica verdadeira. Confira se você compara com `"fim"` escrito exatamente igual (minúsculas, sem espaço).

<a id="sprint-1-escrita"></a>
## Sprint 1 · Escrita: preparar o documento e fichar as leituras da Introdução

**O que você vai entregar:** o documento do artigo aberto e preparado, as normas lidas e as leituras da Introdução fichadas. Nesta semana não há entrega de seção.

### Passo a passo

**1. Abra o documento do artigo** que eu compartilhei com você no Google Drive (o convite chega no e-mail). Preencha o cabeçalho com o seu nome, o curso, o nome dos orientadores e o título provisório: *Onde o socorro imediato faria mais diferença? Mortalidade por infarto agudo do miocárdio e parada cardíaca nos municípios do Rio Grande do Norte*.

**2. Crie a seção "REFERÊNCIAS"** no fim do documento, ainda vazia. A partir de hoje, toda obra que você ler entra nela no mesmo dia.

**3. Leia as normas.** Leia [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) inteiro, com atenção especial a: estrutura do trabalho, Introdução, objetivo geral, como citar e como referenciar.

**4. Leia o resumo do projeto pai** em [`docs/projeto_193sbv.md`](projeto_193sbv.md). Ele é o ponto de partida da Introdução.

**5. Pesquise, leia e fiche em `docs/leituras.md`** (no formato da [seção 8.5](#escrita-geral); este arquivo entra no PR de desenvolvimento da semana que vem):

- **as diretrizes de ressuscitação cardiopulmonar da American Heart Association (AHA):** o projeto cita a versão de 2020. Procure no Google Acadêmico por "2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation" e abra a parte sobre **suporte básico e avançado de vida em adultos** (*Adult Basic and Advanced Life Support*), publicada na revista *Circulation*. Procure também se a AHA publicou uma versão mais nova das diretrizes; se publicou, fiche a mais nova e anote as duas. Leia a introdução e a parte sobre a **cadeia de sobrevivência** (*chain of survival*);
- **a diretriz brasileira:** a "Atualização da Diretriz de Ressuscitação Cardiopulmonar e Cuidados Cardiovasculares de Emergência da Sociedade Brasileira de Cardiologia", publicada nos *Arquivos Brasileiros de Cardiologia* (procure no SciELO, `scielo.br`). Leia a parte sobre suporte básico de vida;
- **de onde vem o "cada minuto reduz a chance de sobreviver":** LARSEN, M. P. *et al.* *Predicting survival from out-of-hospital cardiac arrest: a graphic model*, publicado em 1993 na revista *Annals of Emergency Medicine*. Leia o resumo e anote o número (quanto a chance cai por minuto sem massagem e sem desfibrilação). Esse é o número que o projeto 193 SBV cita;
- **o acionamento de voluntários por celular, que é a ideia do 193 SBV:** RINGH, M. *et al.* *Mobile-phone dispatch of laypersons for CPR in out-of-hospital cardiac arrest*, publicado em 2015 na revista *The New England Journal of Medicine*. Leia o resumo: é um estudo na Suécia em que voluntários treinados eram chamados por SMS quando havia uma parada cardíaca perto deles. Anote o que eles mediram e o que encontraram;
- **as doenças do coração no Brasil:** procure o relatório "Estatística Cardiovascular - Brasil" mais recente, publicado nos *Arquivos Brasileiros de Cardiologia*, e anote um ou dois números sobre a mortalidade por doenças cardiovasculares e por infarto no Brasil (com a página);
- **um número do RN:** abra o TABNET (o caminho está no passo 3 da [Sprint 3](#sprint-3-dev)) e faça uma consulta simples: Linha **Ano do Óbito**, Coluna **Não ativa**, Conteúdo **Óbitos p/Residênc**, período **2024**, e em "Seleções Disponíveis", **Categoria CID-10 = I21 Infarto agudo do miocárdio**. Anote quantas pessoas residentes no RN morreram de infarto agudo do miocárdio em 2024 e a data da consulta. Número concreto vale mais que adjetivo.

### Como saber que deu certo

- O documento do Drive tem o cabeçalho preenchido e a seção de Referências criada.
- O `docs/leituras.md` tem pelo menos **6 obras fichadas**, cada uma com a referência completa no formato ABNT.
- Você tem anotados: a queda da chance de sobreviver por minuto (Larsen), o que o estudo de Ringh mediu e encontrou, um número nacional de mortalidade cardiovascular e o número de óbitos por infarto no RN em 2024, cada um com a fonte e a data da consulta.

### Entrega

- [ ] Documento do Drive com o cabeçalho, o título provisório e a seção de Referências.
- [ ] `docs/orientacoes_escrita_tcc.md` e `docs/projeto_193sbv.md` lidos.
- [ ] Pelo menos 6 obras fichadas em `docs/leituras.md`, com referência ABNT.
- [ ] O número do RN no TABNET anotado com a data da consulta.
- [ ] As obras lidas lançadas na seção de Referências do documento.

Para entregar, comente na *issue* dizendo quantas obras fichou e mova o card para **Em revisão**. O `docs/leituras.md` pode ir no PR desta semana ou no da semana que vem.

---

# Sprint 2: 23/10 a 29/10/2026

<a id="sprint-2-dev"></a>
## Sprint 2 · Desenvolvimento: aprender Python, parte 2

**Branch:** `feature/aprendizado-semana2` · **No PR:** `Closes #3`

**O que você vai entregar:** seis exercícios, agora com dicionários, arquivos CSV, a biblioteca `pandas`, um gráfico de barras, uma consulta a uma API de verdade e os primeiros testes com `pytest`.

Esta semana é a ponte entre o aprendizado e o trabalho: **cada exercício é uma versão pequena de algo que você vai fazer nas Sprints 3 a 8**, com dados reais de 10 municípios do RN, que já estão no repositório, em `aprendizado/exemplo_municipios.csv`. Abra esse arquivo no VS Code e veja: uma linha por município, com o código IBGE, o nome, a população do Censo 2022 e o número de óbitos por infarto agudo do miocárdio em 2024.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 23/10 | passo 1 (aulas do Mundo 3) e exercício 7 |
| segunda, 26/10 | exercícios 8 e 9 (CSV e `pandas`) |
| terça, 27/10 | exercícios 10 e 11 (gráfico e API) |
| quarta, 28/10 | exercício 12 (funções e testes) |
| quinta, 29/10 | diário e PR; a Introdução vence hoje |

### Passo a passo

**1. Assista às aulas do Mundo 3** do Curso em Vídeo (https://www.cursoemvideo.com/curso/python-3-mundo-3/): **tuplas**, **listas**, **dicionários**, **funções** e **módulos**. Digite os exemplos junto.

Depois, leia a introdução do `pandas` na documentação oficial, "10 minutes to pandas" (https://pandas.pydata.org/docs/user_guide/10min.html). Está em inglês: use o tradutor do navegador se precisar, mas **digite e rode os exemplos** das partes *Object creation*, *Viewing data*, *Selection* e *Operations*. Não precisa entender tudo: o objetivo é reconhecer os comandos quando eles aparecerem nos exercícios.

**2. Faça os seis exercícios** em `aprendizado\semana2\`:

**`ex07_dicionario.py`:** crie um dicionário em que a chave é o nome do município e o valor é a população, com três municípios do `exemplo_municipios.csv` (Natal, Mossoró e Parnamirim; copie os números do arquivo). Percorra o dicionário com um `for` e mostre uma linha por município, no formato `Natal: 751300 habitantes`. No fim, mostre a soma das três populações. *Pesquise:* dicionários e o método `.items()`. **Teste:** soma 1268593.

**`ex08_ler_csv.py`:** leia o `aprendizado/exemplo_municipios.csv` com o módulo `csv` (que já vem com o Python) e mostre o **total de óbitos** dos 10 municípios, a **população total** e a **taxa do conjunto** (total de óbitos dividido pela população total, vezes 100 000), com duas casas decimais. *Pesquise:* `open(..., encoding="utf-8")`, `csv.DictReader`, e lembre que o que vem do arquivo é texto (use `int`). **Teste:** 816 óbitos, 1555758 habitantes, taxa 52.45.

**`ex09_pandas.py`:** faça a mesma coisa com o `pandas`, que é como você vai trabalhar daqui para frente, e mais um pouco. Mostre:

1. o total de óbitos, a população total e a taxa do conjunto;
2. uma coluna nova, `taxa`, com a taxa de cada município por 100 mil habitantes;
3. a tabela inteira **ordenada da maior taxa para a menor**;
4. o município com **mais óbitos** e o município com **a maior taxa**;
5. quantos municípios têm **mais de 50 000 habitantes** (filtro).

*Pesquise:* `pd.read_csv`, selecionar uma coluna (`tabela["obitos_2024"]`), `.sum()`, criar coluna nova, `sort_values(..., ascending=False)`, `.idxmax()`, `.loc`, filtro com colchetes (`tabela[tabela["populacao"] > 50000]`) e `len`. Para mostrar a taxa com duas casas, pesquise `round`. **Teste:** taxa do conjunto 52.45; maior taxa Currais Novos, 89.56; menor taxa Parnamirim, 40.36; mais óbitos Natal, com 352; 5 municípios com mais de 50 000 habitantes.

Agora olhe com calma a tabela ordenada e responda no diário: **em que posição Natal ficou na taxa?** Natal tem mais óbitos que todos os outros juntos, quase. Explique com as suas palavras por que ela não está no topo. Essa é a ideia central do seu trabalho.

Compare também o `ex08` com o `ex09`: o que deu menos trabalho? Anote no diário. É por isso que o trabalho usa `pandas`.

**`ex10_grafico.py`:** com o `matplotlib`, faça um gráfico de **barras horizontais** com a taxa de cada um dos 10 municípios, **ordenado** (a maior barra em cima). Escreva o nome do eixo horizontal (`Óbitos por 100 mil habitantes`) e salve a figura como `grafico_taxas.png` na pasta `aprendizado\semana2\`. *Pesquise:* `import matplotlib.pyplot as plt`, `plt.barh`, `plt.xlabel`, `plt.tight_layout` (para os nomes dos municípios não ficarem cortados) e `plt.savefig`. Abra a figura e confira: a barra mais longa tem de ser a de Currais Novos. Se ficou embaixo, pesquise como inverter a ordem do eixo vertical (`invert_yaxis`).

**`ex11_api_ibge.py`:** consulte uma API de verdade. A API de Localidades do IBGE devolve os dados de um município a partir do código dele:

```
https://servicodados.ibge.gov.br/api/v1/localidades/municipios/2408102
```

Abra esse endereço no navegador primeiro e veja a resposta: é um texto no formato **JSON**, que o Python transforma em dicionários dentro de dicionários. Depois, no programa, consulte dois municípios (Natal, `2408102`, e Pau dos Ferros, `2409407`) e mostre, de cada um, o **nome**, a **microrregião** e a **mesorregião**. *Pesquise:* `requests.get`, `resposta.status_code`, `resposta.json()` e como acessar um dicionário dentro de outro (`dados["microrregiao"]["nome"]`). **Teste:** Natal fica na mesorregião Leste Potiguar; Pau dos Ferros, na Oeste Potiguar. Na Sprint 6 você vai usar essa mesma API para descobrir em que região ficam os municípios com as maiores taxas.

**`ex12` (funções e testes):** este exercício tem **dois arquivos**, e é o seu primeiro contato com testes automatizados:

1. `funcoes_anderson.py`, com três funções:
   - `taxa_100mil(obitos, populacao, anos=1)`: devolve `obitos / (populacao * anos) * 100000`. O `anos=1` é um **valor padrão**: quem não informar os anos, calcula a taxa de um ano só;
   - `codigo_6(codigo)`: recebe o código IBGE de 7 dígitos (como texto **ou** como número) e devolve os 6 primeiros, como texto. *Pesquise:* `str(...)`;
   - `situacao(taxa, referencia)`: devolve o texto `"acima"`, `"abaixo"` ou `"igual"`.

   As funções **devolvem** o resultado com `return`; não usam `input` nem `print`.
2. `test_funcoes_anderson.py`, na mesma pasta, que importa as três funções (`from funcoes_anderson import taxa_100mil, codigo_6, situacao`) e tem **pelo menos seis testes**: a taxa de um ano; a taxa de cinco anos (45 óbitos, 30 000 habitantes, 5 anos → 30.0); um município sem óbitos (taxa zero); o código como texto; o código como número (`codigo_6(2408102)` → `"240810"`); e a situação.

Para comparar números decimais, não use `==`: use `pytest.approx`, assim:

```python
assert taxa_100mil(45, 30000, 5) == pytest.approx(30.0)
```

*Pesquise:* "pytest primeiros passos" (https://docs.pytest.org/en/stable/getting-started.html) e `pytest.approx`. Rode, da raiz do repositório:

```
python -m pytest aprendizado
```

O `pytest` mostra um ponto para cada teste que passou e, no fim, quantos passaram. Depois **faça um teste falhar de propósito** (troque o valor esperado) e veja como o `pytest` mostra o erro: o valor esperado, o obtido e a linha. Volte ao valor certo.

**3. Diário e PR.** Escreva o diário (com a resposta sobre Natal), faça os *commits* e abra o PR com `Closes #3`, colando em **Evidências de teste** a saída do `pytest`, a saída do `ex09` e o gráfico do `ex10`. Coloque também o `docs/leituras.md` da Sprint 1 neste PR, se ele ainda não foi.

### Como saber que deu certo

- Os exercícios 8 e 9 dão os números dos testes.
- O `grafico_taxas.png` mostra 10 barras ordenadas, com a de Currais Novos em cima e o eixo nomeado.
- O `ex11` mostra Pau dos Ferros na mesorregião Oeste Potiguar.
- `python -m pytest aprendizado` mostra pelo menos 6 testes passando.
- O diário explica por que Natal não está no topo da taxa.

### Entrega da sprint

- [ ] Aulas do Mundo 3 (tuplas, listas, dicionários, funções e módulos) assistidas e o "10 minutes to pandas" praticado.
- [ ] Os exercícios 7 a 12 em `aprendizado/semana2/`.
- [ ] `grafico_taxas.png` gerado.
- [ ] Testes com `pytest` passando, e a falha proposital vista e desfeita.
- [ ] Diário atualizado, com a resposta sobre Natal.
- [ ] PR aberto para a `develop`, com `Closes #3`.

### Erros comuns

- **`FileNotFoundError` no `ex08` ou no `ex09`:** você rodou o programa de dentro de outra pasta. Rode da raiz do repositório, com o caminho `aprendizado/exemplo_municipios.csv`.
- **`KeyError: 'obitos'`:** o nome da coluna está escrito diferente do cabeçalho do CSV. Confira com `print(tabela.columns)`.
- **`ModuleNotFoundError: No module named 'funcoes_anderson'`:** o arquivo de teste não está na mesma pasta das funções, ou o nome do arquivo está diferente do nome no `import`.
- **`codigo_6(2408102)` dá erro de `int` não ser "subscriptable":** número não pode ser fatiado. Converta para texto com `str` antes.
- **`requests.exceptions.ConnectionError`:** sem internet, ou o endereço está digitado errado. Teste o endereço no navegador.

<a id="sprint-2-escrita"></a>
## Sprint 2 · Escrita: Introdução e Objetivo geral (Entrega 1)

**Prazo:** 29/10/2026

**O que você vai entregar:** a Introdução completa, nos cinco blocos de parágrafos da sequência fixa do [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md), e o Objetivo geral.

Como os resultados ainda não existem, escreva o bloco 4 (apresentação da solução) **no futuro** ("será desenvolvido", "serão calculadas"). Na Sprint 8 você passa para o passado.

### Bloco 1: Contextualização (1 a 2 parágrafos)

**Pesquise:** as doenças cardiovasculares como principal causa de morte no Brasil (o relatório "Estatística Cardiovascular - Brasil" que você fichou); a parada cardíaca fora do hospital e a importância dos primeiros minutos (Larsen e as diretrizes); o papel de quem está perto da vítima, antes de a ambulância chegar (a cadeia de sobrevivência).

**Escreva sobre:** o peso das doenças do coração e da parada cardíaca, com **pelo menos um número** (nacional ou o do RN que você consultou no TABNET, com a fonte). Mostre que o tempo é decisivo e que quem está perto pode fazer a diferença. Termine apresentando o projeto 193 SBV como a iniciativa que quer acionar voluntários treinados pelo celular.

### Bloco 2: Problemática (1 a 2 parágrafos)

**Pesquise:** a desigualdade de acesso ao atendimento pré-hospitalar entre a capital e o interior; por que comparar municípios pelo número de óbitos é enganoso (procure "taxa de mortalidade" e "indicadores de saúde" e a publicação da RIPSA, que está na [seção 12](#referencias-minimas)).

**Escreva sobre:** o problema em duas camadas. Primeiro, **o que falta**: o projeto precisa decidir onde começar a captar voluntários, e para isso precisa saber **onde** os óbitos por essas causas pesam mais. Segundo, **por que a resposta não é óbvia**: os dados são públicos, mas vêm em arquivos que precisam ser limpos e juntados, e o número absoluto de óbitos favorece sempre as cidades grandes.

**Feche com a pergunta de pesquisa** da [seção 2](#ideia), com as suas palavras, e com as três perguntas menores da [seção 8.4](#escrita-geral).

### Bloco 3: Caminho para a solução (1 parágrafo)

**Pesquise:** as fontes públicas de dados de mortalidade no Brasil (o SIM, consultado pelo TABNET) e de população (o Censo do IBGE); as formas de analisar esses dados (consultar e copiar à mão, planilhas eletrônicas, programas). *Pesquise:* "reprodutibilidade" em análise de dados.

**Escreva sobre:** as alternativas, dizendo o que cada uma resolve e o que custa. Consultar o TABNET e copiar para uma planilha funciona para poucos municípios, mas é trabalhoso para 167 e difícil de repetir sem erro. Um programa faz sempre as mesmas contas do mesmo jeito, pode ser testado e pode ser rodado de novo quando sair um ano novo de dados. Justifique a taxa por 100 mil habitantes como forma de comparação justa.

### Bloco 4: Apresentação da solução (1 a 2 parágrafos)

**Escreva sobre:** o que será feito, de forma concreta: um programa em Python, com a biblioteca `pandas`, que lê os dados de óbitos por infarto agudo do miocárdio e parada cardíaca (de 2020 a 2024) e de população do Censo 2022, limpa, junta pelo código do município, calcula a taxa média anual por 100 mil habitantes e aponta os 10 municípios com maior taxa, com gráficos.

Diga **como o resultado será conferido**: a comparação com o próprio TABNET para 10 municípios, o cálculo à mão em uma planilha para 5 municípios, os testes automatizados e a repetição do processo a partir dos arquivos guardados.

Registre que **todos os dados são públicos, secundários e agregados por município**, de órgãos oficiais, e que **o trabalho não envolve pessoas**: por isso não há necessidade de submissão ao Comitê de Ética em Pesquisa (CEP).

### Bloco 5: Vínculo com o projeto e escopo (1 parágrafo)

**Escreva sobre:** o vínculo com o projeto 193 SBV, do IFRN, em parceria com o Corpo de Bombeiros Militar do RN, e a meta em que o trabalho entra (Meta I, diagnóstico, parte quantitativa). Deixe claro o **escopo**: o trabalho não desenvolve o aplicativo; entrega uma análise de dados conferida, que serve de argumento numérico para o projeto e indica onde priorizar a captação de voluntários. As entrevistas com profissionais, previstas na mesma meta, ficam como trabalho futuro.

Feche a Introdução com um parágrafo curto dizendo como o texto está organizado (o que vem na seção 2, na 3, e assim por diante).

### 1.1 Objetivo geral

Uma **única frase**, com **uma única ação principal**. Modelo do [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md):

> "O objetivo principal do presente trabalho consiste [na ação] de [o quê] para [finalidade]."

**Direcionamentos:**

- o verbo que melhor descreve o trabalho é **identificar** (ou **analisar**): o centro do trabalho são os municípios com maior taxa;
- diga **o quê**: as taxas de mortalidade por infarto agudo do miocárdio e parada cardíaca;
- diga **onde e a partir de quê**: nos municípios do RN, com dados públicos do DATASUS e do IBGE;
- diga **para quê**: apoiar a priorização da captação de voluntários do projeto 193 SBV;
- **não** empilhe ações: "desenvolver, calcular e validar" são três objetivos, não um;
- **não** prometa o que não vai medir: o trabalho não mede vidas salvas nem tempo de resposta.

**Confira antes de entregar:** leia o objetivo geral e a pergunta de pesquisa do bloco 2. Os dois precisam estar falando da mesma coisa.

### 1.2 Objetivos específicos

Deixe o título da seção e escreva embaixo "(a ser escrito na Sprint 8)". Eles ficam para o fim de propósito: descrevem o que foi **realmente** alcançado.

### Entrega

- [ ] Os cinco blocos, na ordem, com citações.
- [ ] Pelo menos um número no bloco 1, com a fonte.
- [ ] A pergunta de pesquisa e as três perguntas menores no fim do bloco 2.
- [ ] Bloco 4 no futuro, com a dispensa do Comitê de Ética.
- [ ] Objetivo geral em uma frase, com uma ação principal.
- [ ] Seção 1.2 com "(a ser escrito na Sprint 8)".
- [ ] Obras citadas lançadas nas Referências.
- [ ] Versão nomeada no histórico: `Entrega 1 - Introdução - 29/10`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 3: 30/10 a 05/11/2026

<a id="sprint-3-dev"></a>
## Sprint 3 · Desenvolvimento: os dados do TABNET e do IBGE

**Branch:** `feature/dados-brutos` · **No PR:** `Closes #5`

**O que você vai entregar:** os quatro arquivos de dados baixados à mão e guardados em `dados/brutos/`, o protocolo que diz exatamente como cada um foi baixado e um primeiro programa que abre os arquivos com o `pandas` e mostra o que tem neles.

**Segunda, 02/11, é feriado.** A semana tem um dia útil a menos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 30/10 | passos 1 e 2 (os conceitos e os códigos da CID-10) |
| terça, 03/11 | passos 3 a 5 (os três arquivos do TABNET e o do IBGE) |
| quarta, 04/11 | passos 6 e 7 (protocolo e inspeção dos arquivos) |
| quinta, 05/11 | passos 8 a 10 (`explorar_dados.py`, diário e PR); a escrita da semana |

### Passo a passo

**1. Entenda de onde vêm os dados.** Antes de baixar qualquer coisa, pesquise e anote no diário, com as suas palavras:

- **o que é o SIM** (Sistema de Informações sobre Mortalidade) e **a Declaração de Óbito**, de onde vêm os dados dele;
- **o que é a "causa básica" do óbito**: cada óbito entra no SIM com **uma** causa básica, a doença que iniciou a cadeia de acontecimentos que levou à morte. Por isso os óbitos de causas diferentes podem ser somados sem contar a mesma pessoa duas vezes;
- **óbitos por residência contra óbitos por ocorrência**: o TABNET oferece os dois. "Por ocorrência" conta o óbito no município onde a pessoa morreu; "por residência", no município onde ela morava. **Explique por que este trabalho usa "por residência".** Dica: pense em quem mora no interior, passa mal e morre no hospital de Natal ou de Mossoró, e em qual população a taxa vai usar no denominador.

*Pesquise:* "Sistema de Informações sobre Mortalidade" no site do Ministério da Saúde e as **Notas Técnicas** do próprio TABNET (há um link "Notas Técnicas" no alto da página de consulta).

**2. Confira os códigos da CID-10.** A CID-10 (Classificação Internacional de Doenças, 10ª revisão) dá um código a cada causa de morte. Abra a CID-10 do DATASUS (http://www2.datasus.gov.br/cid10/V2008/cid10.htm), procure o **capítulo IX** (doenças do aparelho circulatório) e encontre:

- **I21 Infarto agudo do miocárdio** e as subcategorias dele (I21.0 a I21.9);
- **I46 Parada cardíaca** e as subcategorias dele.

Anote no `docs/leituras.md` o que cada código inclui. Responda no diário: **por que esses dois códigos são causas em que o socorro imediato faz diferença?** Use o que você leu na Sprint 1 (o infarto é a principal causa da parada cardíaca; na parada, a massagem e a desfibrilação nos primeiros minutos decidem a sobrevivência). Essa resposta vai para o Referencial Teórico desta semana.

**3. Baixe o primeiro arquivo do TABNET: os dois códigos juntos.**

1. Abra https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ → **Estatísticas Vitais** → **Mortalidade - desde 1996 pela CID-10** → **Mortalidade geral** → em "Abrangência Geográfica", escolha **Rio Grande do Norte**. (Atalho direto: http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/obt10rn.def.) Tire um print da página.
2. **Role até o fim da página e leia as "Notas".** Elas dizem até que ano os dados são **finais** e a **data de extração**. Anote as duas informações. Confira se os dados de 2024 são finais; os de 2025 e 2026 são preliminares e não entram.
3. Preencha o formulário:
   - **Linha:** `Município`;
   - **Coluna:** `Ano do Óbito`;
   - **Conteúdo:** `Óbitos p/Residênc`;
   - **Períodos Disponíveis:** o ano mais recente já vem marcado. Clique em `2024` e depois, segurando `Shift`, clique em `2020`: ficam marcados **exatamente** 2020, 2021, 2022, 2023 e 2024. Confira que **2025 e 2026 não ficaram marcados**;
   - **Seleções Disponíveis:** clique no **+** ao lado de **Categoria CID-10**. Na lista que abre, desmarque "Todas as categorias", procure e clique em `I21 Infarto agudo do miocárdio` e, segurando `Ctrl`, clique em `I46 Parada cardíaca`. (O campo "Digite o texto e ache fácil" ajuda a encontrar.) **Não mexa nas outras seleções;**
   - deixe **desmarcados** "Ordenar pelos valores da coluna" e "Exibir linhas zeradas";
   - **Formato:** `Tabela com bordas`.
4. Tire um print do formulário preenchido e clique em **Mostra**. A tabela abre em uma aba nova. Tire um print do começo da tabela.
5. No fim da tabela, clique em **Copia como .CSV**. O navegador baixa um arquivo com um nome comprido, terminado em `.csv`.
6. Mova esse arquivo para `dados\brutos\` e **renomeie** para `obitos_i21_i46_2020_2024.csv`. **Não abra no Excel e não altere nada dentro dele.** (O Excel pode mudar o arquivo ao salvar; se você abrir por engano, feche **sem salvar**.)

**4. Baixe mais dois arquivos do TABNET, um para cada código.** Volte ao formulário e repita o passo 3 mudando só a seleção da Categoria CID-10:

- só `I21 Infarto agudo do miocárdio` → salve como `dados\brutos\obitos_i21_2020_2024.csv`;
- só `I46 Parada cardíaca` → salve como `dados\brutos\obitos_i46_2020_2024.csv`.

Esses dois servem para mostrar no artigo quanto de cada causa existe e para uma conferência que você vai fazer na Sprint 5.

**5. Baixe a população do IBGE.**

1. Abra a tabela 4709 do SIDRA: https://sidra.ibge.gov.br/tabela/4709 (é a tabela de **população residente** do **Censo Demográfico 2022**). Tire um print.
2. Em **Variável**, deixe marcada **só** `População residente (Pessoas)` (desmarque as outras).
3. Em **Ano**, deixe `2022`.
4. Em **Unidade Territorial**, marque **Município** e use o ícone de lista ao lado para escolher os municípios **"Na Unidade da Federação"** → **Rio Grande do Norte**. Confira se aparecem **167** municípios selecionados. Desmarque qualquer outro nível (Brasil, Unidade da Federação).
5. Clique no botão de **Download** (no alto da tabela), escolha o formato **CSV (BR)** e baixe.
6. Mova para `dados\brutos\` e renomeie para `populacao_censo2022_rn.csv`. Tire um print das seleções.

**6. Escreva o protocolo de download** em `docs/protocolo_download.md`. É ele que permite a qualquer pessoa (inclusive você, daqui a um ano) baixar de novo exatamente os mesmos dados. Para **cada um dos quatro arquivos**, registre:

- o nome do arquivo em `dados/brutos/`;
- a fonte (sistema, órgão) e o endereço da página;
- o dia e a hora do download;
- todas as opções escolhidas no formulário (Linha, Coluna, Conteúdo, Períodos, Seleções, Formato; no SIDRA, Variável, Ano e Unidade Territorial);
- para o TABNET, o que dizem as Notas (ano dos dados finais e data de extração);
- o nome dos prints em `docs/evidencias/`.

**7. Olhe os arquivos por dentro, sem alterar.** Abra cada arquivo no VS Code. Os arquivos do TABNET vêm na codificação **ISO-8859-1** (também chamada de "Latin 1"), e não em UTF-8; por isso as letras acentuadas podem aparecer como símbolos estranhos. Para ver direito: clique em `UTF-8`, na barra de baixo do VS Code → **Reopen with Encoding** → **Western (ISO 8859-1)**. Isso só muda a visualização: **não salve**.

Anote no diário, para o arquivo `obitos_i21_i46_2020_2024.csv`:

- quantas linhas existem **antes** da linha de cabeçalho (a que começa com `"Município"`), e o que elas dizem;
- como aparece cada município (o código e o nome estão na mesma "célula"? quantos dígitos tem o código?);
- o que aparece no lugar do zero quando um município não teve óbito naquele ano. *Pesquise:* "TABNET sinais convencionais" para saber o que esse sinal quer dizer;
- o que existe **depois** do último município (a linha de "Total" e as linhas de fonte e notas);
- qual é o separador entre as colunas.

Faça o mesmo com o `obitos_i46_2020_2024.csv` e responda: **quantos municípios aparecem nele?** O RN tem 167. Por que aparecem menos? (Dica: a opção "Exibir linhas zeradas" que ficou desmarcada.) Não baixe de novo: o seu programa vai tratar isso na Sprint 5.

E com o `populacao_censo2022_rn.csv`: quantas linhas de título existem antes dos dados, quantos dígitos tem o código do município, como está escrito o nome do município, o que existe depois do último município, qual é o separador e qual é a codificação (se os acentos aparecem certos em UTF-8, é UTF-8; se não, é ISO 8859-1).

**8. Escreva `explorar_dados.py`.** É o seu primeiro programa com os dados de verdade. Ele não limpa nada ainda: só **mostra** o que o `pandas` enxerga. Para o arquivo dos dois códigos, a leitura começa assim (copie, porque a combinação dos parâmetros não dá para adivinhar):

```python
import pandas as pd

obitos = pd.read_csv(
    "dados/brutos/obitos_i21_i46_2020_2024.csv",
    sep=";",
    encoding="latin-1",
    skiprows=4,
)
```

O `skiprows=4` pula as quatro linhas de título que você contou no passo 7. Se você contou um número diferente, use o seu número e anote por quê.

Depois, o programa precisa mostrar, com um `print` e um título antes de cada um:

1. as primeiras linhas (`.head()`);
2. as **últimas 15 linhas** (`.tail(15)`): é ali que aparecem a linha de "Total" e as notas;
3. o número de linhas e colunas (`.shape`);
4. os nomes das colunas (`.columns`);
5. o tipo de cada coluna (`.dtypes`).

Rode e responda no diário: **por que as colunas dos anos aparecem com um tipo de texto (`str` ou `object`, conforme a versão do `pandas`), e não como número?** (Dica: o sinal do passo 7.) Agora acrescente `na_values="-"` na leitura e rode de novo. O que mudou no tipo das colunas? *Pesquise:* o parâmetro `na_values` do `read_csv` e o que é `NaN`.

Acrescente ao programa a leitura do `populacao_censo2022_rn.csv`, com o separador, a codificação e o número de linhas de título que você descobriu no passo 7, e mostre o `.head()`, o `.tail()` e o `.shape`.

Por último, responda no diário: o arquivo do TABNET tem **mais linhas** que os 167 municípios. Quantas a mais, e o que são?

**9. Envie os arquivos brutos.** Os quatro arquivos de `dados/brutos/` vão para o repositório **exatamente como foram baixados**. Antes do `git add`, confira no `git status` que eles aparecem e que nenhum foi alterado depois do download.

**10. Diário e PR.** Escreva o diário (as anotações dos passos 1, 2, 7 e 8 e as três linhas da semana), faça os *commits* e abra o PR com `Closes #5`, colando em **Evidências de teste** a saída do `explorar_dados.py`.

### Como saber que deu certo

- `dados/brutos/` tem os quatro arquivos, com os nomes certos.
- `docs/protocolo_download.md` tem, para cada arquivo, a fonte, o endereço, a data, as opções escolhidas e os prints.
- `python explorar_dados.py` mostra o começo e o fim das duas tabelas, e o fim da tabela do TABNET mostra a linha de "Total" e as notas.
- O diário explica: por que "por residência", por que I21 e I46, o que é o sinal `-`, por que o arquivo do I46 tem menos municípios e o que são as linhas a mais.

### Entrega da sprint

- [ ] Os três arquivos do TABNET e o do IBGE em `dados/brutos/`, sem alteração.
- [ ] `docs/protocolo_download.md` completo, com os prints em `docs/evidencias/`.
- [ ] Anotações dos arquivos no diário (linhas de título, rodapé, sinal `-`, municípios faltando no I46).
- [ ] `explorar_dados.py` lendo os dois tipos de arquivo.
- [ ] PR aberto para a `develop`, com `Closes #5`.

### Erros comuns

- **`UnicodeDecodeError: 'utf-8' codec can't decode byte`:** o arquivo não está em UTF-8. Use `encoding="latin-1"`.
- **`ParserError: Error tokenizing data`:** o `skiprows` está errado (o `pandas` tentou ler uma linha de título como dado) ou o separador não é o que você informou. Volte ao passo 7 e conte de novo.
- **Tudo veio em uma coluna só:** o separador está errado. Os arquivos do TABNET usam `;`.
- **A tabela do TABNET veio com 2025 ou 2026:** o ano mais recente já vem marcado no formulário. Baixe de novo, conferindo os períodos, e atualize o protocolo.
- **O arquivo baixado tem outro nome ou foi parar em "Downloads":** é normal. Mova para `dados\brutos\` e renomeie.

<a id="sprint-3-escrita"></a>
## Sprint 3 · Escrita: Referencial Teórico, seções 2.1 e 2.2 (Entrega 2)

**Prazo:** 05/11/2026

**O que você vai entregar:** as duas primeiras seções do Referencial Teórico: a parte da saúde (parada cardíaca e Suporte Básico de Vida) e a parte dos dados (o SIM e a CID-10).

Antes de escrever, **assista ao vídeo de explicação do Referencial Teórico**: https://youtu.be/8Qztq1Q5vb0. Lembre a analogia do [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): o referencial explica ao leitor **os conceitos de que ele precisa para entender o seu trabalho**, e nada além disso.

### 2.1 Parada cardíaca, Suporte Básico de Vida e o tempo de resposta

**Pesquise:** o que é a parada cardiorrespiratória e a relação dela com o infarto agudo do miocárdio; a cadeia de sobrevivência; o que é o Suporte Básico de Vida (reconhecer a parada, chamar ajuda, massagem cardíaca, desfibrilador externo automático); o efeito do tempo na sobrevivência (Larsen); o papel do leigo treinado e do acionamento de voluntários (Ringh). Use as diretrizes da AHA e da Sociedade Brasileira de Cardiologia que você fichou.

**Escreva sobre:** os conceitos, nessa ordem, sempre com referência. Termine a seção amarrando ao seu trabalho: se o tempo é decisivo e se voluntários treinados podem chegar antes da ambulância, **saber onde essas mortes pesam mais** ajuda a decidir onde formar e captar voluntários.

**Não escreva** que o SBV "salva todas as vítimas" nem dê números de sobrevivência sem a fonte.

### 2.2 O Sistema de Informações sobre Mortalidade e a CID-10

**Pesquise:** o SIM e a Declaração de Óbito (o que você anotou no passo 1 da Sprint 3); a causa básica do óbito; a CID-10 e a organização dela em capítulos, agrupamentos e categorias; o TABNET como ferramenta de consulta. *Pesquise também:* "qualidade da informação sobre causa de morte" e "causas mal definidas" ou "códigos garbage", para entender as limitações dessas informações.

**Escreva sobre:**

- o que é o SIM, de onde vêm os dados e quem os publica;
- o que é a causa básica e por que cada óbito tem uma só;
- a CID-10 e **a escolha dos dois códigos**, I21 e I46, com a justificativa: por que eles representam óbitos em que o socorro imediato pode fazer diferença. Seja honesto sobre o que fica de fora (por exemplo, óbitos por parada cardíaca registrados com outro código, ou outras causas sensíveis ao tempo, como engasgo e afogamento);
- a diferença entre óbitos por residência e por ocorrência, e qual foi usada;
- uma limitação conhecida: a qualidade do preenchimento da causa de morte varia entre municípios, e a parada cardíaca (I46) é considerada por alguns autores uma causa pouco específica. Diga isso com referência.

### Entrega

- [ ] Vídeo do Referencial assistido.
- [ ] 2.1 com os conceitos de saúde, referenciados e amarrados ao trabalho.
- [ ] 2.2 com o SIM, a CID-10, a justificativa dos códigos I21 e I46 e a limitação da qualidade da causa de morte.
- [ ] Toda afirmação técnica com referência; obras lançadas nas Referências.
- [ ] Comentários da Entrega 1 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 2 - Referencial 2.1 e 2.2 - 05/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 4: 06/11 a 12/11/2026

<a id="sprint-4-dev"></a>
## Sprint 4 · Desenvolvimento: a limpeza dos dados, com testes

**Branch:** `feature/limpeza-dados` · **No PR:** `Closes #7`

**O que você vai entregar:** o arquivo `mortalidade.py` com as funções de leitura e limpeza, os testes delas com `pytest` e o script `limpar_dados.py`, que transforma os arquivos brutos do TABNET e do IBGE em duas tabelas limpas, conferindo os totais.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 06/11 | passos 1 e 2 (`ler_tabnet` e o arquivo de teste) |
| segunda, 09/11 | passos 3 a 5 (código e nome, ausentes, total) |
| terça, 10/11 | passos 6 e 7 (`codigo_6_digitos` e `ler_populacao`) |
| quarta, 11/11 | passos 8 e 9 (testes e `limpar_dados.py`) |
| quinta, 12/11 | passo 10 (diário e PR); a escrita da semana |

### Passo a passo

**1. Crie `mortalidade.py` e a função `ler_tabnet(caminho)`.** Esse arquivo vai guardar **todas** as funções do trabalho. Comece com um comentário no topo dizendo para que ele serve. A função `ler_tabnet` recebe o caminho de um arquivo do TABNET e devolve uma tabela **só com as linhas de municípios**. Ela precisa:

1. ler o arquivo com o `read_csv` como no `explorar_dados.py` (separador, codificação, `skiprows=4` e `na_values="-"`);
2. conferir se a primeira coluna se chama `Município`. Se não se chamar, o arquivo não é do formato esperado (ou o `skiprows` está errado), e a função deve **parar com uma mensagem clara**, em vez de seguir e dar um número errado lá na frente. *Pesquise:* `raise ValueError("...")`;
3. guardar **só as linhas em que a primeira coluna começa com 6 dígitos seguidos de um espaço**. Isso tira, de uma vez só, a linha de "Total", as linhas de fonte e notas e a linha de "município ignorado", se existir. Use:

   ```python
   tabela = tabela[tabela["Município"].str.match(r"\d{6} ", na=False)]
   ```

   *Pesquise:* expressões regulares (`\d` quer dizer "um dígito"; `{6}` quer dizer "seis vezes") e o parâmetro `na=False` (o que ele faz com as linhas vazias);
4. devolver a tabela com o índice refeito (*pesquise:* `reset_index(drop=True)`).

**2. Crie o arquivo de teste `tests/tabnet_mini.csv`.** Para testar a leitura sem depender do arquivo grande, crie um arquivo pequeno **no mesmo formato** do TABNET, com 3 municípios inventados, o "Total" e as notas. O conteúdo é este (copie, porque o formato tem de ser exato):

```
 Mortalidade - Teste
Óbitos p/Residênc por Município e Ano do Óbito
Categoria CID-10: teste
Período:2023-2024
"Município";"2023";"2024";"Total"
"240001 CIDADE A";2;3;5
"240002 CIDADE B";-;1;1
"240003 CIDADE C";10;-;10
"Total";12;4;16
 Fonte: arquivo de teste
 Notas:
 
```

Ao salvar, **salve na mesma codificação do TABNET**: clique em `UTF-8` na barra de baixo do VS Code → **Save with Encoding** → **Western (ISO 8859-1)**. Assim o teste confere também a leitura com a codificação certa (as palavras "Óbitos", "Município" e "Período" têm acento).

**3. Crie a função `separar_codigo_nome(tabela)`.** Ela recebe a tabela que saiu do `ler_tabnet` e devolve uma tabela com duas colunas novas, no lugar da coluna `Município`:

- `codigo6`: os 6 primeiros caracteres (o código do município, **como texto**);
- `nome`: do oitavo caractere em diante (o nome).

*Pesquise:* fatiar texto em uma coluna inteira com `.str[0:6]` e `.str[7:]`, e apagar uma coluna com `drop(columns=...)`. Por que o código fica como **texto**, e não como número? Porque ele é um **identificador**, e não uma quantidade: ninguém soma códigos. Além disso, guardar como texto evita perder zeros à esquerda em outros contextos. Anote isso no diário.

**4. Crie a função `tratar_ausentes(tabela, colunas)`.** Ela troca o `NaN` (que veio do sinal `-`) por **zero** nas colunas informadas e transforma essas colunas em números inteiros. *Pesquise:* `fillna(0)` e `astype(int)`. Por que zero, e não "dado faltando"? Porque, no TABNET, o `-` quer dizer "zero" (você pesquisou os sinais convencionais na Sprint 3). Em outros sistemas o vazio pode significar "não informado", e trocar por zero seria um erro: **sempre confira o que o sinal quer dizer na fonte**.

Depois, renomeie as colunas para nomes simples, sem acento e sem espaço: `2020` vira `obitos_2020` (e assim para os outros anos) e `Total` vira `obitos_total`. *Pesquise:* `rename(columns={...})`.

Para não repetir a lista de anos em todo lugar, crie no topo do `mortalidade.py` uma **constante**: `ANOS = [2020, 2021, 2022, 2023, 2024]`. Use essa lista para montar os nomes das colunas. Se um dia o trabalho for refeito com outro período, muda-se só essa linha.

**5. Crie a função `ler_total_tabnet(caminho)`.** Ela lê o mesmo arquivo e devolve **o número da coluna "Total" na linha "Total"**: o total geral que o próprio TABNET calculou. Ela serve para conferir a limpeza: **a soma dos óbitos dos municípios, depois de limpa, tem de ser igual a esse número.** Se não for, ou alguma linha de município foi perdida, ou existe uma linha de "município ignorado" (óbitos de residentes do RN sem município informado), e isso tem de ser anotado. *Pesquise:* filtrar a linha em que a primeira coluna é igual a `"Total"` e pegar um valor com `.iloc[0]`.

**6. Crie a função `codigo_6_digitos(codigo)`.** É a função do exercício 12 da Sprint 2, agora no `mortalidade.py`: recebe o código IBGE de 7 dígitos (texto ou número) e devolve os 6 primeiros, como texto. Acrescente uma conferência: se o código não tiver 7 dígitos, a função para com `ValueError`.

**7. Crie a função `ler_populacao(caminho)`.** Ela lê o arquivo do SIDRA e devolve uma tabela com as colunas `codigo7`, `codigo6`, `nome_ibge` e `populacao`, **uma linha por município**. Use o que você anotou no passo 7 da Sprint 3 (separador, codificação, linhas de título) e a mesma ideia do `ler_tabnet`: guarde só as linhas em que a coluna do código tem **exatamente 7 dígitos**. *Pesquise:* `.str.fullmatch(r"\d{7}", na=False)` e leia a coluna do código **como texto** (*pesquise:* o parâmetro `dtype` do `read_csv`, por exemplo `dtype=str`). Depois:

- crie `codigo6` aplicando a regra dos 6 primeiros dígitos à coluna inteira (`.str[0:6]`);
- transforme `populacao` em número inteiro;
- tire do nome o sufixo do estado, se o SIDRA tiver escrito, por exemplo, `Acari (RN)` ou `Acari - RN`. *Pesquise:* `.str.replace(...)`.

**8. Escreva os testes** em `tests/test_mortalidade.py`, com **pelo menos 8 testes**. Os quatro primeiros usam o `tests/tabnet_mini.csv`:

1. `ler_tabnet` devolve **3 linhas** (tirou o "Total" e as notas);
2. depois do `separar_codigo_nome`, a primeira linha tem `codigo6` igual a `"240001"` e `nome` igual a `"CIDADE A"`;
3. depois do `tratar_ausentes`, o `obitos_2023` da CIDADE B é **0** e a coluna é de números inteiros;
4. a soma de `obitos_total` é igual ao `ler_total_tabnet` (16).

E pelo menos mais quatro:

5. `codigo_6_digitos("2408102")` devolve `"240810"`;
6. `codigo_6_digitos(2408102)` (número) devolve o mesmo;
7. `codigo_6_digitos("24081")` para com `ValueError` (*pesquise:* `with pytest.raises(ValueError):`);
8. `ler_tabnet` com um arquivo que não é do TABNET para com `ValueError` (use o próprio `aprendizado/exemplo_municipios.csv` como "arquivo errado").

Para o teste encontrar o arquivo de teste, use o caminho a partir da raiz: `"tests/tabnet_mini.csv"`, e rode sempre `python -m pytest` da raiz.

**9. Escreva `limpar_dados.py`.** É o script que usa as funções. Ele precisa:

1. ler `dados/brutos/obitos_i21_i46_2020_2024.csv` com `ler_tabnet`, separar código e nome e tratar os ausentes;
2. **conferir**: mostrar o número de municípios (tem de ser 167), a soma de `obitos_total` e o total do TABNET (`ler_total_tabnet`), e dizer se as duas somas são iguais. Se não forem, mostrar a diferença;
3. gravar `dados/obitos_limpos.csv` (com `index=False` e `encoding="utf-8"`);
4. ler `dados/brutos/populacao_censo2022_rn.csv` com `ler_populacao`;
5. **conferir**: número de municípios (167) e a população total do RN;
6. gravar `dados/populacao_limpa.csv`.

Confira a população total do RN no próprio SIDRA (mesma tabela 4709, nível **Unidade da Federação**, Rio Grande do Norte) e anote no diário se bate com a soma dos municípios.

**10. Diário e PR.** Anote no diário os números que o `limpar_dados.py` mostrou e se as somas bateram. Faça os *commits* e abra o PR com `Closes #7`, colando em **Evidências de teste** a saída do `python -m pytest` e a saída do `limpar_dados.py`.

### Como saber que deu certo

- `python -m pytest` mostra pelo menos 8 testes novos passando (além dos do aprendizado).
- `python limpar_dados.py` mostra 167 municípios nas duas tabelas e diz que a soma dos óbitos é igual ao total do TABNET.
- `dados/obitos_limpos.csv` tem as colunas `codigo6`, `nome`, `obitos_2020` a `obitos_2024` e `obitos_total`, sem nenhum `-` e sem a linha de "Total".
- `dados/populacao_limpa.csv` tem as colunas `codigo7`, `codigo6`, `nome_ibge` e `populacao`, com 167 linhas.

### Entrega da sprint

- [ ] `mortalidade.py` com `ANOS`, `ler_tabnet`, `separar_codigo_nome`, `tratar_ausentes`, `ler_total_tabnet`, `codigo_6_digitos` e `ler_populacao`.
- [ ] `tests/tabnet_mini.csv` em ISO 8859-1 e `tests/test_mortalidade.py` com pelo menos 8 testes.
- [ ] `limpar_dados.py` com as conferências de contagem e de soma.
- [ ] `dados/obitos_limpos.csv` e `dados/populacao_limpa.csv`.
- [ ] Diário com os números e a conferência da população do RN.
- [ ] PR aberto para a `develop`, com `Closes #7`.

### Erros comuns

- **`AttributeError: Can only use .str accessor with string values`:** a coluna não é de texto. Leia com `dtype=str` ou converta com `.astype(str)` antes.
- **O teste do `tabnet_mini.csv` dá `UnicodeDecodeError` ou não acha a coluna `Município`:** o arquivo foi salvo em UTF-8. Salve de novo com **Save with Encoding → Western (ISO 8859-1)**.
- **`ValueError: cannot convert float NaN to integer`:** sobrou `NaN` em alguma coluna antes do `astype(int)`. Confira se passou todas as colunas de anos e o total para o `tratar_ausentes`.
- **A soma não bate com o total do TABNET:** abra o arquivo bruto e procure uma linha sem código (por exemplo, "MUNICIPIO IGNORADO"). Se existir, a diferença é esse número, e ele vai para o diário e para o artigo. Se não existir, alguma linha de município foi perdida no filtro: mostre as linhas que **não** passaram no filtro para descobrir qual.
- **167 virou 166 ou 168:** confira se o filtro está pegando só as linhas com código de 6 dígitos **seguido de espaço**.

<a id="sprint-4-escrita"></a>
## Sprint 4 · Escrita: Referencial Teórico, seções 2.3 e 2.4 (Entrega 3)

**Prazo:** 12/11/2026

**O que você vai entregar:** as duas últimas seções do Referencial: os indicadores de mortalidade (por que taxa, e não número absoluto) e os trabalhos relacionados, com um quadro comparativo.

### 2.3 Indicadores de mortalidade: números absolutos e taxas

**Pesquise:** o conceito de **taxa de mortalidade específica por causa** na publicação da RIPSA (*Indicadores básicos para a saúde no Brasil*): a fórmula, o que vai no numerador e no denominador e por que se multiplica por 100 mil. *Pesquise também:* "problema dos pequenos números" ou "instabilidade de taxas em pequenas áreas", e "padronização por idade" (só o conceito).

**Escreva sobre:**

- por que o número absoluto não serve para comparar municípios de tamanhos diferentes (um exemplo com números inventados ajuda: dois municípios, um grande e um pequeno);
- a definição da taxa, com a **fórmula numerada** (como equação, no padrão do [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md)), e por que se usa "por 100 mil habitantes";
- por que somar vários anos e usar a população do ano do meio (a [seção 3](#decisoes) deste plano explica; procure uma referência que diga a mesma coisa);
- **a limitação dos municípios pequenos**: com poucos habitantes, um ou dois óbitos a mais mudam muito a taxa;
- **a diferença entre taxa bruta e taxa padronizada por idade**: populações mais velhas têm mais infartos, e a taxa bruta não corrige isso. Diga que o trabalho usa a taxa bruta e por quê (simplicidade e disponibilidade dos dados), e deixe a padronização como trabalho futuro.

### 2.4 Trabalhos relacionados

**Pesquise** no Google Acadêmico e no SciELO 3 ou 4 trabalhos próximos do seu. Termos de busca que funcionam: "mortalidade por infarto agudo do miocárdio" com "distribuição espacial" ou "municípios"; "mortalidade por doenças cardiovasculares" com "Rio Grande do Norte" ou "Nordeste"; "parada cardiorrespiratória extra-hospitalar" com "Brasil"; "DATASUS" com "Python" ou "análise de dados". Dê preferência a trabalhos sobre o Nordeste e o RN, e inclua o estudo de Ringh (acionamento de voluntários) se ele não tiver sido usado na 2.1.

**Escreva:** um parágrafo para cada trabalho, dizendo o que ele fez, com que dados, que medida usou (número absoluto, taxa bruta, taxa padronizada) e o que encontrou. Termine com um **quadro comparativo** com as colunas: trabalho, local, período, causas (códigos), medida usada, ferramenta, se o processo pode ser repetido (código ou passo a passo disponível). A última linha do quadro é **o seu trabalho**. Feche com um parágrafo dizendo o que o seu trabalho tem de diferente (por exemplo: foco no RN e no período mais recente, ligação com um projeto de voluntários, processo aberto, testado e conferido com a fonte).

### Regras que valem para o referencial inteiro

- Toda afirmação técnica com referência; nenhuma referência que você não leu.
- Explique com as suas palavras e amarre ao seu trabalho no fim de cada seção.

### Entrega

- [ ] 2.3 com a fórmula numerada, a justificativa dos cinco anos e da população do meio, os pequenos números e a taxa bruta contra a padronizada.
- [ ] 2.4 com 3 ou 4 trabalhos, um parágrafo cada, e o quadro comparativo com a linha do seu trabalho.
- [ ] Pelo menos 10 obras nas Referências.
- [ ] Comentários da Entrega 2 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 3 - Referencial 2.3 e 2.4 - 12/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 5: 13/11 a 19/11/2026

<a id="sprint-5-dev"></a>
## Sprint 5 · Desenvolvimento: a junção das tabelas e as taxas

**Branch:** `feature/juncao-taxas` · **No PR:** `Closes #9`

**O que você vai entregar:** a tabela de óbitos e a de população juntas pelo código do município, a taxa por 100 mil habitantes de cada um dos 167 municípios, as listas dos 10 maiores (por taxa e por número de óbitos) e a taxa do RN, tudo gerado pelo script `analisar.py`, com testes.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 13/11 | passos 1 e 2 (as outras duas causas e o experimento com os nomes) |
| segunda, 16/11 | passos 3 a 5 (`juntar`, `calcular_taxa`, `maiores`) |
| terça, 17/11 | passo 6 (testes) |
| quarta, 18/11 | passo 7 (`analisar.py`) |
| quinta, 19/11 | passo 8 (olhar os resultados), diário e PR; a escrita da semana |

### Passo a passo

**1. Limpe também os arquivos de cada causa.** No `limpar_dados.py`, você fez quatro passos para limpar o arquivo do TABNET (ler, separar, tratar ausentes, renomear). Agora são três arquivos do TABNET. Em vez de copiar e colar os quatro passos três vezes, crie no `mortalidade.py` uma função `limpar_tabnet(caminho)` que faz os quatro passos e devolve a tabela limpa, e use-a no `limpar_dados.py` para os três arquivos. Grave `dados/obitos_i21_limpos.csv` e `dados/obitos_i46_limpos.csv`, com as mesmas conferências de contagem e de soma. Faça um *commit* só dessa reorganização, com o prefixo `refactor:`.

O arquivo do I46 vai mostrar **menos de 167 municípios** (você já sabe por quê). Isso não é erro: anote o número no diário.

**2. Faça o experimento dos nomes** em `experimento_nomes.py`. A tentação é juntar as duas tabelas pelo nome do município. Teste se isso funciona:

1. leia `dados/obitos_limpos.csv` e `dados/populacao_limpa.csv` (com `dtype={"codigo6": str, "codigo7": str}`);
2. junte pelo nome (`merge` com `left_on="nome"` e `right_on="nome_ibge"`) e mostre **quantos municípios casaram**;
3. mostre, lado a lado, o nome do TABNET e o do IBGE de 5 municípios (junte pelo código só para poder comparar) e veja a diferença;
4. agora tente "consertar": passe os dois nomes para maiúsculas e tire os acentos (*pesquise:* `unicodedata.normalize("NFKD", texto)` e `.encode("ascii", "ignore").decode()`), junte de novo e mostre quantos casaram e **quais continuam sem casar**.

Anote no diário os números das duas tentativas e o que sobrou. **Essa é a justificativa, com número, para juntar pelo código**, e ela vai para a Metodologia.

**3. Crie a função `juntar(obitos, populacao)`** no `mortalidade.py`. Ela junta as duas tabelas pelo `codigo6` e **não pode perder município em silêncio**. Ela precisa:

1. usar `merge` com `on="codigo6"`, `how="outer"` e `indicator=True`. Com `how="outer"`, os municípios que só existem em uma das tabelas **também aparecem** no resultado; com `indicator=True`, aparece uma coluna `_merge` dizendo de onde veio cada linha (`both`, `left_only` ou `right_only`);
2. se alguma linha **não** for `both`, parar com `ValueError`, mostrando os códigos que sobraram;
3. apagar a coluna `_merge` e devolver a tabela.

*Pesquise:* os tipos de junção do `merge` (`inner`, `left`, `right`, `outer`) e o parâmetro `validate="one_to_one"`, que também vale a pena usar aqui (ele para se algum código aparecer duas vezes em uma das tabelas).

**4. Crie a função `calcular_taxa(obitos, populacao, anos)`.** Ela aplica a fórmula da [seção 3](#decisoes): `obitos / (populacao * anos) * 100000`. Escrita assim, ela funciona tanto com números soltos quanto com colunas inteiras do `pandas`, sem mudar nada.

**5. Crie a função `maiores(tabela, coluna, n=10)`.** Ela devolve as `n` linhas com os maiores valores da coluna, em ordem decrescente, com uma coluna `posicao` de 1 a `n`. *Pesquise:* `sort_values`, `head` e `reset_index(drop=True)`.

**6. Escreva os testes** no `tests/test_mortalidade.py`, com tabelas pequenas criadas no próprio teste (*pesquise:* `pd.DataFrame({...})`). Pelo menos estes:

1. `juntar` com 3 municípios em cada tabela, os mesmos códigos → 3 linhas;
2. `juntar` com um código a mais em uma das tabelas → `ValueError`;
3. `calcular_taxa(45, 30000, 5)` → 30.0;
4. `calcular_taxa(0, 30000, 5)` → 0.0;
5. `calcular_taxa` com duas colunas de 3 valores → as 3 taxas certas;
6. `maiores` com uma tabela de 5 linhas e `n=3` → 3 linhas, a primeira com o maior valor e `posicao` igual a 1;
7. `limpar_tabnet` com o `tests/tabnet_mini.csv` → colunas `codigo6`, `nome`, `obitos_2023`, `obitos_2024` e `obitos_total`.

Rode `python -m pytest`. Todos os testes, os da Sprint 4 e os novos, precisam passar.

**7. Escreva `analisar.py`.** Este é o programa principal do trabalho. Ele lê as tabelas limpas e grava os resultados. Ele precisa, nesta ordem:

1. ler `dados/obitos_limpos.csv`, `dados/obitos_i21_limpos.csv`, `dados/obitos_i46_limpos.csv` e `dados/populacao_limpa.csv`, **sempre** com `dtype={"codigo6": str, "codigo7": str}`;
2. juntar óbitos e população com `juntar`;
3. acrescentar as colunas `obitos_i21` e `obitos_i46`: junte a tabela com o `obitos_total` de cada causa (renomeado), usando `how="left"`, e troque por 0 os municípios que não apareceram (`fillna(0)` e `astype(int)`). Por que aqui pode `how="left"` com zero, e no `juntar` não pode? Porque aqui a ausência **quer dizer zero** (a regra do TABNET que você conferiu), enquanto lá a ausência quer dizer **erro**. Anote isso no diário;
4. **conferir**: em todos os municípios, `obitos_i21 + obitos_i46` tem de ser igual a `obitos_total`. Mostre quantos de 167 conferem. *Pesquise:* comparar duas colunas e somar o resultado (`(a == b).sum()`);
5. calcular a coluna `taxa_100mil` com `calcular_taxa(..., len(ANOS))`, arredondada para 2 casas;
6. criar as colunas `posicao_taxa` e `posicao_obitos`, com a posição de cada município nas duas ordenações. *Pesquise:* `rank(ascending=False, method="min")`, que dá a mesma posição a valores empatados;
7. calcular os números do RN: total de óbitos (e de cada causa), população total, **taxa do RN** (com a mesma função) e quantos municípios ficaram acima da taxa do RN;
8. gravar, em `resultados/`:
   - `taxas_municipios.csv`: os 167 municípios ordenados pela `posicao_taxa`, com `codigo6`, `codigo7`, `nome_ibge`, `populacao`, os óbitos de cada ano, `obitos_total`, `obitos_i21`, `obitos_i46`, `taxa_100mil`, `posicao_taxa` e `posicao_obitos`;
   - `top10_taxa.csv` e `top10_obitos.csv`, com a função `maiores`;
   - `resumo_rn.csv`, com uma linha só: número de municípios, óbitos (total, I21 e I46), população, taxa do RN e número de municípios acima da taxa do RN;
9. mostrar na tela o resumo do RN e as duas listas de 10.

**8. Olhe os resultados com calma** e anote no diário:

- a posição de Natal, de Mossoró e de Parnamirim **nas duas ordenações** (por óbitos e por taxa);
- **quantos municípios aparecem nas duas listas de 10** ao mesmo tempo (*pesquise:* `isin`);
- a população do menor município da lista dos 10 maiores taxas;
- a porcentagem dos óbitos que é I21 e a que é I46;
- se há **empate** entre o 10º e o 11º colocado na taxa (veja as linhas 10 e 11 do `taxas_municipios.csv`).

Escreva também, em duas ou três frases, o que mais surpreendeu você. Esse parágrafo é o começo da seção de Resultados.

### Como saber que deu certo

- `python -m pytest` passa, com os testes novos.
- `python limpar_dados.py` grava as três tabelas de óbitos, e a do I46 tem menos de 167 linhas.
- `experimento_nomes.py` mostra quantos municípios casam pelo nome, antes e depois de tirar os acentos.
- `python analisar.py` mostra "167 de 167" na conferência de I21 + I46, a taxa do RN e as duas listas.
- `resultados/taxas_municipios.csv` tem 167 linhas, e `top10_taxa.csv` e `top10_obitos.csv` têm 10 linhas cada.

### Entrega da sprint

- [ ] `limpar_tabnet` e as tabelas limpas do I21 e do I46.
- [ ] `experimento_nomes.py`, com os números no diário.
- [ ] `juntar`, `calcular_taxa` e `maiores` no `mortalidade.py`, com pelo menos 7 testes novos.
- [ ] `analisar.py` gravando os quatro arquivos de `resultados/`.
- [ ] Conferência I21 + I46 = total em 167 de 167 municípios.
- [ ] Diário com as posições, a comparação das duas listas e a surpresa.
- [ ] PR aberto para a `develop`, com `Closes #9`.

### Erros comuns

- **`ValueError: You are trying to merge on object and int64 columns`:** uma das tabelas leu o `codigo6` como número. Leia **sempre** com `dtype={"codigo6": str}`.
- **O `juntar` para dizendo que sobraram códigos:** confira se o `codigo6` da população foi feito com os 6 **primeiros** dígitos do código de 7 (e não com os 6 últimos).
- **A junção deu mais de 167 linhas:** algum código aparece duas vezes em uma das tabelas (por exemplo, uma linha de "Total" que escapou). O `validate="one_to_one"` mostra isso.
- **A taxa do RN saiu igual à média das 167 taxas:** está errado. A taxa do RN é o **total de óbitos** dividido pela **população total**, e não a média das taxas (municípios pequenos pesariam igual a Natal). Anote essa diferença no diário.
- **`posicao_taxa` saiu com números quebrados (como 10.5):** use `method="min"` no `rank` e transforme em inteiro.

<a id="sprint-5-escrita"></a>
## Sprint 5 · Escrita: Metodologia (Entrega 4)

**Prazo:** 19/11/2026

**O que você vai entregar:** a seção 3 do artigo, que junta a metodologia e os materiais e métodos. O critério é um só: **outra pessoa conseguiria repetir o seu trabalho só com o que está escrito?**

Escreva no **passado** o que já foi feito (download, limpeza, junção, cálculo) e no **futuro** o que ainda não foi (as conferências das Sprints 6 e 7). Na Sprint 6 você passa tudo para o passado.

### 3.1 Classificação da pesquisa

**Pesquise** em Gil (2017) e em Prodanov e Freitas (2013) e classifique o trabalho quanto à **natureza** (aplicada), à **abordagem** (quantitativa), aos **objetivos** (descritiva) e aos **procedimentos** (documental, com dados secundários). *Pesquise também:* "estudo ecológico" em epidemiologia, que é o nome dado aos estudos que usam dados agregados por área, como o seu. Justifique cada classificação em uma ou duas frases.

### 3.2 Fontes de dados e ferramentas

**Escreva:**

- as **fontes**: o SIM, pelo TABNET, com as opções da consulta (por residência, códigos I21 e I46, 2020 a 2024, data de extração que aparece nas Notas e data do seu download); e o Censo Demográfico 2022, pela tabela 4709 do SIDRA, com a data de acesso. Tudo isso está no `docs/protocolo_download.md`;
- as **ferramentas**, com a versão (do `docs/ambiente.md` e do `requirements.txt`): Python, `pandas`, Matplotlib, `pytest`, VS Code, Git e GitHub, e a planilha eletrônica usada na conferência;
- o **endereço do repositório**, onde estão o código, os dados brutos e os resultados.

### 3.3 Etapas do processamento

**Faça um fluxograma** no draw.io (https://app.diagrams.net) com as etapas: download manual → limpeza → junção pelo código → cálculo da taxa → listas e gráficos → conferências. Exporte em PNG e coloque no documento como figura.

**Escreva**, etapa por etapa, o que foi feito e **por quê** (as decisões e as justificativas são a parte mais importante):

- por que óbitos por residência;
- como os arquivos foram limpos (linhas de título e de rodapé, linha de "Total", código e nome separados, `-` tratado como zero, com a referência dos sinais convencionais do TABNET);
- por que a junção foi feita pelo código, **com o número do experimento dos nomes**, e como o código de 7 dígitos do IBGE virou o de 6 do DATASUS;
- a fórmula da taxa (cite a equação da seção 2.3) e por que cinco anos e a população de 2022;
- como foram escolhidos os 10 municípios e o que foi feito com empates.

### 3.4 Validação

**Escreva** como o resultado foi (ou será) conferido, com a **meta** de cada conferência:

- **testes automatizados** das funções de limpeza e de cálculo;
- **conferências internas**: soma dos óbitos igual ao total do TABNET; I21 + I46 igual ao total em todos os municípios;
- **conferência com a fonte**: 10 municípios consultados de novo, direto no TABNET, comparados com o programa (meta: 100% iguais). Diga como os 10 foram escolhidos (regra da Sprint 6);
- **conferência das taxas**: 5 municípios calculados à mão em uma planilha (meta: 100% iguais);
- **reprodutibilidade**: o programa rodado de novo em uma pasta limpa, a partir só do repositório, deve dar os mesmos números.

### Entrega

- [ ] 3.1 com as quatro classificações justificadas e o conceito de estudo ecológico.
- [ ] 3.2 com as fontes (opções e datas), as ferramentas (com versão) e o endereço do repositório.
- [ ] 3.3 com o fluxograma e as decisões justificadas, incluindo o número do experimento dos nomes.
- [ ] 3.4 com as cinco formas de validação e as metas.
- [ ] Comentários da Entrega 3 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 4 - Metodologia - 19/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 6: 20/11 a 26/11/2026

<a id="sprint-6-dev"></a>
## Sprint 6 · Desenvolvimento: os gráficos e a conferência com o TABNET

**Branch:** `feature/graficos-conferencia` · **No PR:** `Closes #11`

**O que você vai entregar:** os gráficos de barras do artigo, a região de cada município (pela API do IBGE) com a taxa por mesorregião, e a conferência dos totais de 10 municípios com o que o TABNET mostra diretamente.

**Sexta, 20/11, é feriado.** A semana tem um dia útil a menos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| segunda, 23/11 | passos 1 e 2 (os gráficos) |
| terça, 24/11 | passo 3 (as regiões e a taxa por mesorregião) |
| quarta, 25/11 | passos 4 e 5 (a consulta ao TABNET e o `conferir_tabnet.py`) |
| quinta, 26/11 | passo 6 (diário e PR); a escrita da semana |

### Passo a passo

**1. Crie `graficos.py` com uma função de gráfico reaproveitável.** Crie a função `grafico_top10(tabela, coluna, rotulo_x, caminho, referencia=None)`, que desenha um gráfico de barras horizontais com os nomes dos municípios no eixo vertical e os valores da `coluna` no horizontal, e salva em `caminho`. Ela precisa:

1. ordenar para que **a maior barra fique em cima** (*pesquise:* `invert_yaxis`);
2. escrever o valor na ponta de cada barra, **com vírgula decimal**, como se escreve em português. *Pesquise:* `ax.bar_label(barras, labels=...)`, e monte os textos assim: `[f"{v:.1f}".replace(".", ",") for v in valores]`;
3. se `referencia` for informada, desenhar uma **linha vertical** nesse valor, com legenda (*pesquise:* `ax.axvline` e `ax.legend`). Ela vai mostrar a taxa do RN;
4. escrever o nome do eixo horizontal (`rotulo_x`);
5. **não escrever título dentro da imagem**: o título vai na legenda da figura, no documento do artigo, em cima da figura, como manda a ABNT;
6. ajustar as margens (`tight_layout`), salvar com `dpi=200` e fechar a figura (`plt.close()`), para uma figura não desenhar por cima da outra.

*Pesquise:* `fig, ax = plt.subplots(figsize=(8, 5))` e `ax.barh`. Trabalhar com `ax` (e não com `plt.` direto) é o que vai permitir, no passo 2, colocar dois gráficos lado a lado.

Coloque o código que **chama** a função dentro de um bloco `if __name__ == "__main__":`, no fim do arquivo. *Pesquise* o que esse bloco faz: na Sprint 7 você vai importar a função `grafico_top10` em outro script, e sem esse bloco os gráficos seriam todos refeitos a cada importação.

**2. Gere os dois gráficos principais.** No bloco principal do `graficos.py`, leia `resultados/top10_taxa.csv`, `resultados/top10_obitos.csv` e `resultados/resumo_rn.csv` e gere:

- `graficos/top10_taxa.png`: os 10 municípios com maior taxa, com a linha da taxa do RN. Rótulo do eixo: `Óbitos por 100 mil habitantes por ano (2020-2024)`;
- `graficos/obitos_vs_taxa.png`: **dois gráficos lado a lado**: à esquerda, os 10 municípios com mais óbitos (número absoluto, de 2020 a 2024); à direita, os 10 com maior taxa. *Pesquise:* `plt.subplots(1, 2, figsize=(12, 5))`, que devolve dois `ax`. Para isso, a função do passo 1 precisa poder desenhar em um `ax` que já existe: acrescente a ela um parâmetro `ax=None` (se vier `None`, ela cria a figura; se vier um `ax`, desenha nele e não salva). Este é o gráfico que mostra, em uma imagem só, a ideia central do trabalho.

Abra os dois PNG e confira: nomes legíveis, nada cortado, vírgula decimal, eixos com nome e unidade.

**3. Descubra onde ficam os municípios.** Crie `regioes.py`, que:

1. **se o arquivo `dados/brutos/municipios_ibge_rn.json` ainda não existir**, consulta a API do IBGE com a lista de todos os municípios do RN (o `24` é o código do estado) e grava a resposta nesse arquivo, sem mexer:

   ```
   https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios
   ```

   *Pesquise:* `os.path.exists` e gravar texto em arquivo com `open(..., "w", encoding="utf-8")`. Se o arquivo já existir, o programa **não consulta de novo**: assim, quem repetir o trabalho usa exatamente a mesma resposta que você. Registre a data da consulta no `docs/protocolo_download.md`, como um quinto arquivo bruto;
2. lê o JSON (*pesquise:* `json.load`) e monta `dados/regioes.csv` com `codigo7` (o campo `id`, como texto), `microrregiao` e `mesorregiao`, uma linha por município. O caminho até cada informação é o mesmo do exercício 11 da Sprint 2. Confira se são 167 linhas.

Depois, no `analisar.py`:

1. junte `dados/regioes.csv` à tabela pelo `codigo7` e confira que nenhum município ficou sem região;
2. acrescente `microrregiao` e `mesorregiao` ao `taxas_municipios.csv` e ao `top10_taxa.csv`;
3. grave `resultados/taxa_mesorregiao.csv`, com uma linha por mesorregião: número de municípios, soma dos óbitos, soma da população, **taxa da mesorregião** (total de óbitos dividido pela população total, com a mesma `calcular_taxa`) e **quantos dos 10 maiores** ficam nela. *Pesquise:* `groupby(...).agg(...)`.

Anote no diário: em que mesorregiões ficam os 10 municípios com maior taxa? E qual mesorregião tem a maior taxa? A taxa da mesorregião é muito mais estável que a de um município pequeno, porque soma muita gente. Ela vai ser um argumento forte na recomendação para o 193 SBV.

**4. Consulte o TABNET de novo, para 10 municípios.** Esta é a **conferência com a fonte**: você vai comparar os totais do seu programa com os que o TABNET mostra **na tela**, em uma consulta nova, feita de outro jeito. Se o seu programa perdeu, trocou ou somou errado algum número, essa conferência mostra.

Escolha os 10 municípios por esta regra (ela mistura o topo da lista, as cidades grandes e o meio da lista):

- os que estão nas posições **1, 3, 5, 7 e 9** da `posicao_taxa`;
- **Natal, Mossoró e Parnamirim**;
- os que estão nas posições **50 e 100** da `posicao_taxa` (se houver empate, o primeiro que aparece no arquivo).

Faça a consulta no TABNET com as **mesmas opções** do passo 3 da Sprint 3 (Linha `Município`, Coluna `Ano do Óbito`, Conteúdo `Óbitos p/Residênc`, 2020 a 2024, Categoria CID-10 I21 e I46) e, **além disso**, em "Seleções Disponíveis", clique no **+** ao lado de **Município** e selecione **só os 10** (segure `Ctrl` para marcar vários). Clique em **Mostra**. Tire um print da tabela inteira e salve em `docs/evidencias/s06_conferencia_tabnet.png`. Confira também as Notas: a data de extração ainda é a mesma do seu download?

**Digite** os números da tela em `dados/conferencia_tabnet.csv`, com as colunas `codigo6,nome,obitos_2020,obitos_2021,obitos_2022,obitos_2023,obitos_2024,obitos_total` (onde a tela mostrar `-`, digite 0). Digite olhando a tela, e **não** copie do arquivo baixado na Sprint 3: o objetivo é ter uma segunda fonte, independente.

**5. Escreva `conferir_tabnet.py`.** Ele:

1. lê o `dados/conferencia_tabnet.csv` e o `resultados/taxas_municipios.csv` (com o `codigo6` como texto);
2. junta os dois pelo `codigo6` (confira que são 10 linhas);
3. compara, município a município, os seis números (os cinco anos e o total) e cria a coluna `confere`, que é verdadeira só se **os seis** forem iguais. *Pesquise:* comparar várias colunas de uma vez e `.all(axis=1)`;
4. grava `resultados/conferencia_tabnet.csv`, com o total do programa e o do TABNET lado a lado e a coluna `confere`;
5. mostra na tela quantos dos 10 conferem e a porcentagem. **A meta é 100%.**

Se algum não conferir, descubra por quê antes de entregar: compare com o print. Se foi erro de digitação, corrija o `conferencia_tabnet.csv` **olhando o print**. Se o TABNET mostra outro número e a data de extração mudou, os dados foram atualizados depois do seu download: veja a [seção 10](#riscos). Anote tudo no diário: a divergência e a explicação são resultado.

**6. Diário e PR.** Faça os *commits* e abra o PR com `Closes #11`, colando em **Evidências de teste** a saída do `pytest`, os dois gráficos, a tabela de taxa por mesorregião e a saída do `conferir_tabnet.py`.

### Como saber que deu certo

- `graficos/top10_taxa.png` mostra a maior taxa em cima, os valores com vírgula e a linha da taxa do RN.
- `graficos/obitos_vs_taxa.png` mostra os dois gráficos lado a lado, legíveis.
- `dados/regioes.csv` tem 167 linhas, e rodar `regioes.py` de novo não consulta a API.
- `resultados/taxa_mesorregiao.csv` tem uma linha por mesorregião, e a soma dos municípios dá 167.
- `python conferir_tabnet.py` mostra "10 de 10 (100%)", ou o diário explica cada diferença.

### Entrega da sprint

- [ ] `graficos.py` com `grafico_top10` e o bloco `if __name__ == "__main__":`.
- [ ] `graficos/top10_taxa.png` e `graficos/obitos_vs_taxa.png`.
- [ ] `regioes.py`, `dados/brutos/municipios_ibge_rn.json` e `dados/regioes.csv`.
- [ ] `resultados/taxa_mesorregiao.csv` e as regiões no `taxas_municipios.csv`.
- [ ] Print da consulta ao TABNET e `dados/conferencia_tabnet.csv` digitado.
- [ ] `conferir_tabnet.py` e `resultados/conferencia_tabnet.csv`.
- [ ] PR aberto para a `develop`, com `Closes #11`.

### Erros comuns

- **Os nomes dos municípios saem cortados no gráfico:** use `tight_layout()` antes do `savefig`, ou aumente a largura da figura.
- **Um gráfico aparece desenhado por cima do outro:** faltou o `plt.close()` depois de salvar.
- **O gráfico ficou com a menor barra em cima:** o `barh` desenha de baixo para cima. Use `invert_yaxis()`.
- **`KeyError: 'microrregiao'` no `regioes.py`:** o caminho no dicionário está errado. Abra o JSON no VS Code (ou o endereço no navegador) e siga as chaves com os olhos.
- **O `conferir_tabnet.py` junta menos de 10 linhas:** algum `codigo6` foi digitado errado no `conferencia_tabnet.csv`, ou foi lido como número em uma das tabelas.

<a id="sprint-6-escrita"></a>
## Sprint 6 · Escrita: colocar no documento as tabelas e os gráficos (tarefa curta)

**Prazo:** 26/11/2026

**O que você vai entregar:** as tabelas e os gráficos que já existem colocados na seção 4 do documento, cada um com uma frase que o anuncia, e a seção 3 passada para o passado. Nesta semana não há entrega de seção nova: esta tarefa existe para que a semana dos Resultados seja de **escrever a discussão**, e não de montar tabela.

### Passo a passo

1. Crie no documento os títulos da seção 4: **4.1 Os dados obtidos**, **4.2 Números absolutos e taxas**, **4.3 Os municípios com maiores taxas**, **4.4 Validação e reprodutibilidade** e **4.5 Limitações**.
2. Em **4.1**, monte uma tabela com os números do `resultados/resumo_rn.csv`: municípios, óbitos de 2020 a 2024 (total, I21 e I46), população e taxa do RN.
3. Em **4.2**, coloque a figura `graficos/obitos_vs_taxa.png`.
4. Em **4.3**, coloque a figura `graficos/top10_taxa.png`, uma tabela com os 10 municípios de maior taxa (posição, município, mesorregião, população, óbitos de 2020 a 2024 e taxa) e a tabela de taxa por mesorregião.
5. Em **4.4**, coloque a tabela da conferência com o TABNET (os 10 municípios, o total do programa, o total do TABNET e se confere).
6. Para **cada** tabela e figura: uma frase **antes**, que a anuncia ("A Tabela 2 apresenta..."); a identificação **em cima** (`Tabela 2 - ...`, `Figura 3 - ...`); a fonte **embaixo** (por exemplo: `Fonte: elaborado pelo autor com dados do SIM/DATASUS e do IBGE (2026).`); e números com **vírgula decimal**. As regras completas estão nas seções "Como incluir imagens" e "Como incluir tabelas" do [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).
7. Passe a seção 3 para o **passado** no que já foi feito, incluindo a conferência com o TABNET.

### Entrega

- [ ] Títulos 4.1 a 4.5 no documento.
- [ ] Tabela do resumo do RN, as duas figuras, a tabela dos 10 maiores, a tabela por mesorregião e a tabela da conferência com o TABNET.
- [ ] Cada tabela e figura anunciada no texto, com identificação em cima, fonte embaixo e vírgula decimal.
- [ ] Seção 3 no passado no que já foi feito.
- [ ] Comentários da Entrega 4 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Sprint 6 - tabelas e gráficos - 26/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 7: 27/11 a 03/12/2026

<a id="sprint-7-dev"></a>
## Sprint 7 · Desenvolvimento: a conferência das taxas, a estabilidade e a reprodutibilidade

**Branch:** `feature/validacao-estabilidade` · **No PR:** `Closes #13`

**O que você vai entregar:** a taxa de 5 municípios calculada à mão em uma planilha e comparada com a do programa, a análise da estabilidade das taxas (por ano e por tamanho do município), a lista complementar dos municípios com mais de 20 mil habitantes e a prova de que o programa, rodado do zero, dá os mesmos números.

**Os Resultados vencem nesta mesma quinta.** Por isso, **as tabelas e os gráficos desta sprint precisam estar prontos na segunda, 30/11.** A reprodutibilidade (terça) não gera número novo, só confere os que existem. Quarta e quinta são para escrever.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 27/11 | passos 1 e 2 (a planilha e o `conferir_planilha.py`) |
| segunda, 30/11 | passos 3 e 4 (`estabilidade.py` e a lista de mais de 20 mil); **tabelas e gráficos prontos** |
| terça, 01/12 | passo 5 (reprodutibilidade) |
| quarta, 02/12 | passo 6 (revisão das figuras), diário e PR |
| quinta, 03/12 | a escrita dos Resultados |

### Passo a passo

**1. Calcule 5 taxas à mão, em uma planilha.** Esta é a **conferência das taxas**: as contas do programa comparadas com as mesmas contas feitas por outro caminho.

1. Na pasta do Drive do artigo, crie uma planilha do Google chamada `Conferência das taxas`.
2. Escolha 5 dos 10 municípios da conferência da Sprint 6: os das posições **1, 5 e 9**, **Natal** e o da posição **100**. Assim, os óbitos vêm do print do TABNET da Sprint 6, que é uma fonte independente do seu programa.
3. Crie as colunas: `codigo6`, `nome`, `obitos_2020` a `obitos_2024`, `soma`, `populacao`, `taxa` e `taxa_arredondada`.
4. **Digite** os óbitos de cada ano olhando o print da Sprint 6.
5. **Digite** a população olhando o **IBGE Cidades** (https://cidades.ibge.gov.br): procure o município e copie a "População no último censo" (2022). Outra fonte independente: não use o seu `populacao_limpa.csv`.
6. Use **fórmulas** (e não a calculadora) para as três últimas colunas: `soma` com `=SOMA(...)` dos cinco anos; `taxa` com a fórmula da [seção 3](#decisoes) (soma dividida por população vezes 5, vezes 100 000); `taxa_arredondada` com `=ARRED(...; 2)`.
7. Mostre as fórmulas na tela (*Exibir → Mostrar → Fórmulas*), tire um print e salve em `docs/evidencias/s07_planilha_formulas.png`. Volte a mostrar os valores e tire outro print.
8. Baixe a planilha em CSV (*Arquivo → Fazer download → Valores separados por vírgula (.csv)*) e salve como `dados/conferencia_planilha.csv`.

Abra o CSV no VS Code e veja como os números com casas decimais foram gravados. A planilha em português pode gravar a vírgula decimal (`"30,00"`), entre aspas. Se for assim, leia com o parâmetro `decimal=","` do `read_csv`.

**2. Escreva `conferir_planilha.py`.** Ele lê o `dados/conferencia_planilha.csv` e o `resultados/taxas_municipios.csv` (com o `codigo6` como texto), junta pelos códigos (5 linhas) e confere, para cada município:

- se a `soma` da planilha é igual ao `obitos_total` do programa;
- se a `populacao` é igual;
- se a `taxa_arredondada` é igual à `taxa_100mil` do programa (como são números decimais, considere iguais se a diferença for menor que 0,005; *pesquise:* `abs`).

Grave `resultados/conferencia_planilha.csv`, com os valores lado a lado e a coluna `confere`, e mostre quantos dos 5 conferem. **A meta é 100%.** Se algum não conferir, descubra se o erro está na planilha (digitação, fórmula) ou no programa, e anote no diário.

**3. Meça a estabilidade das taxas** em `estabilidade.py`. Na seção 2.3 do Referencial (Sprint 4), você escreveu sobre o problema dos municípios pequenos. Agora você vai **medir**. O script precisa:

1. ler `resultados/taxas_municipios.csv` e importar `ANOS` e `calcular_taxa` do `mortalidade.py`;
2. calcular a **taxa de cada ano**, para cada município (os óbitos do ano divididos pela população, com `anos=1`), nas colunas `taxa_2020` a `taxa_2024`. Use a população de 2022 para todos os anos: é uma aproximação, que você deve declarar no artigo;
3. calcular a **amplitude** de cada município: a maior taxa anual menos a menor (*pesquise:* `max(axis=1)` e `min(axis=1)`);
4. separar os municípios em três **portes** pela população: até 10 mil, de 10 mil a 50 mil e mais de 50 mil habitantes (*pesquise:* `pd.cut`, com `bins` e `labels`), e calcular, para cada porte, o número de municípios e a **média da amplitude**;
5. gravar `resultados/taxa_por_ano.csv` e `resultados/estabilidade_porte.csv`;
6. gerar `graficos/taxa_por_ano.png`: um gráfico de **linhas**, com os anos no eixo horizontal, mostrando a taxa de cada ano do **1º colocado** da lista, de **Natal** e do **RN** (a taxa do RN de cada ano é o total de óbitos do ano dividido pela população total);
7. gerar `graficos/populacao_taxa.png`: um gráfico de **dispersão** com a população no eixo horizontal, em **escala logarítmica** (*pesquise:* `ax.set_xscale("log")` e o que é escala logarítmica), a taxa no eixo vertical, uma linha horizontal na taxa do RN e os 10 maiores em outra cor.

Olhe os dois gráficos e a tabela por porte e anote no diário: o que acontece com as taxas dos municípios pequenos? A forma do gráfico de dispersão lembra um funil? Quantos dos 10 maiores têm menos de 10 mil habitantes? **Isso não invalida o resultado**, mas muda a forma de lê-lo, e vai para a discussão e para a recomendação.

**4. Faça a lista complementar dos municípios maiores.** No `estabilidade.py`, filtre os municípios com **20 mil habitantes ou mais**, gere os 10 de maior taxa entre eles com a função `maiores` e grave `resultados/top10_taxa_20mil.csv`. Gere o gráfico `graficos/top10_taxa_20mil.png` **importando** a função `grafico_top10` do `graficos.py` (`from graficos import grafico_top10`). Anote quantos municípios do RN têm 20 mil habitantes ou mais.

Por que 20 mil? É um corte simples, que deixa de fora os municípios em que poucos óbitos mudam muito a taxa. Ele é **arbitrário**, e você deve dizer isso no artigo: a lista complementar **não substitui** a lista principal, só mostra quais municípios maiores, onde a taxa é mais estável, também merecem atenção.

**Até aqui, tudo pronto na segunda, 30/11.** Faça os *commits* e o `push`.

**5. Prove que o trabalho se repete.** Esta é a **conferência de reprodutibilidade**: alguém que baixe o seu repositório e rode os programas tem de obter **exatamente** os mesmos números. Você vai fazer isso em uma pasta nova, como se fosse outra pessoa (se puder, em **outra máquina** do laboratório):

1. confira que tudo foi enviado (`git status` limpo e `git push` feito);
2. no Prompt de Comando:

   ```
   cd %USERPROFILE%
   git clone https://github.com/nicifrn/mp_sbv193_analise_mortalidades.git teste_reproducao
   cd teste_reproducao
   git checkout feature/validacao-estabilidade
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. rode os programas **na ordem**: `limpar_dados.py`, `regioes.py`, `analisar.py`, `graficos.py`, `estabilidade.py`, `conferir_tabnet.py` e `conferir_planilha.py`. Depois rode `python -m pytest`;
4. rode `git status`.

**O `git status` é a prova.** Os programas acabaram de **gravar de novo** todos os arquivos de `dados/` (os limpos) e de `resultados/`. Se o Git disser `nothing to commit, working tree clean`, os arquivos novos são **idênticos, byte a byte**, aos que estão no repositório: o trabalho se repete. Se algum arquivo aparecer como modificado, veja a diferença com `git diff nome_do_arquivo` e descubra a causa (um caminho fixo da sua máquina, um arquivo que não foi enviado, uma biblioteca de versão diferente). Se só os PNG aparecerem modificados, anote: o que importa para o artigo são os números dos CSV, mas investigue o motivo.

Repare também que o `regioes.py` **não consultou** a API, porque o JSON já estava no repositório. Tire um print do terminal com o `git status` e salve em `docs/evidencias/s07_reproducao.png`. Anote no diário o resultado, a máquina usada e o tempo que os programas levaram. Depois, apague a pasta `teste_reproducao` pelo Explorador de Arquivos.

**6. Revise todas as figuras.** Abra cada PNG de `graficos/` e confira: eixos com nome e unidade, vírgula decimal nos rótulos, nada cortado, letras legíveis no tamanho em que vão aparecer no documento, nenhum título dentro da imagem. Corrija o que for preciso, rode de novo e faça os *commits*. Abra o PR com `Closes #13`, colando em **Evidências de teste** a saída do `pytest`, a saída do `conferir_planilha.py`, a tabela de estabilidade por porte, os gráficos novos e o print da reprodutibilidade.

### Como saber que deu certo

- `python conferir_planilha.py` mostra "5 de 5 (100%)", ou o diário explica cada diferença.
- `resultados/estabilidade_porte.csv` tem três linhas, e a soma dos municípios dá 167.
- `graficos/taxa_por_ano.png` e `graficos/populacao_taxa.png` estão legíveis, e o eixo da população está em escala logarítmica.
- `resultados/top10_taxa_20mil.csv` tem 10 linhas, todas com 20 mil habitantes ou mais.
- Na pasta `teste_reproducao`, depois de rodar tudo, o `git status` diz `working tree clean` (ou o diário explica o que mudou e por quê).

### Entrega da sprint

- [ ] Planilha com fórmulas, os dois prints e `dados/conferencia_planilha.csv`.
- [ ] `conferir_planilha.py` e `resultados/conferencia_planilha.csv`.
- [ ] `estabilidade.py`, com `taxa_por_ano.csv`, `estabilidade_porte.csv` e os dois gráficos.
- [ ] `top10_taxa_20mil.csv` e o gráfico, usando a função importada do `graficos.py`.
- [ ] Reprodutibilidade conferida, com o print do `git status`.
- [ ] Todas as figuras revisadas.
- [ ] PR aberto para a `develop`, com `Closes #13`.

### Erros comuns

- **`ValueError: could not convert string to float: '30,00'`:** a planilha gravou a vírgula decimal. Use `decimal=","` no `read_csv`.
- **A taxa da planilha difere da do programa na segunda casa:** confira se as duas arredondam no mesmo ponto (no fim, e não no meio da conta) e se a fórmula da planilha multiplica a população por 5.
- **`ImportError` ao importar `grafico_top10`:** rode o `estabilidade.py` a partir da raiz do repositório, onde o `graficos.py` está.
- **Importar o `graficos.py` refaz todos os gráficos:** o código que gera os gráficos ficou fora do bloco `if __name__ == "__main__":`.
- **Na pasta de teste, `FileNotFoundError` em algum arquivo:** ele não foi enviado ao repositório. Confira o `.gitignore` e o `git status` da sua pasta de trabalho.

<a id="sprint-7-escrita"></a>
## Sprint 7 · Escrita: Resultados e Discussão (Entrega 5)

**Prazo:** 03/12/2026

**O que você vai entregar:** a seção 4 completa. É a seção mais importante do artigo. As tabelas e os gráficos principais já estão no documento desde a Sprint 6: agora é acrescentar os da Sprint 7 e escrever a discussão.

> **Regra sem exceção:** toda figura ou tabela é **anunciada no texto antes** de aparecer e **explicada depois**. Nada de duas figuras seguidas sem texto entre elas. Organize a seção respondendo às **três perguntas de pesquisa**, na ordem.

### 4.1 Os dados obtidos

A tabela do resumo do RN. **Discuta:** quantos óbitos foram analisados, a participação de cada causa (quanto é I21 e quanto é I46), quantos municípios não tiveram nenhum óbito por I46 e o que isso diz sobre a forma como as paradas cardíacas são registradas (amarre com a limitação que você escreveu na 2.2). Informe as conferências internas: a soma bateu com o total do TABNET, e I21 + I46 bateu com o total em todos os municípios.

### 4.2 Números absolutos e taxas (pergunta 2)

A figura dos dois gráficos lado a lado. **Discuta:** quantos municípios aparecem nas duas listas de 10; a posição de Natal, Mossoró e Parnamirim por número de óbitos e por taxa; e o que aconteceria se o projeto escolhesse onde captar voluntários pelo número absoluto. Este é o resultado que mostra **por que** o trabalho calculou taxas.

### 4.3 Os municípios com maiores taxas (pergunta 1)

A tabela e a figura dos 10 maiores, a tabela por mesorregião e a lista complementar dos municípios com mais de 20 mil habitantes. **Discuta:**

- quais são os municípios e **onde ficam** (se estão concentrados em alguma região do estado);
- a taxa da mesorregião, que é mais estável que a de cada município, e o que ela confirma;
- a lista dos municípios maiores e o que ela acrescenta;
- **compare com os trabalhos relacionados** da seção 2.4: os seus números estão na mesma faixa? As regiões que se destacam são parecidas?
- cuidado com as explicações: o trabalho **não mede** por que as taxas são mais altas em um lugar. Você pode **levantar hipóteses**, com referência (por exemplo, a idade da população, a distância dos hospitais com tratamento para infarto, a qualidade do registro da causa de morte), deixando claro que são hipóteses.

### 4.4 Validação e reprodutibilidade (pergunta 3)

As tabelas das conferências com o TABNET e com a planilha, o resultado da reprodutibilidade, a tabela de estabilidade por porte e os gráficos de taxa por ano e de dispersão. **Discuta:** se as metas de 100% foram atingidas (se não, por quê); o que a reprodutibilidade garante (qualquer pessoa pode refazer e atualizar com um ano novo); e o quanto a taxa dos municípios pequenos varia de um ano para o outro, com os números.

### 4.5 Limitações

Curta e honesta:

- **municípios pequenos:** poucos óbitos mudam muito a taxa (você mediu quanto);
- **taxa bruta:** não corrige a diferença de idade entre as populações; municípios com mais idosos tendem a ter taxas maiores;
- **qualidade do registro da causa de morte**, que varia entre municípios;
- **a escolha dos códigos:** I21 e I46 não são todas as mortes em que o socorro imediato faz diferença (ficam de fora, por exemplo, engasgo, afogamento e trauma);
- **população de 2022 para todos os anos**, e o período inclui os anos da pandemia de covid-19 (2020 e 2021);
- **estudo ecológico:** o resultado vale para municípios, e não para pessoas; e uma taxa alta não quer dizer, sozinha, que o 193 SBV evitaria aquelas mortes.

### Entrega

- [ ] Seções 4.1 a 4.5, com os números dos arquivos de `resultados/`.
- [ ] Todas as figuras e tabelas anunciadas antes e explicadas depois, com identificação e fonte.
- [ ] As três perguntas de pesquisa respondidas, na ordem.
- [ ] Comparação com os trabalhos relacionados na 4.3.
- [ ] Comentários da Sprint 6 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 5 - Resultados - 03/12`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 8: 04/12 a 10/12/2026

<a id="sprint-8-dev"></a>
## Sprint 8 · Desenvolvimento: README, recomendação e fechamento

**Branch:** `feature/fechamento` · **No PR:** `Closes #15`

**O que você vai entregar:** o código revisado, o `README.md` completo, a recomendação para a equipe do 193 SBV e a apresentação.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 04/12 | passo 1 (revisão do código) |
| segunda, 07/12 | passo 2 (`README.md`); a Conclusão do artigo tem de estar pronta hoje |
| terça, 08/12 | passo 3 (recomendação) |
| quarta e quinta, 09 e 10/12 | passos 4 e 5 (apresentação e PR) e o fechamento do texto |

### Passo a passo

**1. Revise o código.** Para cada arquivo `.py`:

- um comentário no topo dizendo o que ele faz, o que lê e o que grava;
- cada função do `mortalidade.py` com uma *docstring* (o texto entre `"""` logo abaixo do `def`) dizendo o que recebe e o que devolve;
- nada de código comentado "para usar depois", nem de `print` de teste esquecido;
- **nenhum caminho fixo da sua máquina** (`C:\Users\...`) dentro do código: tudo relativo à raiz do repositório;
- os nomes de variáveis dizem o que guardam (`taxa_rn`, e não `x`).

Rode `python -m pytest` e todos os scripts de novo, na ordem, e confira com `git status` que nenhum resultado mudou.

**2. Escreva o `README.md`.** Ele precisa permitir que outra pessoa repita tudo. Escreva na ordem em que a pessoa faria:

1. o que é o projeto, a que projeto pai pertence e o que ele calcula;
2. o que precisa ter: Python 3.10 ou mais novo e Git;
3. como criar o ambiente virtual e instalar (`pip install -r requirements.txt`);
4. **a ordem dos scripts**, numerada, com uma linha explicando o que cada um faz, o que lê e o que grava;
5. como rodar os testes (`python -m pytest`);
6. o que tem em cada pasta, e as colunas do `resultados/taxas_municipios.csv`, com o significado de cada uma;
7. as fontes de dados, com o endereço e a data de acesso (do `docs/protocolo_download.md`);
8. **como atualizar com um ano novo de dados**: o passo a passo (baixar de novo seguindo o protocolo, mudar a constante `ANOS`, rodar os scripts na ordem, refazer as conferências). É isso que torna o seu trabalho útil para o projeto depois que você terminar;
9. a configuração da máquina onde tudo foi rodado;
10. os responsáveis.

**3. Escreva a recomendação para o 193 SBV**, em `docs/recomendacao.md`, em **uma página**, escrita para a equipe do projeto (pessoas que não leram o artigo):

- onde o problema pesa mais: os municípios e as regiões com as maiores taxas, **com os números**;
- por que olhar a taxa, e não o número de óbitos (com o exemplo de Natal);
- o cuidado com os municípios pequenos, e por que olhar também a taxa por região e a lista dos municípios maiores;
- uma sugestão concreta de **onde começar** a captação de voluntários, com a justificativa;
- o que o projeto ainda precisa saber e este trabalho não mede (tempo de resposta real do atendimento, onde estão as bases do SAMU e dos Bombeiros, as entrevistas da Meta I).

**4. Monte a apresentação.** Dez minutos, de 8 a 10 slides no Google Apresentações, salvos na mesma pasta do Drive do artigo: o problema e o projeto 193 SBV, a pergunta, os dados (TABNET e IBGE), a ideia da taxa (com o exemplo de Natal), o processo (o fluxograma), os gráficos lado a lado, os 10 municípios e as regiões, as conferências (as metas de 100% e a reprodutibilidade), a estabilidade dos municípios pequenos e a recomendação.

**5. Feche.** Confira o `git status`, apague arquivos de teste soltos e abra o PR com `Closes #15`, com a saída do `pytest`. Depois do *merge*, os orientadores levam a `develop` para a `main` e publicam a versão `v1.0`.

### Como saber que deu certo

- `python -m pytest` passa, e o `git status` está limpo depois de rodar todos os scripts.
- O `README.md` tem as dez partes, incluindo como atualizar com um ano novo.
- `docs/recomendacao.md` cabe em uma página e tem números.
- A apresentação está na pasta do Drive.

### Entrega da sprint

- [ ] Código revisado (comentário no topo, *docstrings*, nenhum caminho fixo).
- [ ] `README.md` completo.
- [ ] `docs/recomendacao.md`.
- [ ] Apresentação de 10 minutos na pasta do Drive.
- [ ] Repositório limpo.
- [ ] PR aberto para a `develop`, com `Closes #15`.

<a id="sprint-8-escrita"></a>
## Sprint 8 · Escrita: Conclusão, Objetivos específicos, Resumo e Título (Entrega 6)

**Prazo:** 10/12/2026 · **A Conclusão precisa estar pronta na segunda, 07/12.**

**O que você vai entregar:** a Conclusão, os Objetivos específicos, o Resumo, o *Abstract*, as palavras-chave, o Título definitivo e o texto inteiro revisado.

### 5 Conclusão (até 07/12)

Curta e direta. Nada de resultado, conceito ou citação que não tenha aparecido antes. **Escreva, nesta ordem:**

1. **o problema e o objetivo geral**, dizendo que foi alcançado, **com número** (por exemplo, quantos municípios foram analisados, a taxa do RN e a faixa de taxas dos 10 maiores);
2. **a resposta direta às três perguntas de pesquisa**, uma ou duas frases cada;
3. **as contribuições:** a lista de municípios e regiões prioritários para o 193 SBV; um processo aberto, testado, conferido com a fonte e reprodutível, que pode ser atualizado a cada ano novo de dados; e a recomendação para o projeto;
4. **as dificuldades reais**, do `docs/diario.md` (por exemplo: os arquivos com título e rodapé, a codificação, os municípios que não casavam pelo nome, os municípios ausentes no arquivo do I46);
5. **trabalhos futuros**, concretos: a taxa padronizada por idade; outras causas em que o socorro imediato faz diferença (engasgo, afogamento, trauma); cruzar as taxas com a localização das bases do SAMU e dos Bombeiros; as entrevistas da Meta I do projeto.

**Não escreva** que o 193 SBV "vai salvar" um número de vidas: o trabalho não mede isso. E não generalize para outros estados o que você mediu no RN.

### 1.2 Objetivos específicos

De 3 a 5 itens, verbo no infinitivo, minúscula no início, ponto e vírgula no fim de cada um e ponto no último, **na mesma ordem** das etapas da Metodologia e das subseções dos Resultados. Cada um tem de ser **verificável**: na Conclusão, você mostrou que foi atingido. "Aprender Python" ou "instalar as bibliotecas" são tarefas, não objetivos.

O que os itens devem cobrir (escreva com as suas palavras): a obtenção e a preparação dos dados públicos de óbitos e de população; o desenvolvimento do programa que calcula as taxas; a identificação dos municípios e regiões com maiores taxas, comparando com os números absolutos; e a validação dos resultados (conferências e reprodutibilidade).

### Resumo, *Abstract* e palavras-chave

Escrito **por último**, depois do texto aprovado. Parágrafo único, de 150 a 250 palavras, impessoal, sem citações, sem siglas pouco conhecidas e sem menção a figuras ou tabelas (NBR 6028:2021). Uma ou duas frases para cada item:

1. **contexto e problema:** o socorro nos primeiros minutos, o projeto 193 SBV e a pergunta sobre onde o problema pesa mais;
2. **objetivo:** o que o trabalho identificou;
3. **método:** dados do SIM e do Censo 2022, códigos I21 e I46, 2020 a 2024, taxa por 100 mil habitantes, programa em Python;
4. **resultados:** os números principais (taxa do RN, onde ficam os municípios de maior taxa, quantos coincidem com os de mais óbitos, as conferências);
5. **conclusão:** a utilidade para o projeto e o cuidado com os municípios pequenos.

**Coloque números no resumo.** Resumo sem número é resumo fraco.

O ***Abstract*** é a versão em inglês. Os termos da área têm forma consagrada (*mortality rate*, *acute myocardial infarction*, *cardiac arrest*, *basic life support*, *public health data*): use-os, e não a tradução literal. Não entregue tradução automática sem revisar.

**Palavras-chave:** de 3 a 5, separadas por ponto e vírgula, no campo de: mortalidade; infarto agudo do miocárdio; parada cardíaca; suporte básico de vida; DATASUS; análise de dados. Escolha os termos pelos quais alguém **procuraria** o seu trabalho.

### Título

Deve indicar **o que foi feito** e **onde**, coerente com o objetivo geral: a ação (identificação, análise), o objeto (mortalidade por infarto agudo do miocárdio e parada cardíaca, taxas) e o recorte (municípios do Rio Grande do Norte, 2020 a 2024). Subtítulo separado por dois-pontos, se precisar. Evite títulos genéricos ("Análise de dados na saúde") e não prometa mais do que o artigo mede ("vidas salvas", "tempo de resposta"). Proponha **três opções** na *issue*; nós escolhemos uma com você na revisão.

### Revisão final

- [ ] A Introdução (bloco 4) e a Metodologia estão no **passado**?
- [ ] O objetivo geral, as perguntas de pesquisa, os objetivos específicos, as subseções dos Resultados e a Conclusão falam das mesmas coisas, na mesma ordem?
- [ ] Todos os números do Resumo, dos Resultados e da Conclusão são **exatamente** os dos arquivos de `resultados/`?
- [ ] A fórmula da taxa está numerada e citada no texto?
- [ ] As fontes de dados têm endereço, **data de acesso** e a data de extração do TABNET?
- [ ] Os códigos da CID-10 estão justificados?
- [ ] As decisões (residência, cinco anos, população de 2022, junção pelo código, `-` como zero) estão justificadas?
- [ ] Toda tabela e figura é citada antes de aparecer, tem identificação em cima, fonte embaixo, e os gráficos têm unidade nos eixos e vírgula decimal?
- [ ] A seção de limitações está presente?
- [ ] As siglas (SBV, SIM, CID-10, DATASUS, TABNET, IBGE, SIDRA, AHA, CBMRN, CEP) estão por extenso na primeira vez?
- [ ] O texto está impessoal e no passado?
- [ ] Está declarado que os dados são públicos, secundários e agregados, e que não houve participantes humanos?
- [ ] O endereço do repositório está na Metodologia?
- [ ] Todos os comentários foram respondidos e resolvidos?
- [ ] A versão final foi nomeada no histórico: `Entrega 6 - versão final - 10/12`?

Para entregar, comente na *issue* com o nome da versão e as três opções de título, e mova o card para **Em revisão**.

---

<a id="quadro-resumo"></a>
## 9. Quadro-resumo

| Sprint | Período | Desenvolvimento | Escrita | Conceitos novos |
|---|---|---|---|---|
| 1 | 16/10 a 22/10 | Python, parte 1 (Git, ambiente, o básico) | Preparar o documento e fichar | variáveis, condições, repetição, fatiamento de texto |
| 2 | 23/10 a 29/10 | Python, parte 2 (`pandas`, gráfico, API, `pytest`) | Introdução e Objetivo geral | dicionários, funções, `DataFrame`, testes |
| 3 | 30/10 a 05/11 | Os dados do TABNET e do IBGE | Referencial 2.1 e 2.2 | SIM, CID-10, residência e ocorrência, codificação, protocolo |
| 4 | 06/11 a 12/11 | Limpeza, com testes | Referencial 2.3 e 2.4 | expressões regulares, sinais convencionais, conferência de totais |
| 5 | 13/11 a 19/11 | Junção e taxas | Metodologia | `merge`, junção pelo código, taxa por 100 mil, `rank` |
| 6 | 20/11 a 26/11 | Gráficos, regiões e conferência com o TABNET | Tabelas e gráficos no documento | `subplots`, `groupby`, conferência com a fonte |
| 7 | 27/11 a 03/12 | Planilha, estabilidade e reprodutibilidade | Resultados e Discussão | pequenos números, escala logarítmica, reprodutibilidade |
| 8 | 04/12 a 10/12 | README, recomendação e fechamento | Conclusão, Resumo e Título | documentação, síntese |

---

<a id="riscos"></a>
## 10. Riscos e planos B

| Risco | Sinal de alerta | O que fazer |
|---|---|---|
| O Python está difícil | Sprint 2, os exercícios 9 e 12 não saem | Comente na *issue* **na mesma semana**. Refaça os exercícios da Sprint 1 que ficaram frágeis antes de seguir. Não pule para a Sprint 3 sem o `ex09` funcionando: ele é o seu trabalho em miniatura |
| O TABNET fora do ar ou muito lento | Sprint 3, a página não abre ou a consulta não termina | Tente em outro horário (de manhã costuma ser melhor). Se continuar por mais de um dia, comente na *issue*, e eu envio os três arquivos do TABNET para você colocar em `dados/brutos/`. Registre no protocolo que os arquivos foram enviados pelo orientador, com a data de extração que aparece neles |
| O SIDRA não deixa baixar | Sprint 3, erro no download | Tente outro navegador. Se não funcionar, abra no navegador o endereço da API do SIDRA `https://apisidra.ibge.gov.br/values/t/4709/n6/in%20n3%2024/v/93/p/2022?formato=json`, salve a página como `dados/brutos/populacao_censo2022_rn.json` e registre no protocolo. O `ler_populacao` passa a ler esse JSON (*pesquise:* `pd.read_json`; a primeira linha é o cabeçalho, as colunas `D1C`, `D1N` e `V` são o código, o nome e a população) |
| A conferência com o TABNET não dá 100% | Sprint 6, municípios com números diferentes | Primeiro, confira a digitação contra o print. Se o TABNET mudou (a data de extração nas Notas é outra), os dados foram atualizados: baixe de novo os três arquivos seguindo o protocolo, rode todos os scripts na ordem e refaça a conferência. É para isso que o programa existe. Anote tudo: isso vai para o artigo |
| O tempo aperta na Sprint 7 | segunda, 30/11, sem o `estabilidade.py` | Faça só a amplitude por porte e o gráfico de dispersão; o gráfico de taxa por ano e a lista dos maiores de 20 mil viram extras |
| Atraso geral | qualquer sprint | Corte, nesta ordem: as regiões (Sprint 6), a lista dos maiores de 20 mil, os arquivos separados do I21 e do I46. **Não corte** as conferências (TABNET, planilha, reprodutibilidade) nem os testes: elas são o que faz o trabalho ser confiável |

**Se algo tiver de ser cortado, corte quantidade, não qualidade.** Uma lista de 10 municípios bem conferida vale mais que uma análise grande que ninguém consegue repetir.

---

<a id="extras"></a>
## 11. Se sobrar tempo (opcional)

Só depois de a sprint da semana estar entregue. Cada extra que você fizer vira um parágrafo a mais nos Resultados.

- **E1. Óbitos por ocorrência.** Baixe os mesmos dados com o Conteúdo **Óbitos p/Ocorrênc** e compare com os de residência: em quais municípios as pessoas morrem mais do que moram? Isso mostra para onde os pacientes do interior são levados (os municípios com hospitais).
- **E2. Outras causas sensíveis ao tempo.** Repita a análise para causas em que o SBV também faz diferença: **engasgo** (códigos W78 a W80) e **afogamento** (W65 a W74). Os números são pequenos; agregue por mesorregião.
- **E3. Taxa por Região de Saúde.** O TABNET oferece a Linha **Região de Saúde (CIR)**, que é a divisão usada pela Secretaria de Saúde para organizar o atendimento. Calcule a taxa por região de saúde, que é a escala em que o projeto pode conversar com a rede de urgência.
- **E4. Taxa padronizada por idade.** Baixe os óbitos por **Faixa Etária** no TABNET e a população por idade do Censo 2022 no SIDRA, e calcule a taxa padronizada pelo método direto, usando a população do RN como padrão. Compare a lista dos 10 maiores com a da taxa bruta: quantos continuam?

---

<a id="referencias-minimas"></a>
## 12. Referências mínimas do artigo

**Lado da saúde:**

- **as diretrizes de ressuscitação:** da American Heart Association (a versão de 2020, citada no projeto, ou a mais recente) e da Sociedade Brasileira de Cardiologia (seção 2.1);
- **Larsen *et al.* (1993)**, sobre a queda da sobrevivência a cada minuto (seção 2.1);
- **Ringh *et al.* (2015)**, sobre o acionamento de voluntários pelo celular (seções 2.1 ou 2.4);
- **o relatório "Estatística Cardiovascular - Brasil"** mais recente (Introdução);
- **1 ou 2 fontes sobre a qualidade da informação de causa de morte** no Brasil (seção 2.2).

**Lado dos dados:**

- **a documentação do SIM** e as Notas Técnicas do TABNET (Ministério da Saúde) (seção 2.2 e Metodologia);
- **a CID-10** (Organização Mundial da Saúde) (seção 2.2);
- **RIPSA. *Indicadores básicos para a saúde no Brasil: conceitos e aplicações*. 2. ed. Brasília: Organização Pan-Americana da Saúde, 2008**, para a definição de taxa de mortalidade (seção 2.3);
- **o Censo Demográfico 2022** (IBGE) (Metodologia);
- **3 ou 4 trabalhos relacionados** (seção 2.4).

**Lado técnico:**

- **McKinney, *Python para análise de dados*** (o livro do criador do `pandas`; procure a edição mais recente em português, da editora Novatec), para o `pandas`;
- **Hunter (2007)**, *Matplotlib: a 2D graphics environment*, na revista *Computing in Science & Engineering*, para o Matplotlib.

**Obrigatórias:**

- **2 obras de metodologia científica:** Gil (2017) e Prodanov e Freitas (2013), em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

Registre a referência completa de **tudo** o que ler, na seção de Referências do documento do Drive, desde o primeiro dia. Zotero e Mendeley ajudam a montar, mas confira cada entrada contra a NBR 6023:2018 antes de entregar: esses gerenciadores erram com frequência.
