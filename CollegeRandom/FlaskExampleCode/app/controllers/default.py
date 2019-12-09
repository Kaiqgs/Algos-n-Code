import datetime
from app import app,db, login_manager
from flask import render_template,flash,redirect,url_for
from flask_login import login_user,logout_user,current_user


from app.models.forms import SignupForm, LoginForm, AddVeterinaryForm, AddPetForm, AddServiceForm
from app.models.tables import User, Veterinarian, Pet, Service

import app.models.tables as tables

# table_objects = { name:obj for name, obj in inspect.getmembers(tables)
#                 if(inspect.isclass(obj) and issubclass(obj, db.Model)) }

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/<user>")
@app.route("/", defaults = {"user":"usuário"})
def index(user):
    return render_template("index.html",user=user)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user and user.password == form.password.data):
            login_user(user)
            #flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválido!")


    return render_template("login.html",form=form)

@app.route("/signin")
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/signup", methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data, form.password.data)
        existUser = User.query.filter_by(email=form.email.data).first()
        if(not existUser):
            db.session.add(user)
            db.session.commit()
            flash("Conta criada! Já pode fazer o login!")
        else:flash("Email já utilizado")
    return render_template("signup.html", form=form)



@app.route("/veterinarians",methods= ["GET","POST"])
def veterinarians():
    if(current_user.is_authenticated):
        form = AddVeterinaryForm()
        form.gender.choices = [(-1,"Não definir"),(1,"Masculino"),(0,"Feminino")]
        if(form.validate_on_submit()):
            veterinarian = Veterinarian(name=form.name.data,
                                        age=form.age.data,
                                        gender=form.gender.data,
                                        email=form.email.data)

            if(veterinarian not in current_user.veterinarians):
                veterinarian.users.append(current_user)
                db.session.add(veterinarian)
                db.session.commit()
                flash("Veterinário adicionado!")
                return redirect(url_for("veterinarians"))
            else:flash("Veterinário já existe!")
        return render_template("veterinarians.html", form=form)
    else: return redirect(url_for("index"))

@app.route("/pets",methods=["GET","POST"])
def pets():
    if(current_user.is_authenticated):
        form = AddPetForm()
        form.gender.choices = [(-1,"Não definir"),(1,"Masculino"),(0,"Feminino")]
        if(form.validate_on_submit()):
            pet = Pet(name = form.name.data,
                      age = form.age.data,
                      race = form.race.data,
                      gender = form.gender.data,
                      owner_name = form.owner_name.data)

            if pet not in current_user.pets:
                current_user.pets.append(pet)
                db.session.add(pet)
                db.session.commit()
                flash("Pet adicionado!")
                return redirect(url_for("pets"))
            else:flash("Pet já existe!")
        return render_template("pets.html", form=form)
    else: return redirect(url_for("index"))

@app.route("/services", methods=["GET","POST"])
def services():
    if(current_user.is_authenticated):
        form = AddServiceForm()
        form.veterinarian_name.choices = [(i,vet.name) for i,vet in enumerate(current_user.veterinarians)]
        form.pet_name.choices = [(i, pet.name) for i,pet in enumerate(current_user.pets)]

        if(form.validate_on_submit()):
            pet = current_user.pets[form.pet_name.data]
            veterinarian = current_user.veterinarians[form.veterinarian_name.data]

            service = Service(veterinarian_name = veterinarian.name,
                      pet_name = pet.name,
                      price = form.price.data,
                      description = form.description.data,
                      date = datetime.datetime.utcnow())

            if(service not in current_user.services):
                current_user.services.append(service)
                db.session.add(service)
                db.session.commit()
                flash("Serviço adicionado!")
                return redirect(url_for("services"))
            else:flash("Esse serviço já foi adicionado!")
        return render_template("services.html", form=form)
    else: return redirect(url_for("index"))


@app.route("/remove/<obj_name>/<int:idx>",methods=["GET","POST"])
def remove(obj_name=None, idx=None):
    current_user.services;
    current_user.veterinarians;
    current_user.pets;
    dict = current_user.__dict__
    print(obj_name, idx, len(dict), dict)
    if(obj_name in dict.keys() and 0 <= idx < len(dict)):
        flash("Linha foi removida!")
        db.session.delete(current_user.__dict__[obj_name][idx])
        db.session.commit()
        return redirect(url_for(obj_name))
