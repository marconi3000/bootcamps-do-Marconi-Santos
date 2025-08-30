## Para abrir a paleta com os emojis pressione a tecla Windows + (.)
## [README.md](https://readme.so/pt/editor)
## Imagens  
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)
## Como escrever no github - [Aqui](https://docs.github.com/pt/get-started/writing-on-github)

## Atalhos do Teclado - [Aqui](https://docs.github.com/pt/get-started/accessibility/keyboard-shortcuts)

## Alertas  
> [!NOTE]
[!NOTE]  
> Useful information that users should know, even when skimming content.,

> [!TIP]   
[!TIP]  
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]  
[!IMPORTANT]  
> Key information users need to know to achieve their goal.

> [!WARNING]    
[!WARNING]  
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]    
[!CAUTION]  
Advises about risks or negative outcomes of certain actions.  

## Sintaxe em Markdown

Markdown é uma linguagem de formatação leve que transforma texto simples em conteúdo com estilo, como cabeçalhos, negrito, listas e links — ideal para usar em arquivos como README.md, issues, pull requests, wikis e comentários no GitHub.

1. Cabeçalhos
Use # seguido de espaço para criar cabeçalhos; mais # gera um título menor: <br>
\# Título H1 <br>
\## Título H2 <br>
\### Título H3

2. Ênfase (Negrito e Itálico) <br>
Itálico: \*texto\* ou \_texto\_ <br>
Negrito: \**texto\** ou \__texto\__ <br>
Combinação possível: \*Você \*\*pode\*\* fazer isso\* <br>

3. Listas
Não ordenada: use \*, \- ou \+
* Item A
* Item B <br>
  * Subitem C
    * Subitem D <br>
    
Use pelo menos 2 a 4 espaços antes do * para criar um nível recuado.<br>
Ordenada: números com ponto (1., 2.)
1. Primeiro
2. Segundo

