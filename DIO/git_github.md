# :octocat: *Git e GitHub* :octocat:

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>O que é git?</summary>  
        
> O Git é um sistema de controle de versão distribuído (DVCS) que permite rastrear mudanças em arquivos de projetos, mantendo um histórico completo localmente no computador do desenvolvedor — sem necessidade de conexão com a internet ou servidor central.
Características principais:
- Controle de versão distribuído: cada desenvolvedor possui todo o histórico do projeto localmente.
- Alta performance e suporte a fluxo não linear: criação rápida de branches, merges eficientes e navegação complexa do histórico.
- Segurança e integridade: cada mudança é identificada por um hash (SHA‑1), garantindo que o histórico seja imutável e rastreável.
Código aberto: criado por Linus Torvalds e mantido por colaboradores (GPLv2).  
        
</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>O que é um Sistema de Controle de Versão Centralizado (CVCS)</summary>
        
> Um CVCS (Centralized Version Control System) funciona com base em um repositório central onde todas as versões dos arquivos são armazenadas. Os desenvolvedores se conectam a esse servidor para fazer checkout de versões, enviar (commit) alterações e obter updates. É um modelo típico de cliente-servidor, onde:
    
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

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>O que é um Sistema de Controle de Versão Distribuído (DVCS)?</summary>  
        
> Um DVCS (Distributed Version Control System) é um sistema de versionamento em que cada desenvolvedor possui uma cópia completa do repositório, incluindo todo o histórico de commits. Isso permite trabalhar offline, fazer commits locais, criar branches de forma ágil e depois sincronizar com outros repositórios quando necessário — sem depender de um servidor central.
    
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

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>O que é o GitHub?</summary>

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

</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>Principais diferenças</summary>

|Aspecto	|Git	|GitHub|
|:-----:|:-----:|:-----:|
|Natureza|	Software de linha de comando, local	| Plataforma online, baseada na web |
|Controle de versão	| Gerencia histórico localmente |	Hospedagem de repositórios Git na nuvem |
|Colaboração |	Básica (via repositório remoto manual)	| Avançada (pull requests, issues, revisão de código)|
|Conexão com Internet	| Não necessária para operações básicas	| Requer para acessar recursos da plataforma|
|Interface	| CLI (ou GUI de terceiros)	| Interface web amigável, com integrados visuais|
|Licença/Propriedade |	Software livre e aberto	| Serviço comercial (Microsoft), com planos gratuitos e pagos|
|Recursos extras	| Controla versões, branching, merges	| Ferramentas sociais, CI/CD, wikis, GitHub Pages|

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

[Instalação do Git no PC](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git)  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>Comandos iniciais</summary>
<pre>
echo "# NomeDoProjeto" >> README.md   # Cria um README inicial
git init                              # Inicializa o repositório local (cria pasta .git)
git add README.md                     # Adiciona o arquivo README à "stage"
git commit -m "first commit"          # Commita com uma mensagem inicial
git branch -M main                    # Renomeia a branch padrão para "main" (opcional)
git remote add origin https://github.com/seu-usuario/NomeDoProjeto.git  # Adiciona o repositório remoto
git push -u origin main               # Envia os commits locais para o GitHub e configura o rastreamento
</pre>

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>Configurações</summary>

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

**Definir nome de usuário e e-mail (identidade dos commits)**

<pre>
  git config --global user.name "Seu Nome"
  git config --global user.email "seu.email@example.com"

  Confira com git config --list 
  git config user.name - para visualizar o nome
  git config user.email - para visualizar o e-mail
</pre>

**Para que serve esse comando?**

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

**Alterar o nome de usuário e e-mail globalmente**

<pre>
        git config --global user.name "Seu Novo Nome"             # Isso sobrescreve os valores antigos com os novos.
        git config --global user.email "novo-email@exemplo.com"   # Isso sobrescreve os valores antigos com os novos.
        git config --global --list                                # para confirmar
</pre>

**Alterar para um repositório específico (configuração local)**  

<pre>
        git config user.name "Nome para este repo"        # afeta apenas o repositório atual e deixa o valor global intacto.
        git config user.email "email@repo.com"            # afeta apenas o repositório atual e deixa o valor global intacto.
</pre>

**Remover configurações existentes**  

<pre>
        git config --global --unset user.name
        git config --global --unset user.email

        # Para remover todas as entradas duplicadas
        git config --global --unset-all user.name
        git config --global --unset-all user.email
</pre>  

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Como funciona o --edit (Editar Manualmente)</summary>

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

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->


<details><summary>Token de Acesso Pessoal (PAT – Personal Access Token)</summary>
        
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


## Como usar o token no Git (via HTTPS)

<pre>git clone https://github.com/usuario/repositorio.git</pre>

No prompt de Git: 
* Use seu nome de usuário normal do GitHub.
* Quando pedir a senha, cole o token no lugar.

Para repositórios já existentes, basta atualizar o remoto:

<pre>git remote set-url origin https://username:seu-token@github.com/usuario/repositorio.git</pre>

</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>O que faz o credential helper?</summary>
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


**Por que usar um credential helper?**

