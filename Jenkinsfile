node{

    def Appdir = "/var/www/django-app"

    stage("Clean Workspace"){

        echo "Cleaning workspace Directory"

        deleteDir()

    }

    stage("Cloneing Repo"){

        echo "cloning project Repo....."

        git(
            branch: 'main',
            url: 'https://github.com/Eagle766/Django_CI_CD.git'

        )
    } 

    stage("Deploying to Ec2"){

        echo "Application deploying......."

        sh """ 
            sudo mkdir -p ${Appdir}

            sudo chown -R jenkins:jenkins ${Appdir}

            rsync -av --delete --exclude='.git' ./  ${Appdir}
            cd ${Appdir}

             python3 -m venv venv
            . venv/bin/activate

            pip install -r requirement.txt

            python manage.py migrate

            python manage.py runserver
        
        """
    }
}