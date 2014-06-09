from django.db import models

class Ticket(models.Model):
	name = models.CharField(max_length=255)
	is_closed = models.BooleanField(default=False)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	submitter = models.ForeignKey("auth.User")