> Além de evitar digitação repetitiva, os helpers melhoram a segurança — especialmente quando usam armazenamento criptografado,
> como keychains ou managers do sistema. Em repositórios sensíveis, isso protege tokens ou senhas de exposição desnecessária.

**Como remover ou resetar o helper?**

<pre>
        git config --global --unset credential.helper        # volte a pedir suas credenciais a cada operação.
        
</pre>  

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->


<details><summary>Etapas para configurar Autenticação SSH com GitHub</summary>

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

</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Resolvendo problemas de Git Push e Pull e Autenticação SSH com GitHub</summary>

Esse erro:

> git@github.com: Permission denied (publickey).
> fatal: Could not read from remote repository.
> Please make sure you have the correct access rights
> and the repository exists.


> significa que o Git não conseguiu autenticar usando sua chave SSH ao tentar acessar o repositório remoto no GitHub.

🔍 O que causa esse erro?

Esse erro ocorre geralmente por um dos seguintes motivos:

| Causa | Explicação |
|:-----:|:-----:|
| ❌ Chave SSH não configurada | Você ainda não gerou ou adicionou uma chave SSH no seu computador.|  
| ❌ Chave SSH não adicionada ao GitHub | Você tem uma chave, mas ela não está registrada no GitHub. |  
| ❌ Usando o endereço SSH sem ter suporte para ele | Você está tentando usar git@github.com:... (via SSH), mas nunca configurou o acesso SSH. |  
| 🔐 Permissões incorretas no repositório | Seu usuário não tem permissão para acessar esse repositório. |  
| 🧱 Firewall/SSH bloqueado | Algumas redes corporativas ou educacionais bloqueiam conexões SSH. |  
✅ Como resolver passo a passo
🛠️ 1. Verifique se você já tem uma chave SSH  
No terminal, digite:  
> `ls ~/.ssh`  

Procure por arquivos como id_rsa e id_rsa.pub ou id_ed25519 e id_ed25519.pub.  
Se não tiver, crie com:  
> `ssh-keygen -t ed25519 -C "seu-email@example.com"`  
> Pressione Enter para aceitar os valores padrão.

🔑 2. Adicione a chave SSH ao GitHub  
> Copie o conteúdo da sua chave pública:
> `cat ~/.ssh/id_ed25519.pub`  
> Vá para https://github.com/settings/keys  
> Clique em "New SSH key".  
> Cole a chave no campo e dê um nome (ex: "Meu PC").  

🔄 3. Adicione sua chave SSH ao agente  
- Execute:
> `eval "$(ssh-agent -s)"`  
> `ssh-add ~/.ssh/id_ed25519`  

📡 4. Teste sua conexão com o GitHub  
> `ssh -T git@github.com`  
> Se tudo estiver certo, a resposta será algo como:  
> `Hi seu-usuario! You've successfully authenticated, but GitHub does not provide shell access.`  

🔁 5. Alternativa: Use HTTPS em vez de SSH   
> Se preferir evitar SSH, mude a URL do repositório para HTTPS:  
> `git remote set-url origin https://github.com/seu-usuario/repositorio.git`  
> Aí você usará seu login/senha (ou token) ao fazer git push/git pull.  

Apareceu este erro  

```
To github.com:seu-repo/pasta.git  
 ! [rejected]        main -> main (fetch first)  
error: failed to push some refs to 'github.com:seu-repo/pasta.git'    
hint: Updates were rejected because the remote contains work that you do not    
hint: have locally. This is usually caused by another repository pushing to    
hint: the same ref. If you want to integrate the remote changes, use    
hint: 'git pull' before pushing again.    
hint: See the 'Note about fast-forwards' in 'git push --help' for details.    
```

Esse erro:  

```  
! [rejected]        main -> main (fetch first)  
error: failed to push some refs to 'github.com:seu-repo/pasta.git'  
hint: Updates were rejected because the remote contains work that you do not  
hint: have locally.
```  
> significa que o repositório remoto (no GitHub) já tem commits que não existem no seu repositório local, e por isso o Git rejeitou seu git push para evitar sobrescrever essas mudanças.

🧠 O que está acontecendo?  
> Você está tentando dar git push para a branch main.  
> Mas o Git detectou que o repositório remoto tem commits diferentes dos seus.    
> Para proteger o histórico do projeto, o Git exige que você primeiro atualize sua cópia local com git pull.  

✅ Como resolver corretamente  
📌 Etapa 1: Fazer o pull (trazendo as mudanças do remoto)  
- Se você ainda não fez git pull, faça agora:  
- `git pull origin main --rebase`  
- O --rebase tenta aplicar suas mudanças por cima das que estão no GitHub, evitando um commit de merge.  

📌 Etapa 2: Resolver conflitos (se houver)  
- Se houver conflitos, o Git mostrará os arquivos com problemas. Aí você precisa:  
- Abrir os arquivos com conflito.  
- Corrigir os trechos marcados (<<<<<<<, =======, >>>>>>>).  
- Salvar os arquivos.  
- Adicionar ao stage novamente:  
- `git add .`

Continuar o rebase:  
- `git rebase --continue`

