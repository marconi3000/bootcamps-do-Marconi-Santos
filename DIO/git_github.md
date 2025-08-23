# :octocat: *Git e GitHub* :octocat:
## :one: Introdução
## **O que é git?**
>O Git é um sistema de controle de versão distribuído (DVCS) que permite rastrear mudanças em arquivos de projetos, mantendo um histórico completo localmente no computador do desenvolvedor — sem necessidade de conexão com a internet ou servidor central.

Características principais:
- Controle de versão distribuído: cada desenvolvedor possui todo o histórico do projeto localmente.
- Alta performance e suporte a fluxo não linear: criação rápida de branches, merges eficientes e navegação complexa do histórico.
- Segurança e integridade: cada mudança é identificada por um hash (SHA‑1), garantindo que o histórico seja imutável e rastreável.
Código aberto: criado por Linus Torvalds e mantido por colaboradores (GPLv2).

*O que é um Sistema de Controle de Versão Centralizado (CVCS)?*
<details><summary>Clique na setinha para expandir a explicação!</summary>
        Um CVCS (Centralized Version Control System) funciona com base em um repositório central onde todas as versões dos arquivos são armazenadas. Os desenvolvedores se conectam a esse servidor para fazer checkout de versões, enviar (commit) alterações e obter updates. É um modelo típico de cliente-servidor, onde:
    
    - Os usuários baixam a versão mais recente do repositório central para suas máquinas.
    - Fazem alterações localmente.
    - Enviam (commit) essas alterações de volta ao repositório central.
    - O servidor gerencia o histórico de versões e sincroniza os colaboradores.
    
    Vantagens:
    
    - Controle centralizado e visibilidade do que está sendo trabalhado.
    - Curva de aprendizado mais baixa, mais fácil de configurar e usar — ideal para equipes menores e projetos simples.
    - Bom com arquivos binários, pois não exige que cada usuário baixe todo o histórico.
    
    Desvantagens:
    
    - Ponto único de falha — se o servidor ficar offline, os commits e atualizações param.
    - Dependência da rede: operações lentas ou travadas sem acesso ao servidor.
    - Branching e merge costumam ser mais difíceis e propensos a conflitos.

</details>

*O que é um Sistema de Controle de Versão Distribuído (DVCS)?*
<details><summary>Clique na setinha para expandir a explicação!</summary>
        Um DVCS (Distributed Version Control System) é um sistema de versionamento em que cada desenvolvedor possui uma cópia completa do repositório, incluindo todo o histórico de commits. Isso permite trabalhar offline, fazer commits locais, criar branches de forma ágil e depois sincronizar com outros repositórios quando necessário — sem depender de um servidor central.
    
    Principais Vantagens:
    
    - Alta disponibilidade e resiliência: todo clone funciona como um backup completo.
    - Branching e merge eficientes: ramificações são rápidas e menos propensas a conflitos.
    - Trabalho offline: operações como commits, diffs, log e reverts são feitas localmente, sem rede.
    
    Importância dos DVCS hoje
    
    1. Redundância e backup confiável - Cada desenvolvedor possui um repositório completo com histórico. Isso significa que, mesmo diante de falhas no servidor central, qualquer máquina local pode servir como uma fonte para restaurar o repositório principal.
    
    2. Trabalho offline e maior produtividade - Operações como commit, diff, log e branch podem ser realizadas localmente, sem conexão com a internet, o que acelera o desenvolvimento e permite trabalhar em qualquer lugar.
    
    3. Branches e merges fáceis e rápidos - DVCS tornam a criação de branches leve e ágil, e os merges são feitos localmente com mais rapidez, favorecendo workflows inovadores e experimentação segura.
    
    4. Colaboração eficiente e escalável - Projetos open-source e equipes distribuídas se beneficiam de forma significativa: cada colaborador pode trabalhar à vontade, enviar pull requests, e mesclar alterações sem travar o fluxo de todos.
    
    5. Desempenho elevado - Como a maioria das tarefas é feita localmente, o desempenho é superior — commits e outras operações são instantâneos comparados aos sistemas centralizados.
    
    6. Traçabilidade e auditoria - É possível rastrear quem fez o quê, quando e por quê. Isso aumenta responsabilidade, facilita auditoria e manutenção de qualidade do código.
    
    7. Resiliência contra falhas - Sem um ponto único de falha, o ambiente de desenvolvimento se torna robusto. Mesmo que o servidor central apresente problemas, o trabalho continua normalmente localmente.
    
    8. Flexibilidade para workflows avançados - DVCS suportam modelos como forks, pull requests, emergentes em plataformas modernas (GitHub, GitLab etc.), facilitando revisões, CI/CD e governança distribuída.
    
    9. Adotado por projetos e empresas líderes - Git, o DVCS mais usado, é padrão na comunidade de código aberto e adotado em larga escala por empresas como Google e Facebook. Ferramentas como Mercurial e Bazaar também se destacam nesse ecossistema.
    
    10. Adoção ampla (Git como padrão de fato) - Git é hoje o sistema de controle de versão distribuído mais utilizado no mundo — estima-se que mais de 95% dos desenvolvedores o utilizem como sua ferramenta principal 
    
    Vantagens: Controle de histórico, Trabalho em Equipe, Ramificação do projeto, Segurança, Organização.
