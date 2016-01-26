from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Video,
    )


@view_config(route_name='exclusao')
def excluir(request):
    if request.params:
        try:
            id=request.params['id']
            DBSession.delete(DBSession.query(Video).filter_by(id=id).first())
            return HTTPFound(location=request.route_url('consulta'))
        except Exception:
            return Response("ID INVALIDO")
    else:
        return Response("KD O ID?")

@view_config(route_name='edicao',renderer='templates/edicao.pt')
def editar(request):
    save_url = request.route_url('edicao')
    dell = request.route_url('exclusao')
    id = request.params['id']
    video = DBSession.query(Video).filter_by(id=id).one()
    if 'nome' in request.params.keys():
        try:
            print("PASSOU")
            nome = request.params['nome']
            descricao=request.params['descricao']
            preco=request.params['preco']
            
            dados = DBSession.query(Video).filter_by(id=id).update({'name': nome,'descricao': descricao,'preco': preco})
            return HTTPFound(location=request.route_url('consulta')) 
        except Exception:
            return Response('ERRO DB')
        
    else:
        print("nao passou")
    return {'save_url': save_url,'video': video,'dell': dell}

@view_config(route_name='consulta',renderer='templates/consulta.pt')
def consulta(request):
    videos = DBSession.query(Video).all()
    url_edit = request.route_url('edicao')
    url_cad = request.route_url('cadastrar')
    return {'videos': videos,'url_edit': url_edit,'url_cad': url_cad}
   
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
 

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(Video).filter(Video.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'tutorial'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tutorial_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