📌 Etapa 3: Agora sim, faça o push  
- Depois de resolver tudo e estar atualizado com o repositório remoto:  
- `git push origin main`  
- ❗ Alternativa perigosa (forçar push – só se você souber o que está fazendo)    
- Se você quiser descartar tudo o que está no GitHub e forçar seu código local a sobrescrever, use:  
        - `git push origin main --force`  

> ⚠️ Isso pode apagar mudanças no GitHub feitas por outras pessoas. Evite esse comando se estiver colaborando com outras pessoas ou se não tiver certeza do que está fazendo.  

✅ Resumo do caminho seguro   
> `git pull origin main --rebase`    
> corrige conflitos se houver  
> `git push origin main`  

</details> 

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  


<details><summary>Criar site no GitHub</summary>  

Suba os arquivos para o GitHub  

Usando Git no terminal:  

> `git init`  
> `git add .`  
> `git commit -m "first commit"`  
> `git branch -M main`  
> `git remote add origin https://github.com/seu-usuario/meu-site.git`  
> `git push -u origin main`

Ou via GitHub (upload manual):  
- Acesse seu repositório no GitHub.  
- Vá em Add file > Upload files.  
- Selecione todos os arquivos do seu projeto.  
- Clique em Commit changes.  

Configure o GitHub Pages    
- No repositório, clique em Settings.  
- Vá em Pages (geralmente no menu lateral).  
- Em Source, selecione:  
  - Branch: main  
  - Folder: / (root)  
  - Clique em Save.  
GitHub vai gerar uma URL como:
`https://seu-usuario.github.io/meu-site/`

Acesse suas páginas  
| Página | URL |  
|:-----:|:-----:|
| index.html | https://seu-usuario.github.io/meu-site/ |  
| contato.html | https://seu-usuario.github.io/meu-site/contato.html |  
| sobre.html | https://seu-usuario.github.io/meu-site/sobre.html | 


</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Criando e clonando repositório</summary>  

       mkdir nome_da_pasta                   # Criar uma pasta simples  
       mkdir pasta1 pasta2 pasta3            # Criar múltiplas pastas de uma vez  
       mkdir projetos/react/app              # Criar uma pasta dentro de outra (subpastas)  
       mkdir -p projetos/react/app           # Criar subpastas automaticamente com -p  
       cd nome_da_pasta                      # Acessar a pasta criada  
       git init                              # Cria um novo repositório Git localmente na pasta onde você executa o comando.  
       ls                                    # lista os arquivos e pastas do diretório atual no terminal.  
       cat                                   # cat é um comando do terminal que significa "concatenate", mas na prática é muito usado para visualizar arquivos de texto.  
       config                                # config é apenas o nome do arquivo. Pode ser qualquer arquivo de texto com esse nome.  
       cat config                            # Mostra o conteúdo do arquivo config  
       cat .git/config                       # Mostra as configurações do repositório Git local  
       git clone <URL>                       # Copia (clona) um repositório Git que está no GitHub (ou outro servidor) para a sua máquina.  
       cd ..                                 # Volta um nível de diretório
       git remote add origin <URL>           # Explicando por partes: git remote: comando usado para gerenciar repositórios remotos (ex: GitHub, GitLab, Bitbucket).
                                             # add: subcomando que adiciona um novo repositório remoto.
                                             # origin: é o nome padrão usado para se referir ao repositório remoto. Você pode dar outro nome, mas "origin" é o mais comum.
                                             # <URL>: é o endereço do repositório remoto (por exemplo, https://github.com/seu-usuario/seu-repo.git ou git@github.com:seu-usuario/seu-repo.git).
                                             # liga seu repositório local ao repositório remoto, para que você possa:
                                             # Enviar (push) suas alterações com git push origin main
                                             # Receber (pull) atualizações com git pull origin main
                                             # Clonar repositórios a partir desse endereço
      Exemplo de uso completo:               
      git init                               # inicia o repositório local
      git add .                              # adiciona os arquivos
      git commit -m "primeiro commit"
      git remote add origin https://github.com/usuario/repositorio.git
      git push -u origin main                # envia para o repositório remoto
      cat config                             # exibir as configurações locais do repositório Git.                                                  

1. Vá até o repositório no GitHub  
👉 https://github.com/marconi4000/cristo_exaltado  
2. Clique no botão verde <> Code - Ele fica perto do canto superior direito do repositório.  
3. Copie a URL de clonagem Você verá opções como:  
* HTTPS → Mais simples e comum  
https://github.com/marconi4000/cristo_exaltado.git  
* SSH → Mais avançado (requer chave SSH configurada)  
Para iniciantes, use a opção HTTPS.  
Clique no ícone de copiar 📋.  
4. Abra o terminal e rode:  
git clone https://github.com/marconi4000/cristo_exaltado.git  
5. Entre na pasta clonada:  
cd cristo_exaltado  

git clone https://github.com/marconi4000/cristo_exaltado.git nome-do-diretório    # Cria um clone de uma pasta e renomeia  
`git remote -v`                   # Como verificar os remotes existentes    
`git remote add origin <URL>`       # Conecta seu repositório local ao repositório remoto no GitHub (ou outro servidor Git), usando o nome `origin`.   

