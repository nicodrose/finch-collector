from django.shortcuts import render

finches = [
  {'name': 'Lana', 'breed': 'canary', 'description': 'loves singing', 'age': 7},
  {'name': 'Juno', 'breed': 'gold', 'description': 'flies around everywhere', 'age': 3},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })