import datetime

from django import forms
from django.core.exceptions import ValidationError
# gettext_lazy é uma função para internacionalizar o programa (trocar strings)
from django.utils.translation import gettext_lazy as _


class RenovarDevolucaoLivro(forms.Form):
    nova_data_de_devolucao = forms.DateField(
        help_text="Insira a nova data de devolução do livro, sendo no máximo daqui a 4 semanas (3 por padrão)"
    )

    # Se quisermos aplicar algum tipo de validação nos campos do formulário, usamos o método
    # clean_<nome_do_campo>
    def clean_nova_data_de_devolucao(self):

        # O dicionário self.cleaned_data contém os dados do formulário que já foram pré-validados
        # pelos validadores padrão do Django (caracteres especiais, encoding, etc)
        data = self.cleaned_data["nova_data_de_devolucao"]

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("Data de renovação inválida - Maior do que 4 semanas"))

        # Sempre lembrar de retornar o dado validado
        return data