</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Salvando alterações no repositório local</summary>

       mkdir nome_da_pasta                   # Criar uma pasta simples  
       mkdir pasta1 pasta2 pasta3            # Criar múltiplas pastas de uma vez
       cd nome_da_pasta                      # Acessar a pasta criada
       git init                              # inicia o repositório local
       git status                            # mostrar o estado atual do seu repositório Git — ou seja, ele te diz:
                                             # Se há arquivos modificados (não comitados)
                                             # Quais arquivos estão na staging area (prontos para commit)
                                             # Quais arquivos não estão sendo rastreados pelo Git
                                             # Em qual branch você está
                                             # Se seu branch está à frente ou atrás do remoto
       touch README.md                       # Criando o arquivo RAEDME.md
       git status                            # O arquivo RAEDME.md é um (untracked file:) sugere `git add <file>` para incluir 
       git add README.md                     # adicionar o arquivo README.md à "staging area" do Git.
                                             # Essas mudanças ainda não estão no histórico do Git (isso só acontece com git commit)
        git commit -m "first commit"         # salvar (registrar) oficialmente as alterações que estão na staging area
        git log                              # exibir o histórico de commits do seu repositório Git — ou seja, ele mostra tudo o que já foi salvo com git commit, 
                                             # em ordem cronológica (do mais recente para o mais antigo).
       git status                            # A área de trabalho está limpa

</details>  

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Solução para salvar diretórios vazios</summary>

        mkdir minha-pasta-vazia
        touch minha-pasta-vazia/.gitkeep                        # Solução padrão: usar um arquivo .gitkeep
        git add minha-pasta-vazia/.gitkeep
        git commit -m "Mantém diretório vazio com .gitkeep"


</details> 
<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>Por que usar .gitignore?</summary>                   

O .gitignore é um arquivo de texto onde você escreve quais arquivos ou pastas o Git deve ignorar — ou seja, não rastrear, não adicionar e não fazer commit.                 
- Ele é essencial para evitar que você envie arquivos desnecessários, grandes ou sensíveis para o seu repositório.                 
Em um projeto real, você geralmente tem arquivos que não devem ir para o repositório, como:                 
- Arquivos temporários ou de cache                 
- Configurações locais (ex: senhas, chaves de API)                
- Dependências geradas automaticamente               
- Arquivos do seu editor (ex: .vscode/, .DS_Store no macOS)               
`touch .gitignore`       # criar se estiver usando Git Bash                   
Criar manualmente:                   
- Clique com o botão direito na pasta do projeto                  
- Vá em Novo > Documento de Texto                      
- Renomeie para .gitignore (sem extensão .txt!)                   
- Editar o .gitignore e adicionar os itens a ignorar                   
```                 
# Ignorar cache do Python             
__pycache__/             

# Ignorar logs temporários           
logs/           

# Ignorar configurações do VS Code              
.vscode/           

# Ignorar arquivos com senhas              
config.env               

# Ignorar arquivos de resultado automático            
resultado.txt            
```
- Verificar com git status                    
- Se o Git ainda estiver rastreando arquivos que deveriam ser ignorados.                   
- Isso acontece se você já adicionou esses arquivos antes de criar o .gitignore. Para corrigir:                  
- `git rm --cached config.env resultado.txt -r`                
- Depois: `git commit -m "Remove arquivos que agora estão no .gitignore"`               
- Agora, os arquivos ignorados não serão mais comitados                
- Você pode usar git add . e git commit -m "mensagem" tranquilamente — o Git só vai adicionar o que não está no .gitignore.

---

mkdir resumos
touch resumos/resumo-aula1.md
`echo resumos/ > .gitignore` # "ignore a pasta resumos/ e tudo que estiver nela"
  - Ele cria (ou sobrescreve) o arquivo .gitignore com o conteúdo: `texto/`
  - Ou seja, o Git vai ignorar a pasta chamada `texto/` (ou qualquer pasta com esse nome no projeto).
  - O Git vai ignorar tudo que estiver dentro da pasta texto/.
        > sobrescreve o arquivo - apagar tudo e deixar só texto/
        >> Se quiser adicionar a linha sem apagar o que já existe, use >> (duas setas): `echo texto/ >> .gitignore`

        mkdir texto
        echo texto/ > .gitignore        # cria (ou sobrescreve) o arquivo .gitignore com o conteúdo: `texto/`
                                        # o Git vai ignorar a pasta chamada texto/ (ou qualquer pasta com esse nome no projeto)
                                        # > sobrescreve o arquivo
        echo texto/ >> .gitignore       # >> adicionar a linha sem apagar o que já existe
        echo > .gitignore               # Se o arquivo .gitignore não existia, ele será criado vazio. 
                                        # Se o arquivo já existia, seu conteúdo será apagado e ele ficará completamente em branco
        cat .gitignore                  # checar o que tem no arquivo
                                          
</details> 
<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->


<details><summary>O que acontece quando você roda git init?</summary>  
Cria uma pasta oculta chamada .git dentro da pasta atual  
Essa pasta .git contém todos os dados e histórico de versões do repositório  
A partir daí, você pode usar comandos como git add, git commit, git branch, git status, etc.  
```
mkdir meu-projeto
cd meu-projeto
git init
```  
</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<details><summary>Flags comuns usadas com ls:</summary> 
        