</details>  

## **O que é o GitHub?**

> O GitHub é uma plataforma online de hospedagem de repositórios Git, com foco em colaboração entre desenvolvedores.
> Permite que equipes armazenem, compartilhem e trabalhem em projetos de forma colaborativa na nuvem .

Recursos úteis do GitHub:

- Pull Requests: propôs, revisou e discute alterações antes de integrá-las ao código principal.
- Issues e quadros de projeto: ferramenta integrada para rastrear bugs ou gerenciar tarefas.
- Integração de CI/CD: com GitHub Actions, automatiza testes, builds e deploys.
- GitHub Pages: hospeda sites estáticos diretamente do repositório.
- Segurança e permissões avançadas: inclui autenticação, controle de acesso e varredura de código.
- Recursos sociais e comunidade: wikis, social graph, feeds para facilitar colaboração e networking.

Propriedade: atualmente é de propriedade da Microsoft (adquirida em 2018)

### **Principais diferenças**


|Aspecto	|Git	|GitHub|
|:-----:|:-----:|:-----:|
|Natureza|	Software de linha de comando, local	| Plataforma online, baseada na web |
|Controle de versão	| Gerencia histórico localmente |	Hospedagem de repositórios Git na nuvem |
|Colaboração |	Básica (via repositório remoto manual)	| Avançada (pull requests, issues, revisão de código)|
|Conexão com Internet	| Não necessária para operações básicas	| Requer para acessar recursos da plataforma|
|Interface	| CLI (ou GUI de terceiros)	| Interface web amigável, com integrados visuais|
|Licença/Propriedade |	Software livre e aberto	| Serviço comercial (Microsoft), com planos gratuitos e pagos|
|Recursos extras	| Controla versões, branching, merges	| Ferramentas sociais, CI/CD, wikis, GitHub Pages|

## **Instalação do Git no PC**

https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git

## **COMANDOS INICIAIS**

<pre>
echo "# NomeDoProjeto" >> README.md   # Cria um README inicial
git init                              # Inicializa o repositório local (cria pasta .git)
git add README.md                     # Adiciona o arquivo README à "stage"
git commit -m "first commit"          # Commita com uma mensagem inicial
git branch -M main                    # Renomeia a branch padrão para "main" (opcional)
git remote add origin https://github.com/seu-usuario/NomeDoProjeto.git  # Adiciona o repositório remoto
git push -u origin main               # Envia os commits locais para o GitHub e configura o rastreamento
</pre>

## **Configurações**
Clique com botão direito do mouse em uma pasta que deseja vincular com o GitHub. E selecione a opção "Open Git Bash here"

Digite: <pre>git config</pre>

