		Instalação (No diretório do ambiente virtual)
			yum install sqlite-devel git

			virtualenv egito
   
                        cd egito

			pip install "pyramid==1.6"

			bin/pcreate -s alchemy  tutorial

			rm -rf tutorial/*
			
			git clone https://github.com/wagnerwar/piramid.git tutorial
			
			cd tutorial/
			
			python setup.py develop
			
			cd ../

			bin/initialize_tutorial_db tutorial/development.ini