Comando	O que faz
ls -l	                # Lista no formato "detalhado" (mostra permissões, dono, tamanho, data)
ls -a	                # Mostra todos os arquivos, incluindo os ocultos (que começam com .)
ls -la ou ls -al	# Combina as duas: lista tudo e mostra detalhes
ls -lh	                # Mostra tamanho de arquivos de forma legível (KB, MB, etc.)
ls nome-da-pasta	# Lista os arquivos dentro de uma pasta específica

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Resolvendo problema com duas contas do github no mesmo PC</summary> 

Configurar sua máquina para:   
- Usar Conta1 do GitHub com chave SSH   
- Garantir que o repositório remoto use a autenticação correta   
- Evitar conflitos com a Conta2   
      
💻 1. Verificar se você já tem chaves SSH   
- Abra o terminal e execute: `ls ~/.ssh`     
- Procure arquivos como: `id_rsa / id_rsa.pub`, `id_ed25519 / id_ed25519.pub` ou `id_ed25519_conta1`     
- Se já tiver uma chave usada pela Conta2, não se preocupe — vamos criar uma nova para a Conta1.        
     
🔐 2. Criar uma nova chave SSH para a Conta1
- No terminal:
- `ssh-keygen -t ed25519 -C "seu-email-da-conta1@exemplo.com" -f ~/.ssh/id_ed25519_conta1`
- Pressione Enter para aceitar o local sugerido
- Pode deixar a senha em branco ou colocar uma, se quiser mais segurança
- Isso vai criar dois arquivos:
- `~/.ssh/id_ed25519_conta1 (chave privada)`
- `~/.ssh/id_ed25519_conta1.pub (chave pública)`     
              
🧠 3. Adicionar a chave ao ssh-agent                
- No terminal:
- `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_ed25519_conta1`
            
🧷 4. Adicionar a chave pública no GitHub (Conta1)               
- Copie a chave pública:                
- `cat ~/.ssh/id_ed25519_conta1.pub`                    
- Vá para https://github.com/settings/keys                        
- Clique em "New SSH key"                      
- Cole a chave no campo, dê um nome (ex: Chave do meu PC) e clique em Add SSH Key              
                         
🛠️ 5. Configurar o arquivo SSH para múltiplas contas                    
- Edite ou crie o arquivo de configuração SSH:
- `ano ~/.ssh/config` se não funcioonar tente `nano ~/.ssh/config`
- Adicione este bloco ao final:
- Conta1 do GitHub                      
```                 
Host github-conta1                   
    HostName github.com                 
    User git                   
    IdentityFile ~/.ssh/id_ed25519_conta1              
```
- Salvar	CTRL + O → Enter     
- Sair	        CTRL + X     
- Importante: Esse "apelido" github-conta1 será usado para diferenciar da outra conta.
- Testar a conexão SSH com o GitHub da Conta1. Execute este comando no terminal:
- `ssh -T git@github-conta1`                           
- configure o repositório local para usar o remote com o host github-conta1, assim ele usa a chave certa:
- `git remote set-url origin git@github-conta1:conta1/nome-do-repo.git`
- Faça um commit e tente dar push para garantir que tudo está ok:
  - `git add .`
  - `git commit -m "Teste de push com Conta1 configurada"`
  - `git push origin main`
- Se apareceu isso:
  ```
  Apareceu isto: ! [rejected] main -> main (fetch first) error: failed to push some refs to 'github-conta1:conta1/repo.git' hint: Updates were rejected because the remote contains work that you do not hint: have locally. This is usually caused by another repository pushing to hint: the same ref. If you want to integrate the remote changes, use hint: 'git pull' before pushing again. hint: See the 'Note about fast-forwards' in 'git push --help' for details.
  ```
- Faça um pull para baixar e mesclar as mudanças do remoto: `git pull origin main --rebase`
- O --rebase vai aplicar suas mudanças por cima das que já estão no remoto, deixando o histórico mais limpo.
- Se der conflito, o Git vai avisar, e aí você resolve os conflitos nos arquivos e faz: `git add <arquivos-resolvidos>` e `git rebase --continue`
- Tente novamente a flag `git push origin main`                               

🌐 6. Clonar ou configurar o repositório com a Conta1                        
- Se for clonar um repositório da Conta1:                  
  - `git clone git@github-conta1:conta1/nome-do-repo.git`                            
- Perceba que usamos github-conta1 em vez de github.com no início.                        
- Se você já tem o repositório clonado, altere a URL remota:                                 
  - `cd nome-do-repo/`
  - `git remote set-url origin git@github-conta1:conta1/nome-do-repo.git`

👤 7. Configurar nome e e-mail da Conta1 (somente neste repositório)                                  
- `git config user.name "Seu Nome da Conta1"`                   
- `git config user.email "seu-email-da-conta1@exemplo.com"`                       
- Você pode confirmar com:                           
  - `git config --list`                      

✅ Agora você pode usar Git normalmente:             
- git add .            
- git commit -m "mensagem"             
- git push origin main (ou a branch correta)                   
- E tudo será feito com a Conta1, via a chave SSH correta.                         

</details>