O comando git config serve para configurar o comportamento do Git, permitindo definir diversas preferências —  
desde sua identidade (nome e e-mail) até personalizações avançadas como aliases e temas de cores, em níveis diferentes (local, global ou de sistema).

Você pode aplicar configurações em três níveis distintos:

|Nível	|Escopo	|Arquivo afetado|
|:-----:|:-----:|:-----:|
|<pre>--system</pre>	|Afeta todos os usuários e repositórios do sistema	|Ex: /etc/gitconfig|
|<pre>--global</pre>	|Afeta apenas o usuário atual	|~/.gitconfig|
|<pre>--local</pre> (padrão)	|Afeta somente o repositório em que está usando	|.git/config|

## **Definir nome de usuário e e-mail (identidade dos commits)**
<pre>
  git config --global user.name "Seu Nome"
  git config --global user.email "seu.email@example.com"

  Confira com git config --list 
  git config user.name - para visualizar o nome
  git config user.email - para visualizar o e-mail
</pre>

### Para que serve esse comando?

> * O Git utiliza duas informações essenciais para identificar quem fez cada alteração em um repositório: o nome do autor (user.name) e o e-mail do autor (user.email). 
Cada commit é carimbado com esses dados, tornando possível rastrear a autoria das alterações.
> * O uso da flag --global faz com que essas configurações sejam aplicadas a todos os repositórios do usuário no sistema, armazenando-as no arquivo ~/.gitconfig.

<pre>
        git config init.defaultBranch                        #Retornar a branch padrão
        git config --global init.defaultBranch main          #Para modificar para main utiliza o comando
        git config --global --list                           # retorna todas as configurações globais
</pre>

serves para abrir o arquivo de configuração global do Git (~/.gitconfig) diretamente no editor de texto padrão do Git, 
permitindo que você visualize e edite manualmente as configurações globais.

## Alterar o nome de usuário e e-mail globalmente

<pre>
        git config --global user.name "Seu Novo Nome"             # Isso sobrescreve os valores antigos com os novos.
        git config --global user.email "novo-email@exemplo.com"   # Isso sobrescreve os valores antigos com os novos.
        git config --global --list                                # para confirmar
</pre>

## Alterar para um repositório específico (configuração local)

<pre>
        git config user.name "Nome para este repo"        # afeta apenas o repositório atual e deixa o valor global intacto.
        git config user.email "email@repo.com"            # afeta apenas o repositório atual e deixa o valor global intacto.
</pre>

## Remover configurações existentes

<pre>
        git config --global --unset user.name
        git config --global --unset user.email

        # Para remover todas as entradas duplicadas
        git config --global --unset-all user.name
        git config --global --unset-all user.email
</pre>

## Como funciona o --edit (Editar Manualmente)
<details><summary>Clique na setinha para expandir a explicação!</summary>

O Git utiliza uma variável chamada core.editor para definir qual editor será usado ao editar arquivos com git config --edit.

Se você ainda não definiu um editor personalizado, o comando git config --global --edit usará o editor padrão do sistema, 
que pode ser o vi, vim, nano, ou outro, dependendo da configuração.

Ao editar e salvar o arquivo, suas alterações são imediatamente aplicadas à próxima execução de comandos Git.

<pre>git config --global --edit</pre>

### Como sair do editor Vim

Saia do modo de inserção. Se estiver digitando (modo "INSERT"), pressione Esc para voltar ao modo normal.

Digite o comando de saída desejado:

:wq → write (salvar) e quit (sair): salva as mudanças e fecha.

:q! → quit sem salvar: descarta alterações e fecha o editor.

Pressione Enter para confirmar o comando.

### Se você não se sente confortável usando o Vim, pode configurar um editor mais amigável como Nano ou VS Code:

<pre>git config --global core.editor "nano"</pre>
#### ou
<pre>git config --global core.editor "code --wait"</pre>

Após realizar a alteração no VScode é só salvar e fechar

</details>

## Token de Acesso Pessoal (PAT – Personal Access Token)

Antes de gerar um token, é importante garantir que seu endereço de e-mail esteja verificado no GitHub.

