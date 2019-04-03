from django.db import models
# from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)

	date_modified=models.DateTimeField(auto_now=True)

	date_published=models.DateTimeField()

	title=models.CharField(
		max_length = 100,
	)

	producer=models.CharField(
		max_length=50,
		null = True,
		blank = True,
	)


class Song(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)

	date_modified=models.DateTimeField(auto_now=True)

	date_published=models.DateField()

	album = models.ForeignKey(
		Album,
		models.CASCADE,
		null=True,
		blank=True,
		related_name='songs',
	)

	title=models.CharField(
		max_length = 100,
	)

	writer=models.CharField(
		max_length = 50,
		null = True,
		blank = True,
	)

	link=models.CharField(
		max_length = 150,
		null = True,
		blank = True,
	)

	class Meta:
		unique_together = ('album', 'title')


class Concert(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)

	date_modified=models.DateTimeField(auto_now=True)

	date_start = models.DateField()

	date_finish= models.DateField()

	location = models.CharField(
		max_length = 100,
	)

	# geo_location = PointField(
	# 	null = True,
	# 	blank = True,
	# )


class Ticket(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)

	date_modified=models.DateTimeField(auto_now=True)

	consumer = models.ForeignKey(
		Concert,
		on_delete=models.CASCADE,
		related_name='tickets'
	)