<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Desfazendo alterações no repositório local</summary> 
        

        rm -rf <arquivo> ou <pasta>                 # apagar arquivos e pastas sem pedir confirmação
        git restore nome-do-arquivo                 # voltar para a versão anterior (do último commit)
        git restore .                               # Desfazer várias alterações de uma vez
        git restore --staged arquivo.txt            # Retirar arquivos da staging area (desfazer o git add)
        git commit --amend -m "Nova mensagem"       # editar o último commit feito no Git.
        git commit --amend                          # Corrigir a mensagem do commit anterior	
                                                    # Abre o editor para você escrever uma nova
                                                    # 📂 Adicionar arquivos esquecidos no commit anterior
                                                    # Junta os arquivos ao commit já feito
                                                    # 🧹 Corrigir um commit logo após tê-lo feito (sem criar um novo)	
                                                    # Substitui o commit anterior
        git reset --soft <hash-do-commit>           # Voltar o ponteiro do HEAD e da branch atual para um commit anterior, mantendo os arquivos no stage (index).
                                                    # Ele desfaz commits mais recentes, mas: Mantém suas alterações; Mantém os arquivos já preparados para commit (staged)
                                                
Exemplo prático:            
Imagine o seguinte histórico de commits:                  
`A - B - C - D  ← HEAD (main)`                  
Você quer voltar para o commit B, e "desfazer" C e D, mas não quer perder o conteúdo dessas mudanças.                    
Você roda:                                 
`git reset --soft <hash-do-commit-B>`                 
O que acontece:               
O ponteiro HEAD volta para B              
Os commits C e D saem do histórico                                         
As mudanças de C e D ficam como se estivessem prontas para commit (staged)                     
🎯 Quando usar --soft?                         
- Quando você quer reescrever os últimos commits                       
- Quando comitou antes da hora                                                     
- Quando quer juntar vários commits em um só (com git commit --amend depois)

        git log                                     # lista de todos os commits
        git reset --mixed <hash-do-commit>          # é usado para voltar o seu repositório local para um commit anterior,
                                                    # removendo os commits mais recentes, sem apagar os arquivos modificados.
                                                    # Move o ponteiro da branch (HEAD) para o commit indicado
                                                    # Remove os commits posteriores
                                                    # Mantém as alterações feitas nos arquivos, mas retira elas da staging area
                                                    # Desfazer os commits, mas continuar com as alterações nos arquivos, só que ainda não prontas para commit.

Exemplo prático:
Imagine o seguinte histórico de commits:
A -- B -- C -- D  ← HEAD (main)
Se você rodar:
`git reset --mixed B`
O que acontece:
O ponteiro HEAD volta para o commit B
Os commits C e D são removidos do histórico local
As alterações feitas em C e D:
Permanecem nos arquivos
Estão fora da staging area (como se você tivesse editado os arquivos, mas não dado git add)
🎯 Quando usar git reset --mixed?
- Quando você cometeu várias mudanças, mas quer reorganizar os commits
- Quando cometeu algo errado e quer refazer o commit, mantendo as alterações
- Quando quer "descomitar", mas não perder os arquivos modificados


                git reflog                        # ver todo o histórico de movimentações do HEAD — ou seja,
                                                  # acompanhar tudo que aconteceu no seu repositório local, incluindo commits, resets, merges, checkouts, etc.

Recuperar commits perdidos
Você cometeu um erro com `git reset --hard`, `git checkout`, ou deletou uma branch?
Use `git reflog` para ver os commits anteriores e voltar para eles.

        `git restore --staged diretorio/arquivo.md`        # remover um arquivo da staging area (index) — ou seja, desfazer um git add.
                                                           # tirar um arquivo da preparação para commit, mas sem apagar as alterações que você fez nele.
                                                           
|Tipo de Reset	|Histórico (HEAD)	|Staging Area (Index)	|Arquivos no disco (Working Directory)|
|:---:|:---:|:---:|:---:|
|--soft	|✅ Altera|	✅ Mantém|	✅ Mantém|
|--mixed (padrão)|	✅ Altera|	❌ Limpa|	✅ Mantém|
|--hard	|✅ Altera|	❌ Limpa|	❌ Apaga (volta ao último commit)|


</details>


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Usando o Editor Online do GitHub (Atalho .)</summary> 
            
📌 O que é o Editor Online do GitHub?

> O GitHub oferece uma versão baseada na web do Visual Studio Code (VS Code), chamada de GitHub.dev. Ele permite editar qualquer repositório diretamente no navegador, sem precisar clonar localmente.

Você pode acessá-lo de duas formas:

 - Pressionando . em qualquer repositório aberto no GitHub.
- Digitando manualmente github.dev no lugar de github.com na URL.