* Acesse Settings (Configurações) da sua conta.
* Vá até Emails (normalmente na seção "Access" ou similar).
* Verifique se há algum e-mail com status “unverified” (não verificado) e clique em Resend verification email se necessário.

Usando o formato fine-grained (mais seguro).
* No GitHub, clique no seu perfil → Settings.
* Acesse Developer settings na barra lateral.
* Vá em Personal access tokens → Fine‑grained tokens.
* Clique em Generate new token.
* Preencha:
    * Nome do token (para você identificar depois).
    * Data de expiração.
    * Permissões: defina quais repositórios serão acessados e quais operações são permitidas (escolha com base no menor privilégio necessário).
* Clique em Generate token e copie imediatamente. Não será mostrado novamente.


#### Usando o formato classic (mais global)
* Vá em Settings → Developer settings → Personal access tokens → Tokens (classic).
* Clique em Generate new token (classic).
* Defina o nome, data de expiração e selecione scopes (como repo para acesso a repositórios privados e públicos).
* Gere e copie o token imediatamente.


### Como usar o token no Git (via HTTPS)

<pre>git clone https://github.com/usuario/repositorio.git</pre>

No prompt de Git: 
* Use seu nome de usuário normal do GitHub.
* Quando pedir a senha, cole o token no lugar.

Para repositórios já existentes, basta atualizar o remoto:

<pre>git remote set-url origin https://username:seu-token@github.com/usuario/repositorio.git</pre>

## O que faz o credential helper?

<pre>
        git config --global credential.helper store

        git config --global --show-origin credential.helper  # saber de onde uma configuração do Git está sendo lida
        
        git config --global credential.helper store # armazenar permanentemente suas credenciais (usuário e senha ou token) em um arquivo no seu disco, 
        permitindo que você autentique automaticamente em operações futuras sem precisar digitar os dados toda vez.
        
        git config --global credential.helper "cache --timeout=3600"        # Cache por 1 hora

        
</pre>
🧠 Saiba mais - https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage

> Sem um helper configurado, o Git solicitará suas credenciais toda vez que precisar autenticar com um repositório remoto.
> O helper automatiza esse processo, evitando a repetição e garantindo mais segurança ou conveniência, dependendo do tipo de armazenamento escolhido.


### Por que usar um credential helper?

> Além de evitar digitação repetitiva, os helpers melhoram a segurança — especialmente quando usam armazenamento criptografado,
> como keychains ou managers do sistema. Em repositórios sensíveis, isso protege tokens ou senhas de exposição desnecessária.

### Como remover ou resetar o helper?

<pre>
        git config --global --unset credential.helper        # volte a pedir suas credenciais a cada operação.
        
</pre>

## Etapas para configurar Autenticação SSH com GitHub

1. Verifique se você já tem uma chave SSH. No terminal (Git Bash, Terminal, etc.), rode:

<pre>ls -al ~/.ssh</pre>

Gere uma nova chave SSH (Caso não tenha). Para criar uma chave segura, prefira o algoritmo ed25519:

<pre>ssh-keygen -t ed25519 -C "seu_email@exemplo.com"        # A flag -C adiciona um comentário (geralmente seu e-mail), útil para identificar a chave depois</pre>        .

Se seu sistema não suportar ed25519, use RSA:

<pre>ssh-keygen -t rsa -b 4096 -C "seu_email@exemplo.com"</pre>

Adicione a chave SSH ao SSH-agent. Inicie o SSH agent:

<pre>eval "$(ssh-agent -s)"</pre>

E adicione sua chave privada gerada:

ssh-add ~/.ssh/id_ed25519

Se for RSA, ajusta o nome do arquivo conforme necessário.

Copie a chave pública para o GitHub. Copie o conteúdo da chave pública:

<pre>
        clip < ~/.ssh/id_ed25519.pub          # Windows:
        pbcopy < ~/.ssh/id_ed25519.pub        # macOS
        cat ~/.ssh/id_ed25519.pub             # Linux:
</pre>

Depois, vá para **GitHub** → **Settings** → **SSH and GPG keys** → **New SSH key**, cole o texto, dê um título e salve.

