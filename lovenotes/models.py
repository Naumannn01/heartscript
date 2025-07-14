from django.db import models
from django.contrib.auth.models import User
MOOD_EMOJIS = {
    'romantic': '❤️',
    'flirty': '😉',
    'deep': '💌',
    'missing': '😔',
    'nostalgic': '📸',
    'happy': '😊',
    'excited': '🤩',
    'confused': '😵',
    'annoyed': '😤',
    'sad': '😢',
    'angry': '😠',
}


class LoveNote(models.Model):
  MOOD_CHOICES = [
    ('romantic', 'Romantic'),
    ('flirty', 'Flirty'),
    ('deep', 'Deep & Romantic'),
    ('missing', 'Missing You'),
    ('nostalgic', 'Nostalgic'),
    ('happy', 'Happy'),
    ('excited', 'Excited'),
    ('confused', 'Confused'),
    ('annoyed', 'Annoyed'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ]
user=models.ForeignKey(User,on_delete=models.CASCADE)
to_name=models.CharField(max_length=100)
mood=models.CharField(max_length=20,choices=MOOD_CHOICES)
memory=models.TextField(blank=True,null=True)
generated_text=models.TextField()
created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'To {self.to_name}({self.mood})'