🚀 Como Abrir o Editor            
✅ Método 1: Atalho com .
- Acesse qualquer repositório no GitHub (por exemplo: https://github.com/usuario/repositorio).
- Com o repositório aberto, pressione a tecla . (ponto) no seu teclado.
- O navegador abrirá automaticamente o editor online no endereço:
https://github.dev/usuario/repositorio.

✅ Método 2: Alterando a URL
- Pegue a URL do repositório (ex: https://github.com/usuario/repositorio).
- Substitua github.com por github.dev:
https://github.dev/usuario/repositorio.

🧠 O Que Você Pode Fazer no Editor  
✅ Navegar pelos arquivos do repositório.  
✅ Editar arquivos de código, Markdown, JSON, YAML, etc.  
✅ Commitar alterações diretamente para a branch atual.  
✅ Criar novas branches.  
✅ Criar pull requests.  
✅ Visualizar histórico de commits.  
✅ Usar atalhos e extensões compatíveis com o VS Code (limitado).  

|⚙️ Funcionalidade	|Disponível |
|:-----:|:-----:| 
|Edição de arquivos	|✅ Sim| 
|Interface do VS Code	|✅ Sim|
|Terminal integrado	|❌ Não|
|Execução de código	|❌ Não|
|Git integrado	        |✅ Sim|  
|Extensões	        |⚠️ Limitado|  
|Preview de Markdown	|✅ Sim|  

⚠️ Não é possível rodar código ou abrir um terminal, pois ele roda apenas no navegador, sem backend.

📤 Como Salvar e Committar Alterações
- Após editar um arquivo, ele aparecerá com um círculo azul indicando mudanças.
- Clique no ícone de source control (ícone de ramificação à esquerda).
- Escreva uma mensagem de commit.
- Clique em "Commit" para salvar.
- Se quiser, use “Push” para enviar para o repositório (se tiver permissão).

🛠️ Dicas Úteis
- Use Ctrl + P para buscar rapidamente arquivos.
- Use Ctrl + Shift + E para alternar para o explorador de arquivos.
- Use Ctrl + Shift + P para abrir a paleta de comandos.

Para contribuições rápidas em projetos open source, é uma alternativa prática ao VS Code instalado localmente.

🧑‍💻 Quando Usar
- Corrigir erros rápidos em projetos.
- Fazer revisões de pull requests.
- Contribuir com projetos open source sem clonar.
- Escrever documentação diretamente no GitHub.

</details>  


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Como Usar git pull e git push</summary>  

> `git init`  
> `git add .`  
> `git commit -m "first commit"`  
> `git branch -M main`  
> `git remote add origin https://github.com/seu-usuario/NomeDoProjeto.git`  
> `git push -u origin main`
##### OU   
> `git pull origin main`  

🔄 Entendendo git pull e git push  
| Comando | Para que serve |  
|:-----:|:-----:|   
| git pull | Atualiza seu repositório local com mudanças do remoto |     
| git push | Envia suas alterações locais para o repositório remoto |  

🛠️ Pré-requisitos  
> - Antes de usar git pull e git push, é preciso:
> - Ter o Git instalado (site oficial).    
> - Ter um repositório remoto configurado (ex: no GitHub).  
> - Ter feito o git clone do repositório (ou já estar trabalhando em um).  
> - Estar logado/autenticado se o repositório exigir (via HTTPS ou SSH).  

✅ Etapa 1: Clonar um repositório (se ainda não tiver feito)  
> `git clone https://github.com/usuario/repositorio.git`  
`cd repositorio`  
> Isso cria uma cópia local do repositório remoto.  

✅ Etapa 2: Fazer mudanças e commit (simulação)  
Suponha que você editou um arquivo ou criou um novo:
> `touch exemplo.txt`  
`echo "Olá, Git!" > exemplo.txt`  
`git add exemplo.txt`  
`git commit -m "Adiciona o arquivo exemplo.txt"`  

Agora você tem mudanças committadas localmente, prontas para serem enviadas.  
📤 git push: Enviando mudanças para o repositório remoto

🔎 O que faz?  
> Envia seus commits locais para o repositório remoto (ex: GitHub).

▶️ Comando:  
> `git push origin nome-da-branch`  

Exemplo:  
> `git push origin main`  

💡 Dica:  
> - Se for a primeira vez empurrando uma branch nova:
> - `git push -u origin minha-nova-branch`
> - O -u faz com que a próxima vez você possa usar apenas git push.

📥 git pull: Atualizando seu repositório com as mudanças do remoto  
🔎 O que faz?
> - Baixa novas alterações do repositório remoto
> - Integra essas mudanças na sua branch atual

▶️ Comando:  
> - `git pull origin nome-da-branch`

Exemplo: 
> - `git pull origin main`

Esse comando é equivalente a:  
> - `git fetch origin`
> - `git merge origin/main`

🔄 Quando usar?  
> - Antes de começar a programar: para garantir que você está com a versão mais atualizada.
> - Antes de dar push: para evitar conflitos.

🧩 Conflitos de Merge
> - Se ao dar git pull aparecerem conflitos, o Git vai informar quais arquivos precisam ser resolvidos. Você deve:  
> - Abrir os arquivos indicados.  
> - Resolver os conflitos manualmente (removendo marcações do Git).  

Salvar os arquivos.
> - Fazer um commit:
> - `git add arquivo-com-conflito`
> - `git commit -m "Resolve conflito"`

🔄 Exemplo Completo do Fluxo    
1. Clonar o projeto (uma vez só)  
> - `git clone https://github.com/usuario/repositorio.git`
> - `cd repositorio`

2. Criar nova branch (opcional)  
> - `git checkout -b nova-feature`

3. Fazer alterações  
> - `echo "Algo novo" > novo-arquivo.txt`  
> - `git add novo-arquivo.txt`  
> - `git commit -m "Adiciona novo-arquivo.txt"` 

4. Atualizar o repositório local antes de enviar (boa prática)
> - `git pull origin main`

5. Enviar alterações
> - `git push origin nova-feature`

🛑 Erros comuns  
|Erro |	Causa provável	| Solução  |
|:-----:|:-----:|:-----:|
| `rejected non-fast-forward` | Seu repositório está desatualizado | Use `git pull antes de dar push` |  
| `authentication failed` | Credenciais erradas ou token expirado | Atualize suas credenciais/token do GitHub |
| `merge conflict` | Alterações conflitantes | Resolva os conflitos manualmente |

📚 Resumo  

| Ação | Comando |  
|:-----:|:-----:|
| Atualizar com mudanças do repositório remoto | `git pull origin nome-da-branch` |  
| Enviar alterações locais para o remoto | `git push origin nome-da-branch`|

> `git init`  
> `git add .`  
> `git commit -m "first commit"`  
> `git branch -M main`  
> `git remote add origin https://github.com/seu-usuario/NomeDoProjeto.git`  
> `git push -u origin main`
##### OU   
> `git pull origin main`  

</details>  


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  

<details><summary>Comandos Git via Terminal Integrado</summary>  

Como visualizar HTML como página web no GitHub usando GitHub Pages
1. O que é o GitHub Pages?

O GitHub Pages é um serviço gratuito do GitHub que transforma seu repositório em um site estático.

Ele é usado para hospedar sites pessoais, projetos, documentação, blogs etc — tudo diretamente do seu repositório.

2. Passo a passo para ativar e visualizar seu HTML
Passo 1: Tenha seu arquivo HTML no repositório

Certifique-se de que seu arquivo .html esteja no repositório — geralmente na raiz (/) ou na pasta docs/.

Exemplo: index.html

Passo 2: Acesse as configurações do seu repositório

No GitHub, vá até o seu repositório.

Clique na aba Settings (Configurações).

Passo 3: Configure o GitHub Pages

No menu lateral, clique em Pages (geralmente na seção “Code and automation”).

Na seção “Source” (Fonte), selecione a branch onde está seu arquivo HTML (normalmente main ou master).

Escolha a pasta onde está o arquivo (root / ou /docs).

Clique em Save.

Passo 4: Acesse o link do seu site

Após alguns segundos (pode levar alguns minutos para publicar), o GitHub mostrará o endereço do seu site, algo como:

https://seu-usuario.github.io/nome-do-repositorio/


Acesse esse link no navegador e verá seu arquivo HTML renderizado como página web.

3. Dicas extras

O arquivo principal do seu site precisa ser index.html na raiz ou na pasta selecionada para que seja carregado automaticamente.

Você pode adicionar CSS, JavaScript e outras páginas HTML, e navegar entre elas usando links relativos.

Atualize o repositório com commits e o site será atualizado automaticamente.

4. Exemplo prático

Suponha que você tenha um repositório chamado meu-site com o arquivo index.html na raiz.

Depois de configurar o GitHub Pages apontando para a branch main e pasta /, o site ficará disponível em:

https://seu-usuario.github.io/meu-site/


</details>  


parei aqui


<details><summary>Comandos Git via Terminal Integrado</summary>  

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

</details>  


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  


<details><summary>COMANDOS</summary>  


        mkdir nome_do_diretorio                # Criar um diretório simples
        mkdir -p pasta/filho1/filho2           # Criar diretórios aninhados de uma só vez

        touch nome_do_arquivo.ext                   # cria um arquivo vazio ou atualiza a data de modificação se ele já existir.
        touch arquivo1.txt arquivo2.js imagem.png   # Criar múltiplos arquivos simultaneamente
        echo "Texto inicial" > arquivo.txt          # Criar e adicionar conteúdo no mesmo comando
        nano arquivo.txt                            # Criar e começar a editar imediatamente com o editor padrão
        OU
        vi arquivo.txt

        git log	Ver todos os commits com detalhes
        git log --oneline	                    # Ver uma lista resumida
        git log --stat	                            # Ver quais arquivos mudaram em cada commit
        git log --graph --oneline --all	            # Ver o histórico em forma de árvore
        

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


</details>  


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  


<details><summary>Esses atalhos facilitam a edição de linha, movimentação e histórico de comandos:</summary>  

                
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


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  


<details><summary>Atalhos do teclado</summary> 

        Negrito	                                Ctrl + B	
        Itálico	                                Ctrl + I	
        Riscado	                                Alt + Shift + 5	
        Código em linha	                        Ctrl + E	
        Bloco de código	                        Ctrl + Shift + E	
        Lista ordenada	                        Ctrl + Shift + 7	
        Lista com marcadores	                Ctrl + Shift + 8	
        Citação (>)	                        Ctrl + Shift + 9	
        Link [texto](url)	                Ctrl + K	
        Visualizar Markdown (Preview tab)	Ctrl + Shift + P	

</details>  


<!-- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -->  


<details><summary>Setas e Símbolos Diversos</summary> 

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

</details>  