Teste sua conexão SSH. No terminal, digite:

<pre>ssh -T git@github.com</pre>

Você deverá ver algo como: Hi username! You've successfully authenticated, but GitHub does not provide shell access.

Use URLs SSH em vez de HTTPS. Para clonar novos repositórios via SSH:

<pre>git clone git@github.com:usuario/repositorio.git</pre>

Se já tiver um remoto configurado com HTTPS, altere para SSH:

<pre>git remote set-url origin git@github.com:usuario/repositorio.git</pre>

Ou siga o caminho pelo link https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys

Se você já vir arquivos como id_rsa e id_rsa.pub — você já possui um par de chaves. Caso contrário, precisa gerar um.

Escolher o editor padrão para mensagens de commit:

<pre>git config --global core.editor "code --wait"</pre>

Criar aliases (atalhos) para comandos frequentes:

<pre>
        git config --global alias.ci commit
        git config --global alias.st status
</pre>

Ajustar estilo de saída (cores):

<pre>git config --global color.ui auto</pre>

Isso habilita coloração na saída dos comandos Git, tornando as informações mais fáceis de ler. 

Configurar ferramenta de merge externa:

<pre>git config --global merge.tool meld</pre>

Isso configura o Git para usar a ferramenta "meld" ao resolver conflitos. 

Listar todas as configurações atuais:

<pre>git config --list</pre>

Consultar um valor específico:

<pre>git config user.email</pre>

Remover uma configuração:

<pre>git config --global --unset alias.ci</pre>

Editar o arquivo de configuração diretamente:

<pre>git config --global --edit</pre>


<pre></pre>
<pre></pre>
<pre></pre>
<pre></pre>
<pre></pre>
<pre></pre>





### **Comandos Git via Terminal Integrado**

<pre>
git init                  # Inicializa o repositório
git clone <url>           # Clona um repositório remoto
git status                # Mostra o estado atual do arquivo
git add .                 # Adiciona todos os arquivos
git commit -m "msg"       # Cria um commit
git push -u origin main   # Envia para o remoto
git pull                  # Puxa atualizações do remoto
git branch                # Lista branches
git checkout -b nome      # Cria e acessa uma nova branch
git merge outra-branch    # Mescla outra-branch com a atual
git stash                 # Armazena alterações temporariamente
</pre>


