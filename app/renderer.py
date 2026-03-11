from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField()
