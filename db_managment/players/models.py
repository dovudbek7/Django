from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='club_logos/')

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Players(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.PositiveIntegerField(blank=True)
    player = models.ForeignKey(
        Players,
        default=True,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
