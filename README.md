# DIO 
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

Linha horizontal: ---, *** ou ___ <br>
*** <br>
*** <br>
--- <br>
--- <br>
___ <br>
___

7. Tabelas
Use | para separar colunas e - para o cabeçalho:
| Cabeçalho 1 | Cabeçalho 2 |
|-------------|-------------|
| Linha 1     | Conteúdo    |
| Linha 2     | Mais texto  |

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
Você pode incluir diagramas escrevendo código dentro de blocos com a tag mermaid:

```mermaid
graph LR
  A --> B

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

## Git e Github
