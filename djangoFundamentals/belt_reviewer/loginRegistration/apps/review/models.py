from django.db import models
from __future__ import unicode_literals
# Create your models here.
class Author(models.Model):
	# id
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
	# id
	author = models.ForeignKey(Author, related_name='books')
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# Author

class Review(models.Model):
	# id
	book = models.ForeignKey(Book, related_name="book_reviews")
	reviewer = models.ForeignKey(Users, related_name="reviews_ive_written")
	review_text = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# Book