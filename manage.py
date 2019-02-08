from app import create_app,db
from flask_script import Manager,Server, Shell
from app.models import User

# Creating app instance
app = create_app('development')

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
manager.add_command('server',Server)

manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()