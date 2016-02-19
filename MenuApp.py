from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/programs.db'
app.config['SECRET_KEY'] = 'daye'
db = SQLAlchemy(app)
Bootstrap(app)


@app.route('/')
def get_programs():
    from Model import Program
    all_p = Program.query.all()
    return render_template('index.html', all_programs=all_p)



class AddProgramForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    year = IntegerField('Year')
    cdsid = StringField('CDSID')
    comment = StringField('Comment')
    submit = SubmitField('Submit')



@app.route('/add', methods=['GET','POST'])
def add_program():
    from Model import Program
    f = AddProgramForm()
    if f.validate_on_submit():
        # add a program
        p = Program(f.name.data, f.year.data, f.cdsid.data, f.comment.data)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('get_programs'))
    return render_template('add.html', form=f)


@app.route('/delete/<int:pid>', methods=['GET'])
def delete_program(pid):
    from Model import Program
    Program.query.filter_by(id=pid).delete()
    return redirect(url_for("get_programs"))



if __name__ == '__main__':
    app.run(debug=True)
