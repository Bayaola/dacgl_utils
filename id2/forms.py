#-*- coding: utf-8 -*-

from django import forms

from id2.models import Service

class InscriptionForm(forms.Form):
    """
    Ce formulaire s'occupe des inscriptions dans le syst�me.
    Et donc pour toutes les personnes pas encore identifi�es
    """
    SEXE = (('H',u'homme'),('F',u'femme'),)

    PIECE = (
            ('cni',u'CNI'),
            ('passeport',u'passeport'),
            ('recepisse',u'recepisse'),
            ('autre',u'autre carte'),
            )

    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=150,required=False)
    sexe = forms.ChoiceField(choices=SEXE)
    typePiece = forms.ChoiceField(label='Type de piece',choices=PIECE)
    code = forms.CharField(max_length=60,
            help_text=u"Numero ou identifiant de la piece.")
    date_expiration=forms.DateField(
                required=False,
                help_text="Format: DD/MM/YYYY",
    )
    email = forms.EmailField(
            required=False
    )
    telephone = forms.IntegerField(
            required=False
    )

class VisiteForm(forms.Form):
    """
    Enregistrement des visites d'usager
    """

    nom = forms.CharField()
    prenom = forms.CharField()
    service = forms.ModelChoiceField(\
            queryset=Service.objects.all().order_by('nom_serv'))
    motif = forms.CharField(widget=forms.Textarea,
            initial=u"visite")

class RechercheForm(forms.Form):
    nom = forms.CharField()

class AbonnementForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    matricule = forms.CharField(max_length=60,
            #FIXME : pourquoi avec les accents �a g�n�re une erreur ?
            #(unicode error) 'utf8' codec can't decode byte 0xe9 ...
            help_text=u"Code genere suivants les regles du service")
    photo = forms.ImageField(required=False)
    expiration = forms.DateField()
