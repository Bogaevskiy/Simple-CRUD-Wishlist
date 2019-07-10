from django.db import models

class Wish(models.Model):
	title = models.CharField(max_length = 150, db_index = True)
	price = models.CharField(max_length = 150, blank = True)
	link = models.URLField(blank = True)
	note = models.TextField(max_length = 300, blank = True)

	def __str__(self):
		return self.title