### **COMANDOS**

        mkdir nome_do_diretorio                # Criar um diretório simples
        mkdir -p pasta/filho1/filho2           # Criar diretórios aninhados de uma só vez

        touch nome_do_arquivo.ext                   # cria um arquivo vazio ou atualiza a data de modificação se ele já existir.
        touch arquivo1.txt arquivo2.js imagem.png   # Criar múltiplos arquivos simultaneamente
        echo "Texto inicial" > arquivo.txt          # Criar e adicionar conteúdo no mesmo comando
        nano arquivo.txt                            # Criar e começar a editar imediatamente com o editor padrão
        OU
        vi arquivo.txt

    git commit -m"contato da mensagem de commit": Gravação de arquivo no git. Esse comando serve para enviar os arquivos no git. 
    O "-m" é referente ao termo "mensseger". Ou seja, mensagem que será gravada no commit.
    
    ctrl + l = É o comando que limpa a tela do terminal do git.
    
    git log: Comando para visualizar os logs dos arquivos gravados no repositório.
    
    git remote add origin + endereço da pasta no github: Esse comando permite indicar para o repositório no github. Ou seja, 
    o usuário cria uma página no github e pode direcionar uma página do seu computador local para a pasta do github sem precisa clonar o repositório.
    
    git clone + endereço da pasta no github: Esse comando serve para clonar um projeto no github.
    
    gitignore: Arquivo para ser criado no git e evita que determinados arquivos sejam adicionais. Ou seja, o git vai ignorar os arquivos que estão dentro dele.
    
    Exemplo: touch .gitignore (Criar arquivo dentro da pasta determinada) echo "nome do arquivo que você quer ignorar" >> .gitignore 
    (Escreve dentro do arquivo do gitignore o nome do arquivo que você quer ignorar.).
    
    git add .gitignore: Adicionando o gitignore detro do githubIgnorando todos os arquivos de uma extensão: echo "*.log" >> .gitignore
    
    Ignorando um diretório inteiro:  echo "pastaignorada/" >> .gitignore
    
    git commit -am"Rastreando/adicionando e confirmando ao mesmo tempo um arquivo."
    
    git log -n 3: Comando mostra os três últimos commits.
    
    git log --oneline: Resumo dos commits feitos no projeto.
    
    git log --state: Mostra o resumo dos arquivos alterados com o número de linhas alteradas e removidas.
    
    git rm nomedoarquivo: Esse comando serve para remover/deletar um arquivo do repositório. Todo arquivo removido precisa ser commitado - Não esqueça disso.
    
    git mv nomeantigo nome_novo: O comando "mv" altera o nome de um arquivo. Ou seja, renomeia o arquivo existente, exemplo:
    
      git mv algo01.py algoritmo01.py
    
    git checkout -- nomedoarquivo: Esse comando permite fazer uma alteração em um arquivo específico, exemplo:
    
      echo "Mudança no arquivo!" >> arquivo.txt -> Efetuado alteração no arquivo.
    
    git checkout -- arquivo.txt: Cancelando a última alteração do arquivo. Lembrando, as alterações só podem ser corrigidas se estiverem 
    fora do palco. Ou seja, antes de adicionar o arquivo com o comando -> git add nomedoarquivo.
    
    git reset --hard: Comando para desfazer todas as modificações que você fez.
    
    git branch novo_branch: Comando para criar um novo branch.
    
    git branch: Comando para listar as ramificações existentes.
    
    git checkout novo_branch: Comando para mudar de branch.
    
    git checkout -b nova_branch: Comando cria uma nova branch e troca para ela ao mesmo tempo.
    
    git branch -d nova_branch: Comando deletar um branch criado.
    
    OBS: Uma filial só pode ser excluída se o usuário não estiver nela. Ou seja, o desenvolvedor deve mudar de branch com o comando 
    "git checkout master" (por exemplo) e deletar o branch que deseja.
    
    git branch -D nova_branch: O comando usando o "-D" (letra secretos) é usado quando existe commit na branch.
    
    git branch --no-merged: Comando para identificar se existe alguma branch não mesclada.
    
    git merge nova_branch -m"Mensagem sobre a mesclagem do branch.": Esse comando mescla a nova_branch ao master.

**Atalhos nativos do Bash (funcionam no Git Bash)**
<details><summary>Clique na setinha para expandir a explicação!</summary>

                Esses atalhos facilitam a edição de linha, movimentação e histórico de comandos:
                
                Ctrl + A: Vai para o início da linha
                
                Ctrl + E: Vai para o final da linha
                
                Ctrl + K: Deleta do cursor até o fim da linha
                
                Ctrl + U: Deleta do cursor até o início da linha
                
                Ctrl + W: Deleta a palavra antes do cursor
                
                Ctrl + Y: Cola o texto deletado no cursor
                
                Alt + B / Alt + F: Move uma palavra para trás / para frente
                
                Alt + D: Deleta da posição do cursor até o fim da palavra
                
                Alt + C / Alt + U / Alt + L: Converte o caractere ou palavras à direita do cursor em maiúsculas / maiúsculas até o fim da palavra / minúsculas até o fim da palavra
                
                Ctrl + R: Busca incremental no histórico de comandos
                
                Ctrl + L: Limpa a tela (similar ao comando clear)
                
                Ctrl + C: Interrompe o comando em execução
                
                Tab: Completa nomes de arquivo ou comandos automaticamente

</details>

Setas e Símbolos Diversos

Um conjunto diverso de símbolos e setas com seus shortcodes:

:one: → 1️⃣
:hash: → #️⃣
:arrow_down: → ⬇️
:arrow_up: → ⬆️
:arrow_right: → ➡️
⬅️
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
