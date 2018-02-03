Title: Tutorial da linguagem de marcação Markdown
Date: 2016-11-17 01:30
Category: Blog
Tags: pug-pb, blog, tutorial, markdown
Slug: tutorial-markdown
Authors: Hildeberto Abreu
Summary: Principais elementos da sintaxe da linguagem de marcação Markdown, a ser utilizada neste blog.


Principais elementos da sintaxe Markdown
========================================

Fonte: http://daringfireball.net/projects/markdown/syntax

Excertos e tradução: @hilam

### ELEMENTOS DE BLOCO

#### PARÁGRAFOS E QUEBRAS DE LINHA

Um parágrafo é simplesmente uma ou mais linhas consecutivas de texto, separadas
por uma ou mais linhas em branco. (Uma linha em branco é qualquer uma que pareça
com uma linha em branco - uma linha contendo apenas espaços em branco ou tabulações
é considerada em branco.) Parágrafos não devem ser identados com espaços ou tabulações.

#### CABEÇALHOS


    Isto é um H1
    ============

    Isto é um H2
    ------------

produz:

Isto é um H1
============

Isto é um H2
------------

Qualquer número de =’s ou -’s funcionará.

Outra forma:

    # Isto é um H1

    ## Isto é um H2

    ###### Isto é um H6

# Isto é um H1

## Isto é um H2

###### Isto é um H6


#### CITAÇÕES

Markdown usa o caractere >, como no estilo email, para citações. Se você costuma
citar passagens de emails, então você saberá criar uma citação em Markdown. Ele
fica melhor se você distribui o texto e põe o caractere > antes de cada linha:

    > Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
    > consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    > Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
    >
    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    > id sem consectetuer libero luctus adipiscing.

> Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

É possível colocar o > apenas no início da primeira linha do parágrafo citado:

    > Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    id sem consectetuer libero luctus adipiscing.

> Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

Citações podem ser aninhadas (por ex.: uma citação dentro da citação) adicionando
o caractere > para dicionar níveis:

    > Primeiro nível da citação.
    >
    > > Citação aninhada, num segundo nível.
    >
    > De volta ao primeiro nível da citação.

> Primeiro nível da citação.
>
> > Citação aninhada, num segundo nível.
>
> De volta ao primeiro nível da citação.

Citações podem conter outros elementos Markdown elements, incluindo cabeçalhos,
 listas, e blocos de código:

    > ## Cabeçalho H2
    >
    > 1.   Primeiro item da lista.
    > 2.   Segundo item.
    >
    > Um exemplo com código:
    >
    >     return shell_exec("echo $input | $markdown_script");

> ## Cabeçalho H2
>
> 1.   Primeiro item da lista.
> 2.   Segundo item.
>
> Um exemplo com código:
>
>     return shell_exec("echo $input | $markdown_script");


#### LISTAS

Markdown suporta listas ordenadas (numeradas) e não ordenadas (bullet).

Listas não ordenadas usam *, + e - (não misturados):

    *   Red
    *   Green
    *   Blue

equivalente a:

    +   Red
    +   Green
    +   Blue

e:

    -   Red
    -   Green
    -   Blue

todos produzem:

*   Red
*   Green
*   Blue

Listas ordenadas usam números seguidos de ponto(.):

    1.  Bird
    2.  McHale
    3.  Parish

1.  Bird
2.  McHale
3.  Parish

Outros exemplos:

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
        viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
        Suspendisse id sem consectetuer libero luctus adipiscing.

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

Mas se você for preguiçoso, não precisa:

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.

Os itens da lista podem consistir de vários parágrafos. Cada parágrafo
subsequente no item da lista deve ser identado por 4 espaços ou tabulação:

    1.  Um item de lista com dois parágrafos. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit. Aliquam hendrerit
        mi posuere lectus.

        Vestibulum enim wisi, viverra nec, fringilla in, laoreet
        vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
        sit amet velit.

    2.  Suspendisse id sem consectetuer libero luctus adipiscing.

1.  Um item de lista com dois parágrafos. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

        *   Item de lista com dois parágrafos.

            Segundo parágrafo do item. Só
        é necessário identar a primeira linha. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit.

        *   Outro item da lista.

*   Item de lista com dois parágrafos.

    Segundo parágrafo do item. Só
