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

========
Cadastro
========

========
Consulta
=======

======
Edição
======

========
Exclusão
========

===========
Referências
===========

