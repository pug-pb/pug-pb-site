Title: Como Publicar Neste Blog
Date: 2018-11-30 10:00
Category: Blog
Tags: pug-pb, blog, publicar, tutorial, pelican,
Slug: como-publicar
Authors: Hildeberto
Summary: Veja como é fácil contribuir com conteúdo para nosso Blog
image: /images/icons8-ouch-marginalia-coming-soon.png

Este blog é aberto à colaboração e qualquer membro da comunidade pode produzir conteúdo e enviar para que seja publicado aqui. Uma vez que o material não viole o [Código de Conduta da Comunidade](/blog/cdc), a solicitação será processada por um dos membros da equipe do GitHub. Mostraremos a seguir como proceder para ter seu conteúdo publicado aqui.

### O Que é o Pelican

Veremos um tutorial para aqueles que desconhecem o [Pelican](https://docs.getpelican.com/en/stable/). Mostraremos como criar o **virtual env**, instalação das dependẽncias, criação do conteúdo, teste local e envio das modificações ao GitHub.

O Pelican é um gerador de site estático multiplataforma (GNU/Linux, Mac OS e Windows), facilitando a publicação através do [GitHub Pages](https://pages.github.com/). Um site estático não precisa de nenhum servidor de aplicação (*backend*) em execução. Ele é composto apenas de arquivos HTML, CSS e JavaScript. Todo o código é gerado pelo Pelican. Ganhamos em performance, hospedagem, segurança e versionamento.

Como este site receberá publicações de várias pessoas, resolvemos usar as *Pull Requests* do GitHub para controlar os artigos que serão publicados. Desta forma não limitamos as publicações apenas a quem tem permissão no repositório e/ou é membro do PUG-PB. Qualquer pessoa com uma conta no GitHub poderá solicitar um *Pull Request* e ter seu conteúdo publicado.

### Obtendo Uma Cópia dos Fontes do Site

Para obter uma cópia dos fontes do site você vai precisar do Git na sua máquina e de uma conta no [GitHub](https://github.com/). Primeiramente acesse o [repositório do site](https://github.com/pug-pb/pug-pb-site) e crie um fork para o seu usuário. Uma vez criado o fork, clone o site em um diretório qualquer da sua máquina (no exemplo está na raiz do usuário):

``` bash

    cd ~
    git clone https://github.com/<troque_pelo_nome_do_seu_usuario>/pug-pb-site.git
    cd pug-pb-site

```

O repositório é composto de alguns diretórios principais:

``` bash

    pug-pb-site
    │
    ├── content
    │   ├── articles
    │   ├── images
    │   └── pages
    ├── .plugins
    └── themes

```

O diretório ``content`` possui todos os conteúdos, como artigos, imagens, pdfs e páginas, o ``.plugins`` contém todos os *plugins* do Pelican, e o diretório ``themes`` possui o tema que utilizamos no site. Vamos nos focar apenas no diretório ``content``.

Agora temos que preparar o ambiente.

### Preparando o Ambiente

Criar o ambiente de uso do Pelican é muito simples, pra isso você vai precisar de:

- Python 3.6 ou superior;
- Conexão de internet;
- Um terminal;
- Um editor de texto, preferencialmente com suporte a Markdown;
- Um navegador;

Este tutorial é direcionado para o shell Linux. Se você utiliza Windows, os comandos são os mesmos, mas a indicação de diretórios é feita com a barra invertida (\).

Uma vez clonado o repositório do site, abra um terminal e crie um *ambiente virtual* para o Python 3 (note que este passo não é obrigatório, mas é uma boa prática):

``` bash

    cd ~/pug-pb-site
    python3 -m venv pugpb_venv
```

Você pode chamar seu *ambiente virtual* com qualquer nome que queira, e colocar em qualquer outra pasta. Uma vez criado este *ambiente virtual*, ative-o:

``` bash

    source ~/pug-pb-site/pugpb_venv/bin/activate
```

Uma vez ativado o *ambiente virtual* basta instalar todas as dependências. Para isso utilize o seguinte comando:

``` bash

    pip install -r requirements.txt
```

Após instaladas todas as dependências, faça a geração de teste do site, com o comando ``make html``. É criado um diretório ``output``, com o conteúdo gerado. Este diretório já está no ``.gitignore`` e não deverá entrar no seu *commit*. Para visualizar o site **localmente** rode o comando ``make serve`` (sua linha de comando ficará "presa" pois ela está servindo as páginas neste momento) e acesse a URL <http://localhost:8000>. Para sair do "modo servidor" pressione ``Ctrl+C`` e a linha de comando retornará ao normal.

Após algum tempo de uso, é costume sempre executar uma cadeia de comandos para evitar que arquivos de compilações prévias interfiram com a visualização atual: ``make clean html serve``. Apenas esta linha de comando limpa o conteúdo do diretório ``output``, gera o site novamente, e entra no modo servidor. Novamente, para sair do *modo servidor* pressione ``Ctrl+C``.

Note que todos estes comandos devem ser executados na raiz do repositório, onde se encontra o arquivo de "receitas" do make, isto é, o arquivo ``Makefile``. Se você estiver usando Windows, em que não há o comando `make`,  os comandos equivalentes seriam:

1) make clean: `del output`
2) make html: `pelican`
3) make serve: `pelican -l`

### Escrevendo Seus Próprios Artigos

Para escrever seus próprios artigos, a maneira mais simples é copiar o arquivo `content/articles/padrao-artigo.md` para a mesma pasta, abrir o novo arquivo criado e digitar seu artigo. Sugiro olhar o [tutorial](blog/tutorial) da linguagem de marcação Markdown, utilizada para produzir as páginas HTML. Também é possível olhar exemplos dos artigos já publicados, no diretório `contents/articles`. Um artigo tem um cabeçalho fixo, conforme abaixo:

``` markdown

    Title: Como Publicar No Blog
    Date: 2015-07-22 14:57
    Author: Guido
    Category: Blog
    Tags: tutorial, tecnico, pelican, site
    image: /images/monty-python-knights.jpg
```

Coloque o título do seu artigo, seguido da data de publicação (no formato ``YYYY-MM-DD HH:MM``). Logo abaixo temos o nome do autor, categoria e uma lista de tags. A palavra-chave `image` faz referência à imagem de capa do artigo, que também fica no "cabeçalho" do artigo. A imagem deve ser colocada na pasta `content/images`.

Após este cabeçalho fixo, basta escrever o texto de acordo com a linguagem de marcação. Uma vez concluído o artigo, teste a compilação novamente com o comando `make clean html serve` e acesse a URL <http://localhost:8000/blog/index.html> para ver como ficou. Os artigos mais recentes aparecem no início do blog.

### Enviando Sua Contribuição

Uma vez concluído o artigo, vamos realizar o *commit* da alteração:

``` bash

    git add content/article/<substitua-pelo-nome-do-seu-artigo.md>
    git add content/images/<substitua-pelo-nome-da-sua-imagem-do-artigo.png>
    git commit -m "Adicionado novo artivo '<substitua pelo nome descritivo do seu artigo>'"
```

Com o *commit* realizado com sucesso, você pode realizar o push pro seu repositório remoto (GitHub):

``` bash

    git push origin master
```

Agora basta enviar um *Pull Request* do seu repositório, através da interface do GitHub, e os gestores do site irão aprovar sua contribuição.

A fonte da **Ilustração** utilizada: <icons8.com>
