from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """����� �����������"""
    username = StringField('�����', validators=[DataRequired()])
    password = PasswordField('������', validators=[DataRequired()])
    remember_me = BooleanField('��������� ����')
    submit = SubmitField('�����')


class RegisterForm(FlaskForm):
    """����� �����������"""
    user_name = StringField('��� ������������', validators=[DataRequired()])
    email = StringField('Email �����', validators=[DataRequired(), Email()])
    password_hash = PasswordField('������', validators=[DataRequired()])
    confirm = PasswordField('��������� ������', validators=[DataRequired()])
    accept_tos = BooleanField('� �������� ������������ ����������', validators=[DataRequired()])
    submit = SubmitField('������� ������� ������')


class AddCarForm(FlaskForm):
    """����� ���������� ����������"""
    model = StringField('������', validators=[DataRequired()])
    price = IntegerField('����', validators=[DataRequired()])
    power = IntegerField('�������� (�.�.)', validators=[DataRequired()])
    color = StringField('����', validators=[DataRequired()])
    dealer_id = SelectField('����� ���������� ������', coerce=int, validators=[DataRequired()])
    submit = SubmitField('�������� ����������')


class AddDealerForm(FlaskForm):
    """���������� ���������� ������"""
    name = StringField('��������', validators=[DataRequired()])
    address = StringField('�����', validators=[DataRequired()])
    submit = SubmitField('�������� ��������� �����')


class SearchPriceForm(FlaskForm):
    """����� ������ �� ����"""
    start_price = IntegerField('����������� ����', validators=[DataRequired()], default=500000)
    end_price = IntegerField('������������ ����', validators=[DataRequired()], default=1000000)
    submit = SubmitField('�����')


class SearchDealerForm(FlaskForm):
    """����� ������ �� ���������� ������"""
    dealer_id = SelectField('����� ���������� ������', coerce=int, validators=[DataRequired()])
    submit = SubmitField('�����')
