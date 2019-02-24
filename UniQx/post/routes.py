from flask import render_template, flash, Blueprint
from UniQx.models import Post
from UniQx import db
from flask_login import login_required
from UniQx.post.forms import PostForm

post = Blueprint('post', __name__)

@post.route('/post/new')
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, image=form.image.data, content=form.content.data)
	db.session.add(post)
	db.session.commit()
	flash("Post have been created")
	return redirect(url_for('main.about'))
    return render_template('create_post.html', title='Profile', form = form)
