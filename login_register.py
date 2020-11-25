from flask import Flask, url_for, render_template
from flask_restful import Api, Resource, reqparse, inputs
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
api = Api(app)
app.config.from_object(config)
db = SQLAlchemy(app)

#213
class User(db.Model):
    __tablename = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))



class RegisterView(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("password",  required=True)
        parser.add_argument("username",  required=True)
        args = parser.parse_args()
        print("获取全部传来的值:",args)
        print("打印前端传来的值：",args.get("username"))
        print("打印前端传来的值：",args.get("password"))
        u = args.get("username")
        p = args.get("password")
        u1 = User.query.filter(User.username == u).first()
        if u1:
            return {"kk":":  用户名存在"}
        else:
            new_u = User(username = u,password = p)
            db.session.add(new_u)
            db.session.commit()
            return {"kk": ":   注册成功"}


api.add_resource(RegisterView, "/data_register/")


class Send_ajax(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("password",  required=True)
        parser.add_argument("username",  required=True)
        args = parser.parse_args()
        print("获取全部传来的值:",args)
        print("打印前端传来的值：",args.get("username"))
        print("打印前端传来的值：",args.get("password"))
        return {"password": args.get("password")}


api.add_resource(Send_ajax, "/data_login/")


@app.route('/login/')
def login():
    print("主页")
    return render_template("login.html")


@app.route('/')
def register():
    return render_template("register.html")


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)