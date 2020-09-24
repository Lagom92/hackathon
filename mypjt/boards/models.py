from django.db import models


class Landmark(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    # 랜드마크 이미지 url
    # 랜드마크 정보 

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    # 작성 날짜
    # 스코어 ?

    def __str__(self):
        return self.content
