"""Send file to create sample data for Mental Keep Application"""

from models import User, Questions, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#Clear user table if it is not empty
User.query.delete()

#Add User

#Add Questions
q1 = Questions(question='Little interest or pleasure in doing things')
q2 = Questions(question='Feeling down, depressed, or hopeless')
q3 = Questions(question='Trouble falling or staying asleep, or sleeping too much')
q4 = Questions(question='Feeling tired or having little energy')
q5 = Questions(question='Poor appetite or overeating')
q6 = Questions(question='Feeling bad about yourself - or that you are a failure or have let yourself or your family down')
q7 = Questions(question='Trouble concentrating on things, such as reading the newspaper or watching television')
q8 = Questions(question='Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual')
q9 = Questions(question='Thoughts that you would be better off dead or of hurting yourself in some way')


#Add new objects
db.session.add_all([q1, q2, q3, q4, q5, q6, q7, q8, q9])

#Commit
db.session.commit()