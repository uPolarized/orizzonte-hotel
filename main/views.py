from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PollOption
import json # <<< --- ADICIONE ESTA LINHA ---


def home(request):
    # Se já tiver modelo de links, pode buscar do banco e passar no contexto.
    # Ex.: from .models import Link; links = Link.objects.filter(visible=True).order_by('order')
    # Por enquanto, usa uma lista vazia:
    links = []
    return render(request, "home.html", {"links": links})

# NOVA VIEW PARA BUSCAR OS DADOS
def get_poll_data(request):
    options = PollOption.objects.all()
    data = [{'id': option.id, 'text': option.option_text, 'votes': option.votes} for option in options]
    return JsonResponse(data, safe=False)

# NOVA VIEW PARA ADICIONAR UM VOTO
@csrf_exempt # Simplificação para este exemplo, mas em produção o ideal é usar o token CSRF no JS
def add_poll_vote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        option_id = data.get('option_id')
        try:
            selected_option = PollOption.objects.get(id=option_id)
            selected_option.votes += 1
            selected_option.save()
            return JsonResponse({'status': 'success', 'message': 'Voto computado!'})
        except PollOption.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Opção não encontrada'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)