4. Links e Imagens
Link: \[texto\]\(URL\)
Imagem: \!\[alt text\]\(URL_da_imagem\)
\[GitHub\]\(https://github.com)
\!\[Logo GitHub\]\(https://github.com/logo.png/)

5. Código
Inline: use crases simples \`código\` <br>
Bloco: crases triplas, com opção de especificar linguagem para realce de sintaxe: <br>
\<pre\> \```javascript console.log\('Olá, mundo!'\); ``` \</pre\>

6. Citações e Linhas Horizontais
Citação: comece a linha com > <br>
> Este é um bloco de citação <br>

Linha horizontal: ---, *** ou ___ 

***

7. Tabelas
Use | para separar colunas e - para o cabeçalho: <br>

| Cabeçalho 1 | Cabeçalho 2 |
|-------------|-------------|
| Linha 1     | Conteúdo    |
| Linha 2     | Mais texto  |

Definindo Alinhamentos de Coluna
Você ainda pode controlar o alinhamento de textos nas colunas, usando dois pontos (:): <br>
:--- → Alinhamento à esquerda <br>
:---: → Alinhamento centralizado <br>
---: → Alinhamento à direita <br>

| Esquerda | Centralizado | Direita |
| :------- | :---------:  | ------: |
| Texto    | Texto        | Texto   |

8. Task Lists (Listas de Tarefas)
Ideal para checklists em issues ou PRs:
- [x] Tarefa concluída
- [ ] Tarefa pendente

9. Menções e Referências
Mencionar usuário: @username
Referenciar issue/PR: #123 cria link automaticamente 

10. Risque texto com ~~texto~~ 
roachhd.gitbooks.io

11. Emoji
Use códigos entre dois pontos, como :smile: 

12. Diagramas com Mermaid
Você pode incluir diagramas escrevendo código dentro de blocos com a tag \mermaid: <br>

```mermaid
graph LR;
  A --> B;

```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;

13. Escapar com barra invertida \
A forma mais simples e direta é colocar uma barra invertida \ antes do caractere que você quer que seja exibido literalmente, e não interpretado como sintaxe Markdown. Isso funciona para todos os seguintes caracteres:

\  backslash
`  crase (backtick)
*  asterisco
_  underscore (sublinhado)
/{ }/ chaves
/[ ]/ colchetes
/( )/ parênteses
#  cerquilha (hash)
+  sinal de adição
-  hífen ou marcador de lista
.  ponto
!  exclamação
|  pipe (|) — especialmente útil em tabelas

14. Emon=ji
expressões Faciais e Sentimentos
:smile: → 😄
:laughing: → 😆
:blush: → 😊
:smiley: → 😃
:relaxed: → ☺️
:heart_eyes: → 😍
:scream: → 😱
:sob: → 😭

Corações e Símbolos Românticos
:heart: → ❤️
:broken_heart: → 💔
:two_hearts: → 💕

Reações e Objetos
:tada: → 🎉
:sparkles: → ✨
:thumbsup: ou :+1: → 👍
:thumbsdown: ou :-1: → 👎
:fire: → 🔥
:poop: → 💩

Setas e Gestos
:point_up: → ☝️
:point_down: → 👇
:point_left: → 👈
:point_right: → 👉
:clap: → 👏
:pray: → 🙏

Animais e Natureza
:dog2: → 🐕
:cat2: → 🐈
:panda_face: → 🐼
:banana: → 🍌
:corn: → 🌽

Objetos e Dispositivos
:computer: → 💻
:iphone: → 📱
:tv: → 📺
:camera: → 📷
:gift: → 🎁

Emojis Especiais (Custom Emotes do GitHub)
Estes emojis são exclusivos do GitHub e geralmente aparecem como imagens estilizadas:
:bowtie: → 👔 (laço)
:octocat: → (mascote Octocat)
:shipit: → (um gato de navio)
:trollface: → (trollface)
:neckbeard:, :feelsgood:, :finnadie:, :goberserk:, :godmode:, :hurtrealbad:,
:rage1:, :rage2:, :rage3:, :rage4:, :suspect:
são outros exemplos dessas custom emojis no GitHub

alguns objetos comuns e seus shortcodes:
:bulb: → 💡
:hammer: → 🔨
:mag: → 🔍
:computer: → 💻
:iphone: → 📱
:headphones: → 🎧
:lock: → 🔒
:key: → 🗝️
:toolbox: → 🧰
:wrench: → 🔧
:door: → 🚪
:file_cabinet: → 🗄️
:toilet_paper: → 🧻 

Itens do Dia a Dia e Presente
:school_satchel: → 🎒
:mortar_board: → 🎓
:fireworks: → 🎆
:santa: → 🎅
:christmas_tree: → 🎄
:gift: → 🎁
:bell: → 🔔
:tada: → 🎉
:crystal_ball: → 🔮
:camera: → 📷
:tv: → 📺 

Escrita, Estudo e Ferramentas de Escrita
:bookmark_tabs: → 📑
:bar_chart: → 📊
:chart_with_upwards_trend: → 📈
:scroll: → 📜
:clipboard: → 📋
:calendar: → 📆
:file_folder: → 📁
:pencil2: → ✏️
:books: → 📚
:microscope: → 🔬
:musical_score: → 🎼
:violin: → 🎻
:video_game: → 🎮 

Setas e Símbolos Diversos
Um conjunto diverso de símbolos e setas com seus shortcodes:
:one: → 1️⃣
:hash: → #️⃣
:arrow_down: → ⬇️
:arrow_up: → ⬆️
:arrow_right: → ➡️
:information_source: → ℹ️
:ok: → 🆗
:new: → 🆕
:zero: → 0️⃣
:underage: → 🔞
:no_entry_sign: → 🚫
:clock1: → 🕐
:tm: → ™️
:white_check_mark: → ✅
:heavy_check_mark: → ✔️
:x: → ❌ 