é necessário identar a primeira linha. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Outro item da lista.

É possível indicar uma lista ordenada por acidente, escrevendo algo como isso:

    1986. Que grande temporada.

1986. Que grande temporada.

Em outras palavras, uma sequência número-ponto-espaço no começo de uma linha.
Para evitar isso, você pode "escapar" o ponto(.) com a barra invertida:

    1986\. Que grande temporada.

1986\. Que grande temporada.


#### BLOCOS DE CÓDIGO

Para produzir um bloco de código, simplesmente idente cada linha do bloco com,
pelo menos, 4 espaços ou 1 tabulação:

    Parágrafo normal.

        Bloco de código.

Markdown vai gerar:

Parágrafo normal.

    Bloco de código.

Exemplo com Python:

    def teste():
        return "Hello PUG!"

    teste()

Um bloco de código continua até atingir uma linha que não está identada.


    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

Sintaxe regular do Markdown não é processada dentro de blocos de código.


#### RÉGUAS HORIZONTAIS (HR)

É possível produzir uma régua horizontal colocando três ou mais hífens,
asteriscos ou sublinhados numa linha.

    * * *

    ***

    *****

    - - -

    ---------------------------------------

* * *

***

*****

- - -

---------------------------------------


#### LINKS

Markdown suporta dois estilos de links: inline e reference.

Em ambos, o texto do link é delimitado por [colchetes].

Para criar um link "inline", use um conjunto de parêntesis imediatamente após
o colchete que finaliza o texto do link. Dentro dos parêntesis, coloque a URL,
com um título opcional para o link, esntre aspas. Por exemplo:

    Este é [um exemplo](http://example.com/ "Título") de link inline.

    [Este link](http://example.net/) não tem o atributo título.

Este é [um exemplo](http://example.com/ "Título") de link inline.

[Este link](http://example.net/) não tem o atributo título.

Podem ser usados caminhos relativos:

    Veja minha página [Sobre](/about/) para detalhes.

Veja minha página [Sobre](/about/) para detalhes.

Links estilo "reference" usam um segundo conjunto de colchetes, dentro dos quais
colocamos um "label" de nossa escolha para identificar o link:

    Isto é [um exemplo][id] de link estilo "reference".

Isto é [um exemplo][id] de link estilo "reference".

Pode-se, opcionalmente, usar um espaço para separar os conjuntos de colchetes:

    Este é [um exemplo] [id] de link estilo "reference".

Este é [um exemplo] [id] de link estilo "reference".

Então, em qualquer lugar do documento, você define o "label" do seu link assim:

    [id]: http://example.com/  "Título Opcional aqui"

[id]: http://example.com/  "Título Opcional aqui"


#### ÊNFASE

Asteriscos (*) e sublinhados (_) são indicadores de ênfase.

    *um asterisco*

    _um sublinhado_

    **dois asteriscos**

    __dois sublinhados__

produzirão:

*um asterisco*

_um sublinhado_

**dois asteriscos**

__dois sublinhados__


#### CÓDIGO

Par indicar um trecho de código use (`). Pode inserir código num parágrfo normal.

    Use the `printf()` function.

produzirá:

Use the `printf()` function.


#### IMAGENS

Markdown usa para imagesn uma sintaxe parecida com a de links:

Imagens com sintaxe "inline" são assim:

    ![Alt text](/path/to/img.jpg)

    ![Alt text](/path/to/img.jpg "Optional title")

![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")


    ![Alt text][id]

    [id]: url/to/image  "Optional title attribute"

![Alt text][id]

[id]: url/to/image  "Optional title attribute"


#### LINKS AUTOMÁTICOS


    <http://example.com/>

<http://example.com/>


    <address@example.com>

<address@example.com>


#### CARACTERE DE ESCAPE

Markdown permite usar a contra-barra para gerar caracteres literais:

    \*literal asterisks\*

\*literal asterisks\*

Use a contra-barra se quiser colocar algum desses caracteres no texto:

    \\
    \`
    \*
    \_
    \{\}
    \[\]
    \(\)
    \#
    \+
    \-
    \.
    \!

\\
\`
\*
\_
\{\}
\[\]
\(\)
\#
\+
\-
\.
\!
