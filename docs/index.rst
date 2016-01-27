.. Piramid documentation master file, created by
   sphinx-quickstart on Tue Jan 26 13:22:33 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentação da aplicação de teste: pyramid!
===================================

==================================
Estrutura de arquivos e diretórios
==================================


 *__init__.py* -- Configuração inicial. 


 *models.py* -- Camada de acesso á dados. 

 
 *scripts* -- Onde se localizam os scripts de atualização ou manutenção da aplicação. 

 
 *static*-- Onde ficam os arquivos estáticos. 

 
 *templates* -- Arquivos de visualização. 

 
 *tests.py* -- Testes automatizados.  


 *views.py* -- Camada de negócio da aplicação.

=========
Instalação
=========

Tal configuração é para ser feito no terminal de uma máquina linux. A máquina em uso é Centos versão 7. Caso utilize outro tipo de sistema operacional, é necessário rever a síntaxe adotada.


1. yum install sqlite-devel git

2. virtualenv egito

3. pip install "pyramid==1.6"

4. bin/pcreate -s alchemy  tutorial

5. rm -rf tutorial/*

6. git clone https://github.com/wagnerwar/piramid.git tutorial

7. cd tutorial/

8. python setup.py develop

9. cd ../

10. bin/initialize_tutorial_db tutorial/development.ini


===============
Modelo de dados
==============

Arquivo models.py

.. code-block:: python
    :linenos:

    class Video(Base):
        __tablename__ = 'video'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        descricao = Column(Text)
        preco = Column(Float)

    Index('my_index', Video.name, unique=True, mysql_length=255)
				
Sincronização e criação das tabelas
    bin/initialize_tutorial_db tutorial/development.ini -- Onde tutorial/development.ini é o arquivo de configuração
				
Como visto acima, a classe Video representa a tabela video, com os seguintes atributos: id,name,descricao e preco.
O framework SqlAlchemy  permite que, não manipulemos dados diretamente, mas, objetos, que representam estes dados. Por isso,
não precisa conhecer a estrutura dos dados, apenas, saber usar a camada de abstração destes dados. Os mesmos dados  podem estar no SQLite ou no POSTGRESQL; não importa, a forma de manipulá-los é a mesma. 
Foi criado um índice chamada my_index associado com a tabela video.
			
========
Cadastro
========

Arquivo __init__.py

.. code-block:: python
    :linenos:

    def main(global_config, **settings):
        config.include(videos_include, route_prefix='/videos')
					
    def videos_include(config):
        config.add_route('cadastrar', '/cadastrar')

Conforme visto acima, estão configuradas todos os caminhos iniciados com 'videos/' dentro da função videos_include.
Por exemplo, quando digitamos 'videos/cadastrar', será carregada a view cadastrar, cujo conteúdo segue abaixo, no arquivo views.py.


Arquivo views.py

.. code-block:: python
    :linenos:

    @view_config(route_name='cadastrar',renderer='templates/cad.pt')
    def cadastrar(request):
        save_url = request.route_url('cadastrar')
        request.route_url('consulta')
        if  request.params:
            print('PASSOU')
            nome = request.params['nome']
            descricao = request.params['descricao']
            preco = request.params['preco']
            novo_video = Video(name=nome,descricao=descricao,preco=preco)
            try:
                DBSession.add(novo_video)
                return HTTPFound(location=request.route_url('consulta'))
            except DBAPIError:
            return Response("ERRO DB")
        else:
            print('NAO PASSOU')
            return {'save_url': save_url,'project': 'tutorial'}

Conforme visto acima, a view denominada 'cadastrar' renderiza o template 'templates/cad.pt'. A função cadastrar trata das requisições e respostas desta URI (Entende-se como caminho de uma URL, por exemplo: http://localhost/videos/cadastrar ) 
Observe que, se existem parâmetros na requisição, o sistema tenta cadastrar um video novo. Se não há parâmetros, simplesmente exibe o formulário para inclusão de um novo vídeo.



Arquivo de template: templates/cad.pt (Trecho relevante )

.. code-block:: html
    :linenos:

    <div class="content">
    <h1><span class="font-semi-bold">Cadastro de vídeos</span></h1>
    <form action="${save_url}" method="GET">
    <label>Nome:<br>
    <input type="text" name="nome" value="" /><br>
    </label>
    <label>Descricao:<br>
    <input type="text" name="descricao" value="" /><br>
    </label>
    <label>Preco:<br>
    <input type="text" name="preco" value="" /><br>
    </label>
    <label>
    <input type="submit" value="Cadastrar" style="margin-top: 1.2em;">
    </label>
    </form>
    </div>

No meio de um grande código HTML, entre tags HTML e BODY, depois da tag HEAD, segue acima o que realmente nos interessa.
			
URL: http://192.168.56.101:6543/videos/cadastrar



========
Consulta
========

Arquivo __init__.py

.. code-block:: python
    :linenos:

    def videos_include(config):
        config.add_route('consulta', '/')


Agora, no trecho acima, foi configurada nova rota. Ou seja, quando digitarmos na barra de endereço "videos/", seremos redirecionados para a view 'consulta'. A configuração desta view segue abaixo:


Arquivo views.py

.. code-block:: python
    :linenos:

    @view_config(route_name='consulta',renderer='templates/consulta.pt')
        def consulta(request):
            videos = DBSession.query(Video).all()
            url_edit = request.route_url('edicao')
            url_cad = request.route_url('cadastrar')
            return {'videos': videos,'url_edit': url_edit,'url_cad': url_cad}

Conforme código acima, eu busco todos os registros da tabela video, para exibi-los numa listagem.	


Arquivo de template: 'templates/consulta.pt' (Trecho relevante)

.. code-block:: html
    :linenos:

    <div class="content">
    <h1>Listagem de vídeos</h1>
    <a tal:attributes="href string:${url_cad}"><button>CADASTRAR</button></a>
    <div tal:repeat="item videos">
    <div class="vido">
    <a tal:attributes="href string:${url_edit}?&id=${item.id} "><strong>Nome: </strong><span tal:content="string:${item.name}" /></a><br />
    <strong>Descricao: </strong><span tal:content="string:${item.descricao}" /><br />
    <strong>Preco: </strong><span tal:content="string:${item.preco}" /><br />
    </div>
    </div>
    </div>
    </div>


Acima, a listagem de vídeos.


======
Edição
======

========
Exclusão
========

===========
Referências
===========

