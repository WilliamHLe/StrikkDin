from django.db import models


class Inquiries(models.Model):
    """
    En generell modell som består av ulike meldings-felter som representeres i databasen
    Null=True tillater at det kan representeres som NULL i databasen.
    auto_now=True viser den dato og tid meldingen ble sendt.
    """
    text_from = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now=True)

    class Meta:
        """
        Ordering er en av blant flere "Meta-options" som Django tilbyr.
        Den er reservert til sortering. I dette tilfelle sorterer den meldingene i stigende rekkefølge.
        "-" som prefiks, altså ['-created-at'] vil den sortere meldingene i synkende rekkefølge, uten "-" sorteres det stigende.
        "?" som prefiks vil det sorteres tilfeldig.
        """
        ordering = ['created_at']

    def __str__(self):
        """
        Metoden blir kalt på hver gang man bruker str(objekt).
        Django bruker str(objekt) på flere steder, men mest på Admin-siden.
        Derfor er det hensiktmessig å printe det ut på en leselig format.
        For eksempel under "My actions" på adminsiden vil dette printes ut.

        :return: Tekstreng på format subject/description
        """
        return '{}/{}'.format(self.subject, self.description)
