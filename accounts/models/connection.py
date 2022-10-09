from django.db import models
from accounts.models.users import User
from django.core.exceptions import ValidationError
from accounts.custom_managers import ConnectionManager


class Connection(models.Model):
    ACTION_TYPE = (
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_connections")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_connections")
    accepted_or_rejected = models.CharField(choices=ACTION_TYPE, max_length=20, blank=True)
    objects = ConnectionManager()

    def save(self, *args, **kwargs):
        if self.user1 == self.user2:
            return ValidationError("User can't connect with self.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user1_id} and {self.user2_id}"


class BlockList(models.Model):
    friends = models.ManyToManyField(User)

    def __str__(self):
        return str(id)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.user == self.follower:
            return ValidationError("User can't follow self.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} - {self.follower_id}"
