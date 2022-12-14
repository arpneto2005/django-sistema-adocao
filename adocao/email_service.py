from django.core.mail import send_mail

def enviar_email_confirmacao(adocao):
    assunto = 'Adoção realizada com sucesso!'
    conteudo = f'Parabéns pela adoção do pet {adocao.pet.nome}, com o valor mensal de R$:{adocao.valor}'
    remetente = 'arpneto1987@gmail.com'
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)